from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv('.env.prod' if os.environ.get('FLASK_ENV') == 'PROD' else '.env.dev')

def make_celery(app_name, broker, backend, include):
    return Celery(app_name, broker=broker, backend=backend, include=include)

REDIS_URI = os.environ.get("REDIS_URI")

celery = make_celery(
    __name__,
    broker=REDIS_URI,
    backend=REDIS_URI,
    include=[
        'api.utils',
    ]
)
