from gendiff.formats import stylish


FORMATS = {
    'stylish': stylish.formatter,
}


def choose_format(format):
    return FORMATS.get(format)
