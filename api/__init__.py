from flask import Flask

from api.config.settings import load_config
from api.config.logger import setup_logging
from celery_app import celery

def create_app(): 
    app = Flask(__name__, template_folder='templates', static_folder='static')

    config = load_config()
    ENV = config["ENV"]
    if ENV == 'PROD':
        setup_logging(app)

    REDIS_URI = config["REDIS_URI"]

    app.config['CELERY_BROKER_URL'] = REDIS_URI
    app.config['CELERY_RESULT_BACKEND'] = REDIS_URI
    celery.conf.update(app.config)

    from .routes.home import home_bp
    from .routes.submit import submit_bp
    from .routes.token import token_bp
    from .routes.tasks import task_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(submit_bp)
    app.register_blueprint(token_bp)
    app.register_blueprint(task_bp)

    # Register other blueprints or configure database here

    return app
