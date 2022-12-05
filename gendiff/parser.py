import json
import yaml


EXTENSIONS = {
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
    ".json": json.load
}


def get_method(method):
    return EXTENSIONS.get(method)
