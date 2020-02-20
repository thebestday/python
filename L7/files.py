...
#Работа с текстовыми файлами
...

# обычное проесто считывание - открытие файла в режиме чтения
# f = open('data')
# content = f.read()
# print(content)
# f.close()
#
# # метод построчного считывания файла в цикле
# f = open('data')
# for line in f:
#     print(line)
# f.close()

# менеджер контекста
# with open('data') as f:
#     for line in f:
#         print(line)

#print(''''''''''''''''Запись в файл - создаст новый файл data_new и запишет туда фразу This is new file!   ''''')
# with open('data_new', 'w') as f:
#     f.write('This is new file!')
#

 # можно писать построчно
 # создадим список но к каждому эелменту добавляем \n если без то выведет одной строкой
data = ['1\n', '2\n', '3\n']

with open('data_new', 'w') as f:
    f.writelines(data)

# считыаение ОДНОЙ СТРОКИ line = f.readline()
with open('data') as f:
    line = f.readline()
    print(line) #123

#  считываение побайтно в режие 'r' или еще реже в режиме 'rb'

with open('data', 'r') as f:
    data = f.read(10)            # количество байтов которые хотим считать
    print(data)                  # 123
                                 # Hello