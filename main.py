#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit
from importlib import import_module
from prettytable import PrettyTable
from TK_1 import take_list_from_console
from TK_2 import find_min_max_values
from TK_3 import division_elements_by_average
from TK_4 import multiplication_elements_by_average
mod_TK5 = import_module("TK-5")


def main():
    data = take_list_from_console(int(input('\nEnter length of a list: ')))

    table = PrettyTable()
    table.field_names = ['Processing operations over a list', 'Results']
    table.align['Processing operations over a list'] = 'l'
    table.align['Results'] = 'l'
    table.add_row(['Minimum and maximum values in the data list', ', '.join(find_min_max_values(data))])
    table.add_row(['Each element of the list divided by average value of the list', ', '.join(division_elements_by_average(data))])
    table.add_row(['Each element of the list multiplied by average value of the list', ', '.join(multiplication_elements_by_average(data))])
    table.add_row(['Square root of each element in the list', ', '.join(mod_TK5.sqrt_elements(data))])
    print(table)
    return 0


if __name__ == '__main__':
    exit(main())
