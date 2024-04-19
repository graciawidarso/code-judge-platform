from flask import Blueprint, request, jsonify
from datetime import datetime
import os

from api.config.logger import logger
from api.config.settings import load_config
from api.utils import (
     check_problem
)
from api.resources.tokens import check_token_validity

submit_bp = Blueprint('submit_bp', __name__)

config = load_config()
ENV = config["ENV"]

@submit_bp.route("/submit-answer", methods=["POST"])
def submit_answer():
     code = request.form["userCode"]
     user_token = request.form["token"]
     problem_id = request.form["problemId"]

     logger.info(f"Request body. Token: {user_token}; problem ID: {problem_id}; user code: {code}")

     if not user_token:
          return jsonify({
               "code": "error",
               "msg": "Please provide token."
          })
     
     if not problem_id:
          return jsonify({
               "code": "error",
               "msg": "Please provide problem id."
          })

     # cek user token
     is_token_valid = check_token_validity(user_token)
     if not is_token_valid:
          return jsonify({
               "code": "error",
               "msg": "Invalid Token."
          })

     # Filename to save the code
     current_timestamp = int(datetime.now().timestamp())
     filename = f'{user_token}-{str(current_timestamp)}'

     if ENV == "DEV":
          file_dir = f'api/files/{filename}.py'
     else:
          shared_volume_path = '/files/shared/data'  # Path to shared volume
          file_dir = os.path.join(shared_volume_path, f"{filename}.py")

     # Save the code to a file
     with open(file_dir, 'w') as file:
          file.write(code)

     task = check_problem.delay(filename, problem_id)
     logger.info(f"Task Id: {task}")
     return jsonify({
          "code": "task",
          "taskId": task.id,
          "msg": None
     })
