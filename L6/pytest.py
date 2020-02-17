# Полуавтоматические тесты
def test_function(list_in):
    ...
    # вход лист с числами и строкама
    # выход лист с числами
    ...
    list_temp = []
    # i = 0
    # while (type(list_in[i]) == int):
    for i in range(len(list_in)):
        if type(list_in[i])== int:
            list_temp.append(list_in[i])
        elif type(list_in[i]) == str:
            if list_in[i].isdigit(): list_temp.append(int(list_in[i]))
        # i += 1
    return  list_temp
#
# list_temp = [1,2,3,'abc']
#
# print(test_function(list_temp))

# теперь пишем полуавтоматическую фун-ю
def function_test():
    list_temp = [1,2,3,'abc']
    list_out = test_function(list_temp)
    if list_out == [1,2,3]:
        print('TEST 1 IS OK')
    else:
        print('TEST 1 IS FAILED')
    list_temp = [1, 2, 3, 'abc', 4]
    list_out = test_function(list_temp)
    if list_out == [1, 2,3,4]:
        print('TEST 2 IS OK')
    else:
        print('TEST 2 IS FAILED')
    list_temp = [1, 2, 3,'5', 'abc', 4]
    list_out = test_function(list_temp)
    if list_out == [1, 2, 3, 5, 4]:
        print('TEST 3 IS OK')
    else:
        print('TEST 3 IS FAILED')


function_test()
list_temp = [1, 2, 3,'5', 'abc', 4]
list_out = test_function(list_temp)
print(list_out)

