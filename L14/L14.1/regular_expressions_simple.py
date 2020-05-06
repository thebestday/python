import re

string = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'
pattern = r'It'
# findall  найти все вхождения
print(len(re.findall(pattern, string)))
# Мы искали слова но как правило при использовании РЕ требуется более точная настройка - один из базовах элементов это квадратные скобки []
# [ ]
# попробуем найти сколь раз встречалась буква - создаем новый шаблон и указываем что хотим искат только буквы a b c указываем из без запятой подряд
pattern = r'[abc]'
print(re.findall(pattern, string))                # вернет все вхождения букв  abc
print(len(re.findall(pattern, string)))
# хотим найти только одну букву а
pattern = r'[a]'
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))

# нАЙТИ ВСЕ БУКВЫ a-z A-Z 0-9
pattern = r'[a-zA-Z0-9]'
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))

# шаблон для подсчета количества зааятых или точек
pattern = r'[.]'
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))

# Знак точка - это любой символ кроме новый строки
# (.)--------------------------------------------
# например найдем слово которое начинается с буквы w и в нем три буквы -т.е два произвольных симовола после буквы w , пробел тоже считается как символ
pattern = r'[w]..'
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))

# ПОИСК СПЕЦИАЛЬНЫХ СИМВОЛОВ
# \w все кроме специальных знаков (любая буква цифоа)
# \W противоположное тому что с маленькой буквы(есть такое правило в РЕ) -отрицание того что означает маленькая буква - ВСЕ СПЕЦЗНАКИ
pattern = r'\W'
print(re.findall(pattern, string))                # ВСЕ ЗАПЯТЫЕ И ПРОБЕЛЫ И ТОЧКИ -ВООБЩЕМ ВСЕ ЗНАКИ ПРЕПИНАНИЯ(тире , дефисы, и так далее )
print(len(re.findall(pattern, string)))
# \d digit любая цифра ( не число)
# \D все кроме цифры -не цифра
pattern = r'\D'
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))         # ВООБЩЕ ВЕСЬ текст

# ДЛЯ ПОИСКА ТЕЛЕФОНА полезно знать количество которое мы ищем
# Для этого используется следующии мехонизмы
# ПОИСК ОПРЕДЕЛЕННОГО КОЛИЧЕСТВА ЗАДАННЫХ СИМВОЛОВ
# Указываем символ который хотим- например цифру - а потом в фигурных скобках указываем сколько раз мы хотим ее найти
# например \d{n}  - количество цифр n раз  - РОВНО n раз
# \d{n,}          - можно столько раз но можно и больше - БОЛЕЕ n раз
# \d{n,m}         - диапазон  НЕ МЕНЕЕ n ЦИФР НО НЕ БОЛЕЕ m
pattern = r'\W[a-zA-Z]{2}\W'               # ПОЛУЧИЛИ ВСЕ СЛОВА ДЛИНОЙ ДВА  ( не буква спреди и конце \W)
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))
pattern = r'\W\w{2}\W'                      # ПОЛУЧИЛИ ВСЕ СЛОВА ДЛИНОЙ ДВА  ( не буква спреди и конце \W)
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))
# если хотим слова длиной 2-4
pattern = r'\W\w{2,4}\W'                     # поиск слов указанной длины
print(re.findall(pattern, string))
print(len(re.findall(pattern, string)))

# МЫ ИСПОЛЬЗОВАИЛИ МЕТОД findall КОТОРЫЙ НАХОДИТ ВСЕ ПОДСТРОКИ В ДАННОЙ СТРОКЕ
# полезный методы:
# search
pattern = r'\W\w{2,4}\W'                     # поиск слов указанной длины
print(re.search(pattern, string))           # ВОЗВРАЩАЕТ ПЕРВОЕ ВХОЖДЕНИЕ ПАТЕРНА В СТРОКУ и его позицию ( который имеет атрибуты и  к нему можно обратиться)

# sub ----------------------- ЗАМЕНА( ЧАСТО ИСПОЛЬЗУЕТСЯ ДЛЯ ОЧИСТКИ ТЕКСТОВ от ненужных символов)
# sub имеет еще один праметр - то что на что менеяем
pattern = r'\W\w{2,4}\W'                     # поиск слов указанной длины
print(re.sub(pattern,r"***", string))        # поменяли все 2--4  длиной на звездочки
# ДЛЯ ОЧИСТКИ ТЕКСТА МЕНЯЕМ НА ПРОБЕЛЫ
pattern = r'\W\w{2,4}\W'                     # поиск слов указанной длины
print(re.sub(pattern,r' ', string))          # УДАЛИЛИ СЛОВА ДЛИНОЙ 2-4
print(len(re.findall(pattern, string)))






