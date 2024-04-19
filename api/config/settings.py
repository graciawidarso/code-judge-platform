import os
from dotenv import load_dotenv

def load_config():
    load_dotenv('.env.prod' if os.environ.get('FLASK_ENV') == 'PROD' else '.env.dev')
    return {
        "ENV": os.environ.get("FLASK_ENV", "DEV"),
        "REDIS_URI": os.environ.get("REDIS_URI"),
        "MONGO_USERNAME": os.environ.get("MONGO_USERNAME"),
        "MONGO_PASSWORD": os.environ.get("MONGO_PASSWORD"),
        "MONGO_DB_NAME": os.environ.get("MONGO_DB_NAME")
    }
