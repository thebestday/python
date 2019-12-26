# Инициализация () круглыми скобками
temp_tuple = (1,2,3)
print(type(temp_tuple), temp_tuple)

# или с помощью уже созданного list-а через преобразование типов
tempo_list = [4,55,7]
tempo_tuple = tuple(tempo_list)
print(type(tempo_tuple), tempo_tuple)


# Обращение и элементам  кортежа как в списках
print(temp_tuple[0])

for i in range(len(temp_tuple)):
    print(temp_tuple[i])

# Кортеж не дате поменять значение элемнет - выдает ошибку TypeError: 'tuple' object does not support item assignment
# операция присваивания не доступна
#temp_tuple[0] = 100  # выдает ошибку                6-38

# Функции с кортежами
# все как в списках

# Операции с кортежами
# все как в списках

# Методы
# все как в списках

# ПАМЯТЬ - ОТМЕТИМ ЧТО требуется меньше памяти чем при хранении аналогичного объекта в просто list
temp_list = [1,2,3]
temp_tuple = (1,2,3)
# ПОСМОТРИМ СКОЛЬКО ПАМЯТИ ТРЕБУЕТСЯ с помощью атрибута  __sizeof__()
print(temp_list.__sizeof__())
print(temp_tuple.__sizeof__())
