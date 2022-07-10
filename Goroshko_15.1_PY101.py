import pandas as pd
import json
from pprint import pprint


def read_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        pprint(data)


def read_excel(path):
    data = pd.read_excel(path, sheet_name="Sheet1")
    print(data)


name_1 = "Land Cruiser Prado.json"
read_json(name_1)
print()

name_2 = "Land Cruiser Prado.xlsx"
read_excel(name_2)
