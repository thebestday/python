# ОПРЕРАТОР УСЛОВИЯ
brand = 'Volve' # бренд
engine_volume = 1.5 # обьем двигателя
horsepower = 79 # мощность двигателя
sunroof = False # наличение люка
# Проверка условия if
'''
if horsepower < 80:
    print('No Tax')
'''
# Проверка условия if/else
'''
if horsepower < 80:
    print('No Tax')
    print('No Tax')
    print('No Tax')
else:
    print('Tax')
'''
# компактная запись
# print('No Tax') if horsepower < 80 else print('Tax')
# или так
# if horsepower < 80: print('No Tax')
# else: print('Tax')

# КОНСТРУКЦИЯ if elif else
# tax = 0 #инициализировали переменную tax
# if horsepower < 80:
#     tax = 0
# elif horsepower < 100:
#     tax = 10000
# elif horsepower < 150:
#     tax = 20000
# else:
#     tax = 50000
# print(tax)
#

# Удобная конструкция if для присваивания
# Проверка условия if  для присваивания
cool_car = 0
cool_car = 1 if sunroof == 1 else 0
print(cool_car)