from divisor_master_module import simple
from divisor_master_module import Divs
from divisor_master_module import maxsimple
from divisor_master_module import canon
from divisor_master_module import maxsplit

# тест функции проверки числа на простоту

def test_func_simple():
    # тест 1 - простое число от 1 до 1000
    n = 193 # True
    out = simple(n)
    if out == True:
        print('Test 1 is OK')
    else:
        print("Test 1 is failed")
    # тест 2 - простое число от 1 до 1000
    n = 19 # True
    out = simple(n)
    if out == True:
        print('Test 2 is OK')
    else:
        print("Test 2 is failed")
    # тест 3 - отрицательное число
    n = -155 # 'Функция принимает на вход целые числа от 1 до 1000'
    out = simple(n)
    if out == 'Функция принимает на вход целые числа от 1 до 1000':
        print('Test 3 is OK')
    else:
        print("Test 3 is failed")
    # тест 4 - отрицательное число
    n = 1.8 # 'Функция принимает на вход целые числа от 1 до 1000'
    out = simple(n)
    if out == 'Функция принимает на вход целые числа от 1 до 1000':
        print('Test 4 is OK')
    else:
        print("Test 4 is failed")
    # тест 5 - отрицательное число
    n = 1005 # 'Функция принимает на вход целые числа от 1 до 1000'
    out = simple(n)
    if out == 'Функция принимает на вход целые числа от 1 до 1000':
        print('Test 5 is OK')
    else:
        print("Test 5 is failed")
test_func_simple()
# # 2
def test_func_Divs():
    # тест 1
    num = 10
    out = Divs(num) # [1,2,5,10]
    if out == [1,2,5,10]:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    num = 40
    out = Divs(num) # [1, 2, 4, 5, 8, 10, 20, 40]
    if out == [1, 2, 4, 5, 8, 10, 20, 40]:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    # тест 3
    num = -10
    out = Divs(num) # 'Функция принимает на вход целые числа'
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')

    # тест 4
    num = -1001
    out = Divs(num) # 'Функция принимает на вход целые числа'
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')

    # тест 5
    n = 'abc'
    out = Divs(num) # 'Функция принимает на вход целые числа'
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')
test_func_Divs()
# 3
def test_func_maxsimple():
    # тест 1
    number = 10
    out = maxsimple(number)
    if out == 5:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    number = 777
    out = maxsimple(number)  #37
    if out == 37:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    # тест 3
    number =  '08984'
    out = maxsimple(number)  #4492
    if out == 4492:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4
    number =  'abc'
    out = maxsimple(number)  #'Функция принимает на вход числа':
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 5
    number =  0.763
    out = maxsimple(number)  #'Функция принимает на вход числа':
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')

# test_func_maxsimple()
# 4
def test_func_canon():
    # тест 1
    x = 888
    out = 'Число:', 888, 'можно разложить так:', ['2^3', '3^1', '37^1']
    if canon(x) == out:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    x = 273801
    out = 'Функция принимает на вход числа от 1 до 1000'
    if canon(x) == out:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    # тест 3
    x = '78393'
    out = 'Функция принимает на вход числа от 1 до 1000'
    if canon(x) == out:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4
    x = 'abc'
    out = 'Функция принимает на вход числа от 1 до 1000'
    if canon(x) == out:
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 5
    x = 0.763
    out = 'Функция принимает на вход числа от 1 до 1000'
    if canon(x) == out:
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')
test_func_canon()
# 5
def test_func_maxsplit():
    # тест 1
    anynumber = 27
    out = maxsplit(anynumber)
    if out == [9]:
        print('Test 1 is Ok')
    else:
        print('Test 1 is failed')
    # тест 2
    anynumber = 1000
    out = maxsplit(anynumber)
    if out == [500]:
        print('Test 2 is Ok')
    else:
        print('Test 2 is failed')
    # тест 3
    anynumber = -193
    out = maxsplit(anynumber)
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 3 is Ok')
    else:
        print('Test 3 is failed')
    # тест 4
    anynumber = 1.8
    out = maxsplit(anynumber)
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 4 is Ok')
    else:
        print('Test 4 is failed')
    # тест 5
    anynumber = 'abc'
    out = maxsplit(anynumber)
    if out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 5 is Ok')
    else:
        print('Test 5 is failed')


test_func_maxsplit()

