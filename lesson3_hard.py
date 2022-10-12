# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
name = equation.split(' ')
first_name = str(name[2])
name[2] = first_name[:-1]
two_name = float(name[2]) * x + float(name[4])
print(two_name)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

my_date = input('Введите дату через точку: ')
converted_date = my_date.split('.')
converted_day = int(converted_date[0])
converted_month = int(converted_date[1])
converted_year = int(converted_date[2])
long_month = [1, 3, 5, 7, 8, 10, 12]
if len(converted_date[0]) != 2 or len(converted_date[1]) != 2 or len(converted_date[2]) != 4:
    print('Не корректен формат даты')
elif converted_day > 31 or converted_day < 1:
    print('Введён не корректный день')
elif converted_month > 12 or converted_month < 1:
    print('Введён не корректный месяц')
elif converted_year > 9999 or converted_year < 1:
    print('Введён не корректный год')
elif converted_month not in long_month and converted_day > 30:
    print('Введён не корректный день')
else:
    print('Дата введена корректно: ', my_date)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

d_room = int(input('Elevator: Enter the room number:'))

tower = []  # Создание башни
i = 0  # Rooms counter
x = 0  # Stages counter
f = 0  # Floors counter
d = 0  # Doors from left counter

while i < d_room:

    # Counting stages
    x += 1

    # Creating block
    block = []
    for _ in range(x):

        # Creating floor
        f += 1
        floor = []
        for d in range(x):

            # Counting rooms
            i += 1
            floor.append(i)
            if i == d_room:
                print('location of room:', d_room, '\nfloor:', f, '\ndoor from left:', d + 1)

        block.append(floor)

    tower.append(block)

# Draw the tower in a fun way
print('\n The upended tower will looks like:')
print(str(tower).replace('],', ']\n').replace(']', '').replace('[', '\r').replace(',', ''))