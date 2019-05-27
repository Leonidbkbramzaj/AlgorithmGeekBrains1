# задача 2 урок 2

number = int(input("Enter a natural number"))

if number > 0:
    even = odd = 0
    while number > 0:
        if number % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        number = number // 10
    else:
        print("Even numbers " + str(even))
        print("Odd numbers " + str(odd))
else:
    print("Enter a natural number")