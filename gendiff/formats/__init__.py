from gendiff.formats import stylish, plain


FORMATS = {
    'stylish': stylish.formatter,
    'plain': plain.formatter
}


def choose_format(format):
    return FORMATS.get(format)
