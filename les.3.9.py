# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(0, 100) for _ in range(8)] for _ in range(6)]

for line in matrix:
    print(line)



max_number = -1

for i in range(8):
    min_number = 101
    for b in range(6):
        if matrix[b][i] < min_number:
            min_number = matrix[b][i]
    if min_number > max_number:
        max_number = min_number



print(max_number)

