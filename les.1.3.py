x_first = int(input("Введите x1"))
y_first = int(input("Введите y1"))

x_second = int(input("Введите x2"))
y_second = int(input("Введите y2"))

k = int
b = int

k = float((x_second - x_first) / (y_second - y_first))

b = float(y_first - k * x_first)

if b <= 0:
    print(f'уравнение вида: y = {k}x{b}')

else:
    print(f'уравнение вида: y = {k} + x{b}')

# Алгоритм предполагает вывод без условия поскольку вероятно есть более
# оптимальные способы вывода






