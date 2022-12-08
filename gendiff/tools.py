def normalize_data(value):
    if type(value) == bool and value:
        return 'true'
    elif type(value) == bool and not value:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
