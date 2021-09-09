#!/usr/bin/python3
import hidden_4
name_list = dir(hidden_4)

if __name__ == "__main__":
    for names in name_list:
        if names[:2] != "__":
            print("{}".format(names))
