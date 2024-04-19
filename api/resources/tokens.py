from api.config.db import db

class TokenManager:
    """
    False means token is unused
    """
    def __init__(self, collection_name="token"):
        self.collection = collection_name

    def use_token(self, token):
        # Use a token if it exists and is unused
        result = db.token.find_one_and_update(
            {"token_id": token, "is_used": False},
            {"$set": {"is_used": True}}
        )

        if result is not None:
            return True
        return False

    def is_token_used(self, token):
        # Check if a token is used
        token_data = db.token.find_one({"token_id": token})
        return token_data is not None and token_data.get("is_used", True)


def check_token_validity(user_token):
    """
    to check if token is valid.
    """
    is_token_valid = False
    manager = TokenManager()
    is_token_used = manager.is_token_used(user_token)

    if is_token_used:
        is_token_valid = False
    else:
        can_use_token = manager.use_token(user_token)
        if can_use_token:
            is_token_valid = True

    return is_token_valid