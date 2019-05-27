# задача 1 урок 2

def math_action(a, b, c):
    if c == "+":
        res = a + b
    elif c == "-":
        res = a - b
    elif c == "*":
        res = a * b
    elif c == "/":
        if b != 0:
            res = a / b
        else:
            res = "You cannot divide a number by nil"

    elif c == "0":
        res = "You have finished"
    else:
        res = "Type the correct operator"
    return res



first_number = float(input("Enter the first number"))
second_number = float(input("Enter the second number"))

math_oper = 1


while math_oper != "0":
    math_oper = input("Chose one of the next math operators +, -, *, /")
    print(math_action(first_number, second_number, math_oper))
else:
    math_oper == "0"

