# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

SIZE = 15

MIN_ITEM = 0

MAX_ITEM = 300

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

minimum = 0

maximum = 0

for i in range(SIZE):
    if array[i] < array[minimum]:
        minimum = i
    elif array[i] > array[maximum]:
        maximum = i

min_number = print(f'minimum - {array[minimum]}')

max_number = print(f'maximum - {array[maximum]}')

temp_var = array[minimum]

array[minimum] = array[maximum]

array[maximum] = temp_var

print(array)
