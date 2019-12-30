
import regex as re
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

print('#1) методами строк очистить текст от знаков препинания; ')

text_clear = open("text.txt", encoding='utf-8')
data = text_clear.read()

text_clear.close()
# применим "re" для отделения всех цифр и букв алфавита от остальных знаков
# ключ w это Любая цифра или буква (\W — все, кроме буквы или цифры)
# ключ + это 1 и более вхождений шаблона слева
#d1 = re.sub(r'\w+', "", data)  #  вывели  все знаки препинания

# re.sub(pattern, repl, string) Этот метод ищет шаблон в строке и заменяет его на указанную подстроку
# \P{xx}	a character without the xx property
data1 = re.sub("[^\P{P}]+", "", data)
print(type(data1), data1)
print(len(data1))

print('')
print(("# 2) сформировать list со словами (split);"))
# 2) сформировать list со словами (split);

data2 = data1.split()
print(type(data2), data2)
print(len(data2))

print('')
print('# 3) привести все слова к нижнему регистру (map);')
ls = list(map(lambda x: x.lower(), data2))
print(type(ls), ls)
print(len(ls))

print('')
print('# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
# метод get() возвращает значение для данного ключа, возрвращает 0 если ключ не существует
# Перебор с помощью цикла for: здесь вместо функции range мы сразу можем подставить имеющийся список ls
md = {}
for it in ls:
    i = md.get(it, 0)
    md[it] = i + 1

print(type(md), md)
print(len(md))

# или через count
md2 = {}
for it in ls:
    md2[it] = ls.count(it)

print(type(md2), md2)
print(len(md2))



print('')
print('# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')
# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
ls0 = list(md.items())
ls0.sort(key=lambda i: i[1], reverse=True)
#print(ls0[:])
print(ls0[:5])

print('Вывести количество разных слов в тексте (set)')
setList = set(ls)
print('количество разных слов в тексте: ', len(setList))
print('количество слов в тексте: ', len(ls))

print('')
print('5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.')
# #5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.

morph = pymorphy2.MorphAnalyzer()
print(ls)

# череp map()
normal_list = list(map(lambda x: morph.parse(x)[0].normal_form, ls))
print(normal_list)

# через метод append()
newList = []
for i in ls:
    newList.append(morph.parse(i)[0].normal_form)
print(newList)

