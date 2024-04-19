from importlib import import_module
from celery.exceptions import SoftTimeLimitExceeded
import os
import sys
import secrets
import string
import inspect
import ast

from api.resources.problem_ids import problem_id_map
from api.config.logger import logger
from api.config.settings import load_config
from celery_app import celery

config = load_config()
ENV = config["ENV"]

def check_problem_id(problem_id):
    problem_name = problem_id_map.get(problem_id)
    if not problem_name:
        return None

    return problem_name
    

def check_test_case(user_function, problem_name):
    try:
        # Directory where the module is located
        # Assuming the 'resources' directory is in the same directory as your current working script
        resources_dir = os.path.join(os.getcwd(), 'api', 'resources', 'problems')

        # Add the directory to sys.path if not already there
        if resources_dir not in sys.path:
            sys.path.insert(0, resources_dir)
        
        module = import_module(problem_name)
    except Exception as e:
        return None, f"Invalid Problem ID: Can't import problem Id {e}"

    module_func = module.test_problem

    result, error = module_func(user_function)
    logger.info(f"result from test_problem: {result}")

    if result is None:
        return None, error
    return result, None


@celery.task(time_limit=10)
def check_problem(filename, problem_id):
    try:
        # cek problem id
        problem_name = check_problem_id(problem_id)
        if not problem_name:
            return {
                "code": "error",
                "msg": "Invalid Problem ID."
            }

        # get user function
        user_function, error = get_user_function(filename)
        if user_function is None:
            return {
                "code": "error",
                "msg": error
            }

        # cek test case
        result, error = check_test_case(user_function, problem_name)

        if error:
            return {
                "code": "error",
                "msg": error
            }
        return {
            "code": "success",
            "msg": result
        }
    except SoftTimeLimitExceeded:
        return "Time Limit."
    except Exception as e:
        return e


def is_safe_to_import(source_code):
    safe_modules = {'math', 'json', 'time'}  # Example whitelist
    unsafe_patterns = {
        'exec', 'eval', 'os.system', 
        'subprocess.call', 'subprocess.run', 'subprocess.Popen',
        'getattr', 'setattr', 
        '__import__', 
        'open', 
        'pickle.loads', 'pickle.load', 
        'eval (in template engines)', 
        'execfile', 'compile', 
        'globals', 'locals'
    }
    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for name in node.names:
                if name.name not in safe_modules:
                    return False
                
    for node in ast.walk(tree):
        # Check for unsafe function calls
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in unsafe_patterns:
                return False

    return True


def get_user_function(filename):
    try:
        # Directory where the module is located
        # Assuming the 'resources' directory is in the same directory as your current working script
        
        if ENV == "DEV":
            resources_dir = os.path.join(os.getcwd(), 'api', 'files')
        else:
            resources_dir = "/files/shared/data"
        
        file_path = os.path.join(resources_dir, f'{filename}.py')

        # Add the directory to sys.path if not already there
        if resources_dir not in sys.path:
            sys.path.insert(0, resources_dir)

        # Read and analyze the source code
        with open(file_path, 'r') as file:
            source_code = file.read()
        
        if not is_safe_to_import(source_code):
            return None, "Unsafe code detected"
        
        module = import_module(filename)
    except Exception as e:
        return None, f"Failed importing file user token: {e}"
    
    try:
        user_function = module.ans
        source_code = inspect.getsource(user_function)
        logger.info(f"this user code from file: {source_code}")
    except AttributeError as e:
        return None, f"Please make sure your function name is ans(). Please reset and please note that your token has been USED at this time."
    except Exception as e:
        return None, f"Failed {e}"
    return user_function, None


def generate_secure_random_token(length=20):
    if length <= 0:
        raise ValueError("Length must be a positive integer")

    # First character: a random alphabet letter
    first_char = secrets.choice(string.ascii_letters)

    # Remaining characters: a mix of digits and letters
    characters = string.ascii_letters + string.digits
    remaining_chars = ''.join(secrets.choice(characters) for _ in range(length - 1))

    # Combine first character with remaining characters
    token = first_char + remaining_chars
    return token
