def revert_arr_slice(array):
    return array[::-1]


def revert_reverse(array):
    array.copy().reverse()
    return array


def revert_range(array):
    until = int((len(array) + 1) / 2)
    for i in range(0, until, 1):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
    return array
