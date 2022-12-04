import json


def true_false(value):
    if type(value) == bool and value:
        return 'true'
    elif type(value) == bool and not value:
        return 'false'
    else:
        return value

    
def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    
    all_keys = list(set(file1).union(set(file2)))
    all_keys.sort()

    res = '{\n'

    for key in all_keys:        
        if key in file1:
            value1 = true_false(file1[key])
        if key in file2:
            value2 = true_false(file2[key])

        if key in file1 and key in file2:
            if value1 != value2:
                res += f'  - {key}: {value1}\n  + {key}: {value2}\n'
            else:
                res += f'    {key}: {value1}\n'
        else:
            if key in file1 and key not in file2:
                res += f'  - {key}: {value1}\n'
            else:
                res += f'  + {key}: {value2}\n'
    res += '}'

    return res
