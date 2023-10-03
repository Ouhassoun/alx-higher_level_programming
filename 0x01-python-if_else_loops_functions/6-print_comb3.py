#!/usr/bin/python3
for num1 in range(0, 10):
    for i in range(num1 + 1, 10):
        if num1 == 8 and i == 9:
            print("{}{}".format(num1, i))
        else:
            print("{}{}".format(num1, i), end=", ")
