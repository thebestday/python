# Перепишем циклы из конструкции while в конструкцию for
# Простейший цикл
# for i in range(10):
#     print(i)

# Конструкция range(start, stop, step)
# взяли все четные числа
# for i in range(0, 10, 2):
#     print(i)
# ДОбавим в цикл проверку условия
# for i in range(10):
#     print(i)
#     if i == 5: break

# Сложный цикл
# for i in range(10):
#     answer = input('Какая лучшая марка автомобиля?')
#     if answer == 'volvo':
#         print('Вы абсолютно правы!')
#         break
# Пример с continue
for i in range(10):
    if i == 8: break
    if i < 3: continue
    else: print(i)