def make_eq_length(arr):
    max_length = len(max(arr, key=len))

    for i in range(len(arr)):
        elem = arr[i]
        if len(elem) < max_length:
            arr[i] = elem.ljust(max_length, '_')

    return arr
