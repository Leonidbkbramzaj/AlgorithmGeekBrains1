#В диапазоне натуральных чисел от 2 до 99 определить,
#сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_array = [0]*8

print(list_array)

for i in range(2, 100):
    for a in range(2, 10):
        if i % a == 0:
            list_array[a - 2] = list_array[a-2] +1

i = 0
while i < len(list_array):
    print(i + 2, ' - ', list_array[i])
    i += 1






