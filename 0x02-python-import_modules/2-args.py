#!/usr/bin/python3
import sys
arg_len = len(sys.argv)
number = 1
if __name__ == "__main__":
    if arg_len == 1:
        print("{0 arguments.")
    elif arg_len == 2:
        print("{1 argument.")
        print("{}: {}".format(arg_len - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_len - 1))
        for i in range(1, arg_len):
            print("{}: {}".format(i, sys.argv[i]))
