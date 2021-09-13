#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_ = my_list[0]
        for x in range(1, len(my_list)):
            if my_list[x] > max_:
                max_ = my_list[x]
    else:
        return None

    return max_
