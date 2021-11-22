from pymongo import results
from datapipeline.utils.utils import read_json_file
from datapipeline.app_conf import DATA_FILE_PATH
from datapipeline.handlers.transform import Transformer
from datapipeline.utils.db_utils import insert_multiple_record, get_records
from datapipeline.app_conf import CRYPTO_COLLECTION


def handle_load_data():
    try:
        print("In Load data")
        data = read_json_file(DATA_FILE_PATH)
        converted_data = [v for k,v in data.items()]
        transformer = Transformer(converted_data)
        transformed_data = transformer.transform()
        insert_multiple_record(CRYPTO_COLLECTION, transformed_data)
        return {"isSuccess": True, "message": "Data loaded successfully", "data": None}
    except Exception as ex:
        print(f"Exception occured - {str(ex)}")
        return {"isSuccess": False, "message": str(ex), "data": None}


def handle_insert_data(data):
    try:
        print("In Insert data")
        transformer = Transformer(data)
        transformed_data = transformer.transform()
        insert_multiple_record(CRYPTO_COLLECTION, transformed_data)
        return {"isSuccess": True, "message": "Data inserted successfully", "data": None}
    except Exception as ex:
        print(f"Exception occured - {str(ex)}")
        return {"isSuccess": False, "message": str(ex), "data": None}


def handle_query_data(data):
    try:
        print("In query data")
        symbol = data.get("symbol")
        query = {"symbol":symbol.lower()}
        results = get_records(CRYPTO_COLLECTION, query, {"_id": 0})
        return {"isSuccess": True, "message": "Data fetched successfully", "data": results[0] if results else []}
    except Exception as ex:
        print(f"Exception occured - {str(ex)}")
        return {"isSuccess": False, "message": str(ex), "data": None}