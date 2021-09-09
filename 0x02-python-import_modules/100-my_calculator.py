#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator is "+":
        print("{} {} {} = {}".format(a, b, operator, add(a, b)))
    elif operator is "-":
        print("{} {} {} = {}".format(a, b, operator, sub(a, b)))
    elif operator is "*":
        print("{} {} {} = {}".format(a, b, operator, mul(a, b)))
    elif operator is "/":
        print("{} {} {} = {}".format(a, b, operator, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
