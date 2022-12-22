def inner_view_diff(file1, file2):
    file1_keys = set(file1)
    file2_keys = set(file2)

    new_keys = file2_keys.difference(file1_keys)
    removed_keys = file1_keys.difference(file2_keys)
    both_keys = file1_keys.intersection(file2_keys)

    inner_view = {}

    for key in new_keys:
        value = file2[key]
        inner_view[key] = {
            'state': 'added',
            'value': [value]
        }

    for key in removed_keys:
        value = file1[key]
        inner_view[key] = {
            'state': 'deleted',
            'value': [value]
        }

    for key in both_keys:
        value_1 = file1[key]
        value_2 = file2[key]
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            inner_view[key] = {
                'state': 'nested',
                'value': inner_view_diff(value_1, value_2)
            }
        elif file1[key] != file2[key]:
            inner_view[key] = {
                'state': 'changed',
                'value': [value_2, value_1]
            }
        else:
            inner_view[key] = {
                'state': 'unchanged',
                'value': [value_1]
            }

    return inner_view
