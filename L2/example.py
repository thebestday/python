
#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
'''
n = 0
while n < 5:
    n +=1
    print('Это ', n, ' строка из нулей:', '0000000000')


'''


'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

'''
n = 0

for i in range(1, 11):
    s = input('Введите цифру номер {}: ' .format(i))
    while len(s) != 1 or not s.isdigit():
        s = input('Введите цифру номер {}: '.format(i))
    s = int(s)
    if s == 5:
        n += 1
            
print('Вы ввели цифру 5 ,', n, 'раз')
'''





'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
'''
sum = 0
for i in range(1, 101):
    sum += i
print('Сумма ряда чисел от 1 до 100 равна: ', (sum))
'''


'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

'''
Multiplication = 1
for i in range(1, 11):
    Multiplication *= i
print(' Произведение ряда чисел от 1 до 10 равна: ', Multiplication)
'''




'''
Задача 5
Вывести цифры числа на каждой строчке.
(Нужно взять отсток от деления числа на 10)
( деление на цело или  Целочисленное деление в Python обозначается двумя косыми чертами «//»)
# print(intenger_number % 10, intenger_number // 10)


# def rec(n):
#     if n == 0:
#         return
#     else:
#         rec(n // 10)
#         print(n % 10, end=' ')
#
# rec(number)
'''

'''
s = input('Введите положителное число: ')
while s == '' or (s == '/' or s == '*' or s == '-' or s == '+') or s.isalpha() == True or float(s) < 0:
        s = input('Введите положителное число: ')


else:
    number = float(s)
    print('-------')

int_number = int(number)
p = 10
while p < int_number:
    p *= 10
print('-------')

n = 1
while (p // 10) > 0:
    p //= 10
    n = n + 1
print('-------')

while n > 1:
    nu = int(number / 10**(n - 2))
    print(nu % 10)
    n -=1

print('Целая часть числа:', int(number / 10**(n-p)))
'''




'''
Задача 6
Найти сумму цифр числа.

'''
'''
s = input('Введите натуральное число: ')
while not s.isdigit():
    s = input('Введите натуральное число: ')

s = int(s)
sum = 0
while s > 0:
    sum += s % 10
    s = s // 10
print(sum)

'''

'''
Задача 7
Найти произведение цифр числа.
'''
'''
s = input('Введите натуральное число: ')
while not s.isdigit():
    s = input('Введите натуральное число: ')

s = int(s)

Multip = 1
while s > 0:
    Multip *= (s % 10)
    s = s // 10
print(Multip)

'''


'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
'''
s = input('Введите положительное число: ')

while float(s) < 0:
    while not s.isdigit():
        print(float(s))
        s = input('Введите положительное число: ')

integer_number = int(float(s))

while integer_number > 0:
    if integer_number % 10  == 5:
        print('Yes')
        break
    integer_number = integer_number //10
else: print('No')


'''


'''
Задача 9
Найти максимальную цифру в числе
'''
'''
s = input('Введите натуральное число: ')

while not s.isdigit():
    s = input('Введите натуральное число: ')

s = int(s)

maxNumber = 0
while s > 0:
    if maxNumber < s % 10:
        maxNumber = s % 10
    s //= 10

print('Максимальная цифра:', maxNumber)

'''

'''
Задача 10
Найти количество цифр 5 в числе
'''
'''s = input('Введите положительное число: ')

while float(s) < 0:
    while not s.isdigit():
        print(float(s))
        s = input('Введите положительное число: ')

number = int(s)

yes5 = 0

while number > 0:
    if number % 10  == 5:
        yes5 +=1
    number = number // 10

print('Цифр 5 в числе:', yes5)


'''


