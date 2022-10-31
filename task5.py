def swap_first_last(array):
    if len(array) < 2:
        raise ValueError(f'Length or array must be greater than 2, got len"{len(array)}"')

    array[0], array[len(array) - 1] = array[len(array) - 1], array[0]

    return array
