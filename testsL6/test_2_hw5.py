from divisor_master_module import simple
from divisor_master_module import Divs
from divisor_master_module import maxsimple
from divisor_master_module import canon
from divisor_master_module import maxsplit

# тест функции проверки числа на простоту

def test_func_simple():
    assert simple(13) == True
    assert simple(25) == False
    assert simple(33) == False
    assert simple(17) == True
    assert simple('121') == 'Функция принимает на вход числа от 1 до 1000'
    assert simple(1020) == 'Функция принимает на вход числа от 1 до 1000'


# 2
def test_func_Divs():
    n = 10
    out = [1,2,5,10]
    assert Divs(n) == out
    n = 40
    out = [1, 2, 4, 5, 8, 10, 20, 40]
    assert Divs(n) == out
    n = -10
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert Divs(n) == out
    n = -1001
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert Divs(n) == out
    n = 'abc'
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert Divs(n) == out

# 3
def test_func_maxsimple():
    number = 19
    out = 19
    assert maxsimple(number) == out
    number = 555
    out = 37
    assert maxsimple(number) == out
    number = 952
    out = 17
    assert maxsimple(number) == out
    number = 1002
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert maxsimple(number) == out
    number = 'abc'
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert maxsimple(number) == out

 # 4
def test_func_canon():
    x = 888
    out = 'Число:', 888, 'можно разложить так:', ['2^3', '3^1', '37^1']
    assert canon(x) == out
    x = 121
    out = 'Число:', 121, 'можно разложить так:', ['11^2']
    assert canon(x) == out
    x = 952
    out = 'Число:', 952, 'можно разложить так:', ['2^3', '7^1', '17^1']
    assert canon(x) == out
    x = 1022
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert canon(x) == out
    x = -22
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert canon(x) == out


# # 5
def test_func_maxsplit():
    anynumber = 888
    out = [444]
    assert maxsplit(anynumber) == out
    anynumber = 121
    out = [11]
    assert maxsplit(anynumber) == out
    anynumber = 952
    out = [476]
    assert maxsplit(anynumber) == out
    anynumber = 1022
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert maxsplit(anynumber) == out
    anynumber = -22
    out = 'Функция принимает на вход числа от 1 до 1000'
    assert maxsplit(anynumber) == out