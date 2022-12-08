DATA = {
    'added': '+',
    'deleted': '-',
    'unchanged': ' ',
    'changed': {
        'old_data': '-',
        'new_data': '+'
    }
}


INDENT, TAB = ' ', 4
TEMPLATE = '{0}{1} {2}: {3}'


def stringify(data, depth):
    res = []
    indent = INDENT * (TAB * depth - 2)

    if isinstance(data, dict):
        res.append('{')
        for key, value in data.items():
            res.append(TEMPLATE.format(
                indent,
                ' ',
                key,
                stringify(value, depth + 1)
            ))
        res.append(f'{INDENT * (TAB * (depth - 1))}}}')
    else:
        res.append(str(data))
    return '\n'.join(res)


def formatter(data, depth=1):
    res = ['{']
    indent = INDENT * (TAB * depth - 2)

    for key, value in sorted(data.items()):
        state = value.get('state')
        value = value.get('value')
        if state == 'changed':
            res.append(TEMPLATE.format(
                indent,
                DATA[state]['old_data'],
                key,
                stringify(value[1], depth + 1)
            ))
            res.append(TEMPLATE.format(
                indent,
                DATA[state]['new_data'],
                key,
                stringify(value[0], depth + 1)
            ))
        elif state != 'nested':
            res.append(TEMPLATE.format(
                indent,
                DATA[state],
                key,
                stringify(value[0], depth + 1)
            ))

        else:
            res.append(TEMPLATE.format(
                indent,
                ' ',
                key,
                formatter(value, depth + 1)
            ))
    res.append(f'{INDENT * (TAB * (depth - 1))}}}')

    return '\n'.join(res)
