def my_add(x, y):
    return x + y

def my_sub(x, y):
    return x - y

def my_mul(x, y):
    return x* y

def my_div(x, y):
    return x / y
# fibo number
# 1, 1, 2, 3, 5, 8, 13 ....
def fib_num(n):
    if n == 1: return 1
    elif n == 2: return 1
    else: return fib_num(n-1) + fib_num(n-2)

# print(fib_num(7))

# lambda
fib_num_1 = lambda n: fib_num_1(n-1) + fib_num_1(n-2) if n > 2 else 1
# print(fib_num_1(8))

# в самом модуле напишем код для исполнения- как будьто он проверочный
# проверим свой-во фибоначи

print(__name__)
if __name__ == '__main__':
    n = 10
    if(fib_num_1(n)**2 + fib_num_1(n+1)**2) == fib_num_1(2*n + 1):
        print('Test Complete!')
    else:
        print("Test failed!")
