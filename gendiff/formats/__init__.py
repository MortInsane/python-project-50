from gendiff.formats import stylish, plain, json


FORMATS = {
    'stylish': stylish.formatter,
    'plain': plain.formatter,
    'json': json.formatter
}


def choose_format(format):
    return FORMATS.get(format)
