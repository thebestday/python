import my_math_module

print(my_math_module.my_add(3,8))

#проверим свойства фибоначи
# (f_n)**2 + (f_(n+1))*2 = f_(2n +1)

n = 10
print(my_math_module.fib_num_1(n)**2 + my_math_module.fib_num_1(n+1)**2)
#10946
print(my_math_module.fib_num_1(2*n + 1))
#10946

print(__name__)
# все что записали в модуле будет скомпилирован и выполнен тот который должен выполниться
# т.е при вызове файла main.py выполниться импорт и все выведется Test Complete!
# что бы это не происходило нужно следующее происать в самом модуле
# if__name == '__main__': и под ним уже код проверочного теста