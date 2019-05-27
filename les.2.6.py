
# Задание 6 урок 2

import random

def guess_number(user_number, random_number):
    if user_number > random_number:
        res = "Your number is bigger than the generated number"
        return res
    elif user_number < random_number:
        res = "Your number is lesser than the generated number"
        return res
    else:
        res = "You winner! Your number and generated number are equal"
        return res


random_number_ex = random.randint(0, 100)

for i in range(10):
    user_number_ex = int(input("Enter a natural number from 0 to 100"))
    print(guess_number(user_number_ex, random_number_ex))
    if user_number_ex == random_number_ex:
        break


print(f'Your number was {random_number_ex}')










