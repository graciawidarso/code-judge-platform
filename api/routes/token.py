from flask import Blueprint, jsonify, request

from api.utils import generate_secure_random_token
from api.config.db import db

token_bp = Blueprint('token_bp', __name__, url_prefix='/token')

@token_bp.route('/generate-token', methods=["GET"])
def generate_token():
    length = request.args.get("length", 20)
    n_token = int(request.args.get("n", 1))

    if n_token > 100:
        return jsonify({"msg": "Too many number of token request. Max is 100 tokens."})

    token_data = []
    for i in range(n_token):
        new_token = generate_secure_random_token(int(length))
        token_data.append(
            {
                "token_id": new_token,
                "is_used": False
            }
        )

    try:
        db.token.insert_many(token_data)
    except Exception as e:
        return {"msg": f"Failed insert token to db: {e}"}
    
    return {"msg": f"{n_token} is generated and saved to db."}


@token_bp.route('/get-available-token', methods=["GET"])
def get_available_token():
    n_token = request.args.get("n", 1)

    get_token_condition = {
        "is_used": False
    }

    try:
        data_cursor = db.token.find(get_token_condition).limit(int(n_token))
    except Exception as e:
        return {"msg": f"Failed query token: {e}"}
    
    # Convert cursor to list and handle ObjectId
    data_list = list(data_cursor)
    for document in data_list:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string

    result = {
        "count": len(data_list),
        "data": data_list
    }
    return jsonify(result)


@token_bp.route('/reset-token-all', methods=["GET"])
def reset_token_all():
    try:
        result = db.token.update_many(
            {'is_used': True},
            {'$set': {'is_used': False}}
        )
        print(result)
        data = {
            "matched_count": result.matched_count,
            "modified_count": result.modified_count
        }
        return jsonify(data)
    except Exception as e:
        result = {"error": str(e)}
        return jsonify(result)
