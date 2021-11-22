from logging import debug
from flask import Flask, request, jsonify

from datapipeline.handlers.handler import handle_load_data, handle_insert_data, handle_query_data
from datapipeline.app_conf import PORT

app = Flask(__name__)

@app.route('/load_data', methods = ['POST'])
def load_data():
    return jsonify(handle_load_data())

@app.route('/insert_data', methods = ['POST'])
def insert_data():
    data = request.get_json()
    print(f"Data received - {data}")
    return jsonify(handle_insert_data(data))

@app.route('/query_data', methods = ['POST'])
def query_data():
    data = request.get_json()
    print(f"Data received - {data}")
    return jsonify(handle_query_data(data))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=False, threaded=True)