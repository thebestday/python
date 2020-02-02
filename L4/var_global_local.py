# global служебное слово
global_var = 10
def function_example(local_var_1, local_var_2):
    print(local_var_1,local_var_2, global_var)

function_example(11, 12)
# теперь попробуем изменить значение глобальной переменной

def function_example(local_var_1, local_var_2):
    global global_var
    global_var = 20
    print(local_var_1,local_var_2, id(global_var))
function_example(11, 12)
print(id(global_var)) # но видим что  глобальная пременная не изменлась и переменнаые ссылаются на разные участки памяти
# т.е  совершенно разные переменные хотя и называются одинаково
# все что создается  внутри не можте быть глобальной перменной , а = это фактически создание новой переменной
# что бы реально поменять значения нужно использовать служебнос слово global
# обяьвим что в функции что следующая переменная будет глобальной global global_var
# id показывают одно значение

#  nonlocal ключевое слово
# можно добавлять переопределение области во внутренней области
def counter():
    num = 0
    def plus_one():
        nonlocal num
        num += 1
        return num
    return plus_one

c = counter()
print(c)
c()  # local variable 'num' referenced before assignment
print(c())
print(c())