from gendiff.parser import get_method
import os


def true_false(value):
    if type(value) == bool and value:
        return 'true'
    elif type(value) == bool and not value:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def generate_diff(file1, file2):
    _, ext1 = os.path.splitext(file1)
    _, ext2 = os.path.splitext(file2)

    method1 = get_method(ext1)
    method2 = get_method(ext2)

    file1 = method1(open(file1))
    file2 = method2(open(file2))

    all_keys = list(set(file1).union(set(file2)))
    all_keys.sort()

    res = '{\n'

    for key in all_keys:
        if key in file1 and key in file2:
            value1 = true_false(file1[key])
            value2 = true_false(file2[key])

            if value1 != value2:
                res += f'  - {key}: {value1}\n  + {key}: {value2}\n'
            else:
                res += f'    {key}: {value1}\n'
        elif key in file1 and key not in file2:
            value1 = true_false(file1[key])
            res += f'  - {key}: {value1}\n'
        else:
            value2 = true_false(file2[key])
            res += f'  + {key}: {value2}\n'

    res += '}'

    return res
