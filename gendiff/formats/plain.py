import json


DATA = {
    'added': 'Property \'{0}\' was added with value: {1}',
    'deleted': 'Property \'{0}\' was removed',
    'changed': 'Property \'{0}\' was updated. From {1} to {2}'
}


def stringify(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, str):
        return f'\'{data}\''
    else:
        return json.dumps(data)


def formatter(data, key_name=None):
    if key_name is None:
        key_name = []
    res = []

    for key, value in sorted(data.items()):
        state = value.get('state')
        value = value.get('value')

        key_name.append(key)

        if state == 'added':
            res.append(DATA[state].format(
                '.'.join(key_name),
                stringify(value[0])
            ))
        elif state == 'deleted':
            res.append(DATA[state].format(
                '.'.join(key_name),
                value[0]
            ))
        elif state == 'changed':
            res.append(DATA[state].format(
                '.'.join(key_name),
                stringify(value[1]),
                stringify(value[0])
            ))
        elif state == 'nested':
            res.append(
                formatter(value, key_name)
            )

        key_name.pop()
    return '\n'.join(res)
