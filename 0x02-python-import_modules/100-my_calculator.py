#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add,sub,mul,div
    import sys

    if len(sys.argv) -1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators={"+,-,*,/"}
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ope="null"
    if sys.argv[2] == "+":
        ope="add"
    elif sys.argv[2] == "-":
        ope="sub"
    elif sys.argv[2] == "*":
        ope="mul"
    else:
        ope="div"
    print(a," ",sys.argv[2]," ",b," = ",ope(a,b))
