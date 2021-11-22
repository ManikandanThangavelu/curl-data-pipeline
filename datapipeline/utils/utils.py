import json

def read_json_file(path):
    with open(path) as infile:
        loaded_json = json.load(infile)
    return loaded_json