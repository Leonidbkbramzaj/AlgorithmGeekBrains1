import random

print("Выберите число от 1 до 3")
print("1 - Возвращает псевдослучайное целое число из заданного диапазона")
print("2 - Возвращает псевдослучайное вещественное число из заданного диапазона")
print("3 - Возвращает псевдослучайный символ из заданной строки символов")

user_choice = int(input("введите число от одного до трех"))

if user_choice == 1:
    min_range = int(input("введите нижнюю границу диапазона"))
    max_range = int(input("введите верхнюю границу диапазона"))
    number_x = random.randint(min_range, max_range)
    print(f"Псевдослучайное целое число: {number_x}")

elif user_choice == 2:
    min_range_m = int(input("введите нижнюю границу диапазона"))
    max_range_m = int(input("введите верхнюю границу диапазона"))
    number_y = random.uniform(min_range_m, max_range_m)
    print(f"Псевдослучайное вещественное число: {number_y}")

elif user_choice == 3:
    symbol_string = input("Введите набор символов")
    symbol_z = random.choice(symbol_string)
    print(symbol_z)

else:
    print("введите число от 1 до 3 перезапустив программу")

