#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
    last_digit = (-1 * number) % 10

if last_digit  > 5:
    print("Last digit of {:d} is {:d} and is greater than {:d}".format(number, last_digit, 5))
if last_digit == 0:
    print("Last digit of {:d} is {:d} and is {:d}".format(number, last_digit, 0))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than {:d} and not {:d}".format(number, last_digit, 6, 0))
