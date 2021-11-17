def take_list_from_console(list_length):
    data_list = []
    for i in range(list_length):
        data_list.append(int(input('Enter an integer value: ')))
    return data_list
