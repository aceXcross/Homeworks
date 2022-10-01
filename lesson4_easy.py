# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

km = int(input('введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)
# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
         number = number // 1 + 1
    else:
         number = number // 1
    return number / (10 ** ndigits)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
        return 'Некорректный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
        sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
        sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' % ticket_number
        else:
            return 'Билет %s несчастливый' % ticket_number
number = 123456
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))