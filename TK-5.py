from math import sqrt


def sqrt_elements(data_list):
    new_list = map(lambda element: (sqrt(element) if element >= 0 else 'Error'), data_list)
    return [str((round(elem, 2)) if not isinstance(elem, str) else elem) for elem in new_list]
