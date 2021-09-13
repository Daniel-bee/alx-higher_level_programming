#!/usr/bin/env python3
def no_c(my_string):
    
    for char in my_string:
        if char == 'C' or char == 'c':
            my_string = my_string.translate({ord(char): None})

    return my_string
