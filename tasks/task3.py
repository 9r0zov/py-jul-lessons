def revert_arr_slice(string):
    return string[::-1]


def revert_slice(string):
    return string[slice(-1, -len(string) - 1, -1)]


def revert_range(string):
    result = ""
    for i in range(-1, -len(string) - 1, -1):
        result += string[i]
    return result
