#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    cal = 0
    op_ = sys.argv[2]
    if op_  == '+':
        cal = add(a, b)
    elif op_ == '-':
        cal = sub(a, b)
    elif op_ == '*':
        cal = mul(a, b)
    elif op_ == '/':
        cal = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, op_, b, cal))
