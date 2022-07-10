import json
from pprint import pprint


def read_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        pprint(data)


name = "Land Cruiser Prado.json"
read_json(name)



