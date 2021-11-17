def division_elements_by_average(data_list):
    new_list = map(lambda element: element / (sum(data_list) / len(data_list)), data_list)
    return [str(round(elem, 2)) for elem in new_list]
