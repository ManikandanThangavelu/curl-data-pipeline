import json
import os

#Flask conf
PORT = os.environ.get("PORT", 8000)

#Locations
_root_dir = os.getcwd()
_app_location = os.path.join(_root_dir)
DATA_DIR = os.path.join(_app_location, "data")
DATA_FILE_PATH =  os.path.join(DATA_DIR, "fetchTickers.json")

#Database conf
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "27017")
DB_NAME = "crypto-data"
MONGO_URL = f"mongodb://{DB_HOST}:{DB_PORT}/"

#Collection details
CRYPTO_COLLECTION = "cryptos"