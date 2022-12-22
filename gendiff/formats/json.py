import json


def formatter(data):
    return json.dumps(data, indent=2, sort_keys=True)
