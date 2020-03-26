def longest_str(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) == len(str2):
        return 'Equal'
    else:
        return str2

assert longest_str('Volvo', 'Audi') == 'Volvo'
assert longest_str('BMW', 'Audi') == 'Audi'
assert longest_str('BMW', 'KEA') == 'Equal'
