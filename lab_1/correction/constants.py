import json


def json_loader(filename: str) -> dict:
    with open(filename, "r") as texts_json:
        return json.load(texts_json)

LISTMESSAGETEXT = ["_", ';']

DATA = json_loader('texts.json')
