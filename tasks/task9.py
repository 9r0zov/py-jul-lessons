def lists_to_dict(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError(f'Length or arrays must be same. Arr1 len: {len(arr1)}, Arr2 len: {len(arr2)}"')

    return {arr1[i]: arr2[i] for i in range(0, len(arr1))}
