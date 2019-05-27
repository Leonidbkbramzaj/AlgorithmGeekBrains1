# задача 3 урок 2

number = int(input("Enter a natural number"))

if number > 0:
    reverse_number = 0
    while number > 0:
        reverse_number = reverse_number * 10 + number % 10
        number = number // 10
    else:
        print(reverse_number)

else:
    print("Enter a natural number")