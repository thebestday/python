# # Динамическая типизация
# temp_var_1 = input('Input something!')
# print(temp_var_1,type(temp_var_1), id(temp_var_1))
#
# temp_var_2 = input('Input something!')
# print(temp_var_2,type(temp_var_2), id(temp_var_2))
#
# # ИТак у нас две переменные проведем операцию присваивания
# #temp_var_1 = temp_var_2
#
# print(id(temp_var_1), id(temp_var_2))
#
# # Небольшой трюк с присваение типов поменяем тип у второй пременной
# temp_var_1 = int(temp_var_2)
#

# Пример приведения типов
# Попросим ввести иенно число
temp_float = input('Input float number!')
print(temp_float,type(temp_float), id(temp_float))

# if temp_float.isdigit():
#     temp_float= float(temp_float) # приводим к типу float
#     print(temp_float,type(temp_float), id(temp_float))
# else: print(' There is not number')
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


if is_digit(temp_float):
    temp_float = float(temp_float) # приводим к типу float
    print(temp_float, type(temp_float), id(temp_float))
else: print(' There is not number')