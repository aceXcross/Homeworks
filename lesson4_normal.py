# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1, 1]

    for i in range(2, m):
        new_element = fib_list[-1] + fib_list[-2]
        fib_list.append(new_element)
    return fib_list[n:m]

a = fibonacci(2, 5)
for i in a:
    print(i)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len (origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_function(func,iterable):
    output_iterable = []
    for i in range(len(iterable)):
        if func(iterable[i]) == True:
            output_iterable.append(iterable[i])
    return output_iterable

func = lambda x: type(x) == str
iterable = [-1, 2, 'a', 4, 'fgf']
print(filter_function(func,iterable))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

from math import sqrt

print('Введите координаты точек в двумерной плоскости: \n'
      'А0(х0, у0), А1(х1, у1), А2(x2 ,у2), А3(x3 , у3))')
x = [int(input('x{} = '.format(x))) for x in range(0,4)]
y = [int(input('y{} = '.format(y))) for y in range(0,4)]

sides = []
for i in range(0,4):

    if i == 3:
        side = [x[0] - x[i], y[0] - y[i]]
    else:
        side = [x[i + 1] - x[i], y[i + 1] - y[i]]

    sides.append(sqrt(side[0]**2 + side[1]**2))
print(sides)
if sides[0] == sides[2] and sides[1] == sides[3]:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')
