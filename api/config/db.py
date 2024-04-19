import pymongo
from api.config.logger import logger
from api.config.settings import load_config

# Now you can use os.getenv to read the environment variables
config = load_config()
ENV = config['ENV']
MONGO_USERNAME = config['MONGO_USERNAME']
MONGO_PASSWORD = config['MONGO_PASSWORD']
MONGO_DB_NAME = config['MONGO_DB_NAME']

if ENV == 'PROD':
    MONGO_URI = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017'
else:
    MONGO_URI = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@localhost:27017'

try:
    mongo_db_client = pymongo.MongoClient(MONGO_URI)
    db = mongo_db_client[MONGO_DB_NAME]
    # Test the connection
    db.command("serverStatus")
    logger.info(f"Database connection is OK. Connect to DB: {MONGO_DB_NAME}")
except pymongo.errors.ConnectionFailure as e:
    logger.error(f"Could not connect to MongoDB: {e}")
except pymongo.errors.OperationFailure as e:
    logger.error(f"Authentication failed: {e}")
