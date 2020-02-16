# try:
#     исполняем какой-то код
# except Exception as e:
#     обработка исключения
# else:
#     код, который будет исполнен в случае, когда не возникает исключения
# finally:
#     код, который гарантированно будет исполнен последним (всегда исполняется)


# Деление на ноль(обработаем это исключение методом try except
# try:
#     a = int(input('Введите первое число'))
#     b = int(input('Введите второе число'))
#     print(a / b)
# except ZeroDivisionError as e:
#     print('ТАК Нельзя:',e)
# else:
#     print('все хорошо')
# finally:
#     print('Это было не просто')

# '-------------'
# СЧИТАЕМ ЧИСЛА ИЗ ФАЙЛА data.py / метод open
f = open('data.py')
int_arr_list = []
# отркываем цикл по строкам в этом файле
try:
    for line in f:
        int_arr_list.append(int(line))
    print(int_arr_list)
except ValueError:
    print('Я нашел не число')
else:
    print('Все прошло хорошо')
finally:
    f.close()

print(int_arr_list) # прочитал все до ошибки