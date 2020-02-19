
# 1 - 1
import math

def simple(n):
    if type(n) == int and n >= 1 and n <= 1000 :
        i = 2
        limit = int(math.sqrt(n))
        while i <= limit:
            if n % i == 0:
                return False
                quit()
            i += 1
        return True
    else:
        return 'Функция принимает на вход числа от 1 до 1000'
# print(simple(n))

# 1 - 2

# n = int(input())
#
# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

# print(IsPrime(n), type(IsPrime(n)))
# if IsPrime(n):
#     print(n, '- это простое число')
# else:
#     print(n, '- это составное число')

# 2 -1
#
# d = int(input())
#
# from itertools import chain
# divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0))
#
# print(list(divs(d)))
# print(max(list(divs(d))))
# print('-----------')

# 2-2


# num = int(input())

def Divs(num):
    if type(num) == int and num >= 1 and num <= 1000:
        a = []
        for i in range(1, num + 1):
            if num % i == 0:
                a.append(i)
        return a
    else:
        return 'Функция принимает на вход числа от 1 до 1000'
# print(Divs(num))

# 3




def maxsimple(number):
    if type(number) == int and number >= 1 and number <= 1000:
        l = Divs(number)
        w = []
        for el in l:
            if simple(el):
                w.append(el)
        # print(w)
        return max(w)
    else:
        return 'Функция принимает на вход числа от 1 до 1000'



# 4

def canon(x):
    if type(x) == int and x >= 1 and x <= 1000:
        number = x
        split = []
        order = {}
        Canonical = []
        i = 1
        z = 0
        if x == 1:
            return ('Число:', number, 'можно разложить следующим образом: [1^1]')
        else:
            while i <= x:
                i = i + 1
                if x % i == 0:
                    split.append(i)
                    x = x / i
                    i = 1
            for k in split:
                if k in order:
                    order[k] += 1
                else:
                    order[k] = 1
            for key, value in order.items():
                Canonical.append(str(key) + '^' + str(value))
            return ('Число:', number, 'можно разложить так:', Canonical)
    else:
        return ('Функция принимает на вход числа от 1 до 1000')

# 5



def maxsplit(anynumber):
    if type(anynumber) == int and anynumber >= 1 and anynumber <= 1000:
        m = Divs(anynumber)
        return m[-2:-1]
    else:
        return ('Функция принимает на вход числа от 1 до 1000')