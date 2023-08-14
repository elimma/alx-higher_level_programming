#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lis = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_lis[i] = 1
        else:
            new_lis[i] = 0
    return new_lis
