class Run:
    def can_run(self):
        return 'I can run'
    def sport(self):
        return 'Run'

class Swim:
    def can_swim(self):
        return 'I can swim'
    def sport(self):
        return 'Swim'

class Ride:
    def can_ride(self):
        return 'I can ride'
    def sport(self):
        return 'Ride'

class Triatlon(Run, Swim, Ride):
    pass

if __name__ == '__main__':
    a = Triatlon()
# isinstance() ялялется ли текущий объект - объектом данного класса?
    print(isinstance(a, Run), isinstance(a, Swim), isinstance(a, Ride), isinstance(a, int))
# проверим есть ли все методы которые мы определили у  объекта а есть
    print(dir(a))
#   проверим что является методом sport у объекта а
# тот который стоит в первом тот и будет при поиске (ПРИ ОБХОДЕ В ШИРИНУ) ЭТО БУДЕТ ПЕРВЫЙ КЛАСС который будет в качестве
# класса поиска метода который не встретился в триатлоне
    print(a.sport())   #  run

# ЕСЛИ СЛОЖНАЯ СТРУКТУРА НАСЛЕДОВАНИЯ ТО КАК В ЦЕЛОМ ОПРЕДЕЛИТЬ?
# ОТ КУДА БУДЕТ - КАК БУДЕТ ОСУЩЕСТВЛЯТЬСЯ ПОИСК (если не хочется разворачивать дерево, обходить граф в ширину)
# можно у класса триалон вызвать методо mro - он выведт то каким образом будет обходится дерево наследования
    print(Triatlon.mro())