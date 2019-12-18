# Цикл while
# Простейший while
i = 0
while i < 10:
    print(i)
    i = i + 1 # важно добавлять 1 что бы не создать бесконеный цикл
    if i == 5: break

# Более сложный цикл
answer = None

while answer != 'Volvo':
    answer = input('Какая лучшая марка автомобиля?')
print('Вы абсолютно правы!')

# Обсудим операторы ветления continue
while i < 10:
    print(i)
    i = i + 1 # важно добавлять 1 что бы не создать бесконеный цикл
    if i == 9: break
    if i < 3: continue