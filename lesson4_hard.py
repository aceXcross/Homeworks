# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

fractInput = input("Введите выражение сложения дробей в формате (-)n x/y -/+ (-)n x/y: ")

def fractSplit(fract):
    fract = fract.strip()
    #Parsing data from fraction string to variables
    try:
        minusIndex = fract.find("-", 1) #Со второго элемента, чтобы не захватить минус первой дроби
        plusIndex = fract.find("+", 1)

        if minusIndex != -1 and plusIndex != -1:
            if minusIndex > plusIndex:
                delimInd = plusIndex
                delim = +1
            else:
                delimInd = minusIndex
                delim = -1
        elif minusIndex != -1 and plusIndex == -1:
            delimInd = minusIndex
            delim = -1
        elif minusIndex == -1 and plusIndex != -1:
            delimInd = plusIndex
            delim = +1

        leftPart = fract[:delimInd].strip()
        rightPart = fract[delimInd+1:].strip()

        if len(leftPart.split()) > 1:
            leftWhole, leftFract = leftPart.split()
        else:
            leftWhole = 0
            leftFract = leftPart

        if len(rightPart.split()) > 1:
            rightWhole, rightFract = rightPart.split()
        else:
            rightWhole = 0
            rightFract = rightPart


        leftWhole = int(leftWhole)
        leftNumer, leftDenom = list(map(int, leftFract.split("/")))

        rightWhole = int(rightWhole)
        rightNumer, rightDenom = list(map(int, rightFract.split("/")))

        #Subtraction of given fractions

        if leftWhole != 0:
            leftNumer = leftWhole * leftDenom + (leftNumer if leftWhole > 0 else -leftNumer)
        if rightWhole != 0:
            rightNumer = rightWhole * rightDenom + (rightNumer if rightWhole > 0 else -rightNumer)

        if rightDenom == leftDenom:
            subNumer = leftNumer + rightNumer * delim
            subDenom = rightDenom or leftDenom
        else:
            subNumer = leftNumer * rightDenom + rightNumer * leftDenom * delim
            subDenom = rightDenom * leftDenom

        resNumer = subNumer % subDenom
        resWhole = int(subNumer/subDenom)
        resDenom = subDenom

        #If higher term fraction i.e. 2/4 or 3/6 or 2/6 or 13/169 or 88/1014

        for i in range(2,9):
            while resDenom % i == 0 and resNumer % i == 0:
                resDenom = resDenom/i
                resNumer = resNumer/i

            if resDenom % resNumer == 0:
                resDenom = resDenom/resNumer
                resNumer = 1

        #Format of return

        if resNumer != 0 and resWhole != 0:
             returnString = "{0} {1}/{2}"
        elif resNumer == 0:
             returnString = "{0}"
        elif resWhole == 0:
             returnString = "{1}/{2}"

        return returnString.format(resWhole, int(resNumer), int(resDenom))

    except ValueError:
        return "Введенная дробь не соответсвует формату n x/y или указаны отличные или лишние знаки операции или пробелы."
    except UnboundLocalError:
        return "Введен нераспозноваемый набор символов"

fraction = "5 12/1014 + 6 66/1014"

print(fractSplit(fractInput))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import re
print('-' * 50)
print('Задача 2')
person = []
hours = []
info =[]
workers = open('data/workers.txt', 'r', encoding ='utf-8')
for line in workers:
    person.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()

hours = open('data/hours_of.txt', 'r', encoding ='utf-8')
for line in hours:
    hours.append(re.findall(r'[А-я]+\s?[А-я]+|[0-9]+', line))
hours.close()

cvit = open('data/cvit_of_price.txt', 'w', encoding ='utf-8')
cvit.write('Имя Фамилия Заработанная плата\n')
# убираем из матриц строку с названием колонок

info_person = person[1:]
info_hours = hours[1:]
for i in info_person:
    name_one_table = i[0]
    surname_one_table= i[1]
    for i in info_hours:
        name_two_table = i[0]
        surname_two_table = i[1]
        if name_one_table == name_two_table and \
            surname_one_table == surname_two_table:
            salary = int(i[2])      # оклад
            hours_norm = int(i[4])  # норма отработанных часов
            hours_work = int(i[2])  # отработано часов
            work = hours_work - hours_norm
            # Усли отработано больше нормы, сверурочную почасовую оплату
            # считаем по двойному тарифу.
            # Если отработано меньше нормы, недоработанную почасовую оплату
            # считаем по текущему тарифу
            if work > 0:
                price = salary + \
                        (2 * (salary / hours_norm) * (hours_work - hours_norm))
            else:
                price = salary + \
                        (salary / hours_norm) * (hours_work - hours_norm)
            # записываем в файл квитанции
            person_data = '{0} {1} {2:.2f}\n'.format(name_one_table,
                                                  surname_one_table,
                                                  price)
            cvit.write(person_data)
            print(person_data.strip())
cvit.close()
print('Зарплатная ведомость сформирована в файле - data/cvit_of_price.txt')

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

dict_fruts = dict()
with open('fruits.txt',encoding='utf-8') as inp_ut:
    for fruits in inp_ut.readlines():
        file_name = 'fruits_{}'.format(fruits[0].upper())
        dict_fruts[file_name] = dict_fruts.get(file_name,'')+fruits
    
for i in dict_fruts:
    name = '{}.txt'.format(i)
    with open(name,'w') as out:
        out.write(dict_fruts[i])
print('Формирование файлов по именам фруктов закончено!')