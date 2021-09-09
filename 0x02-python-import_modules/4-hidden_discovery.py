#!/usr/bin/python3
from hidden_4 import *
name_list = dir(hidden_4)
if __name__ == "__main__":
    for name in name_list:
        if name[:2] != '__':
            print(name)

