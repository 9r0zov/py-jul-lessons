def prod_values(dictionary: dict):
    prod = 1
    for elem in dictionary.values():
        prod *= elem
    return prod
