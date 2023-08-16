#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    list_k = list(a_dictionary.keys())
    for i in list_k:
        number += 1
    return (number)
