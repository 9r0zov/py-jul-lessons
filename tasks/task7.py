def combine_dicts(dict1: dict, dict2: dict):
    return dict1 | dict2


def combine_dicts_upd(dict1: dict, dict2: dict):
    combined = dict1.copy()
    combined.update(dict2)
    return combined
