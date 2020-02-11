print("модуль принимают на вход натуральные числа от 1 до 1000")
# 1 - 1
import math

def simple(n):
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            return False
            quit()
        i += 1
    return True

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
    a = []
    for i in range(1, num + 1):
        if num % i == 0:
            a.append(i)
    return a

# print(Divs(num))

# 3




def maxsimple(number):
    l = Divs(number)
    w = []
    for el in l:
        if simple(el):
            w.append(el)
    # print(w)
    return max(w)


# print(maxsimple(55))

# 4

def canon(x):
    number = x
    split = []
    order = {}
    Canonical = []
    i = 1
    z = 0
    if x == 1:
        return print('Число:', number, 'можно разложить следующим образом: [1^1]')
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
        return print('Число:', number, 'можно разложить так:', Canonical)

# 5



def maxsplit(anynumber):
    m = Divs(anynumber)
    print(m)
    return m[-2:-1]
