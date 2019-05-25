# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Введите трехзначное число"))

first_digit = number // 100

second_digit = (number // 10) % 10

third_digit = (number % 10)

sum_digit = first_digit + second_digit + third_digit

multiple_digit = first_digit * second_digit * third_digit

print(f' Сумма цифр числа = {sum_digit}')
print(f' Произведение цифр числа = {multiple_digit}')






