from flask import Blueprint, jsonify
from celery_app import celery

task_bp = Blueprint('task_bp', __name__, url_prefix='/task')

@task_bp.route('/get-task-status/<task_id>')
def get_task_status(task_id):
    task_result = celery.AsyncResult(task_id)
    if task_result.state == "FAILURE":
          return jsonify({"status": task_result.state, "result": str(task_result.result)})
    elif task_result.state == "SUCCESS":
        return jsonify({"status": task_result.state, "result": task_result.get()})
    else:
        return jsonify({"status": "pending"}), 202