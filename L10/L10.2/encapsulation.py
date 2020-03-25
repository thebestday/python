import random
# В ЧЕМ У НАС БУДЕТ ЗАКЛЮЧАТЬСЯ ИНКАПСУЛЯЦИЯ?
# мы хотим скрыть параметры self._hidden_num_1 / self._hidden_num_2
# эти параметры компьютер выбирает случайно - пользователю видеть не нужно - поэтому ставим им две земли
class Dice_inc:
    def __init__(self, N):
        self.throw_num = N
        self.current_throw = 0

    def set_hidden_numbers(self):
        self.__hidden_num_1 = random.randint(1,6)
        self.__hidden_num_2 = random.randint(1,6)

# У нас будет еще одна ф-я сменить загаданные числа( будет в автоматическом режиме)

    def change_dices(self):
        self.__hidden_num_1 = random.randint(1,6)
        self.__hidden_num_2 = random.randint(1,6)

# или для тестирования пользователь сам захочет устанавливать эти числа
# вэтом случае нам будет доступно это значение - потому что это внутри класса
# принято через set_ или можно через get_ ( тогда появиться доступ)
# прелесть ручной настройки в том что можно поставить условие( проверку) когда get(там dice не передается)
#     def set_dices1(self, dice):
#         if (dice > 0) & (dice < 7):
#             self.__hidden_num_1 = dice
#         else:
#             raise ValueError('Числа должны быть от 1 до 6 !!!')

    # def get_dices1(self):
    #     #id dice > 0 & dice < 7:
    #     return self.__hidden_num_1
    # создадим декатор для ф-и которая будет возращать это занчение
    # теперь мы можем обращаться к скрытой переменной __hidden_num_1 как к hidden_num_1 (просто без всего)
    # т.е мы обращаемся к фун-и как к атрибуту при этом вызывается функция и возвращает то значение которое оно возвращает
    @property
    def hidden_num_1(self):
        return self.__hidden_num_1

# соответсвенно есть ф-я доступа и есть фун-я настройки
# т.е есть аналог метода set_dice только с помощью декоратора
# так же создаем фун-ю и декаратор с setter (это позволит нам просто через равно обращаться к переменным)
    @hidden_num_1.setter
    def hidden_num_1(self, dice):
        if (dice > 0) & (dice < 7):
            self.__hidden_num_1 = dice
        else:
            raise ValueError('Числа должны быть от 1 до 6 !!!')

    # def set_dices2(self, dice):
    #     self.__hidden_num_2 = dice
    #
    # def get_dices2(self):
    #     #id dice > 0 & dice < 7:
    #     return self.__hidden_num_2

# декаратор он как бы формирует доступ к тому что вы возвращаете в этой фун-и как к переменной
    @property
    def hidden_num_2(self):
        return self.__hidden_num_2

# соответсвенно есть ф-я доступа и есть фун-я настройки
# т.е есть аналог метода set_dice только с помощью декоратора
# так же создаем фун-ю и декаратор с setter
    @hidden_num_2.setter
    def hidden_num_2(self, dice):
        if (dice > 0) & (dice < 7):
            self.__hidden_num_2 = dice
        else:
            raise ValueError('Числа должны быть от 1 до 6 !!!')


    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток')
        if {dice_1,dice_2} == {self.__hidden_num_1, self.__hidden_num_2}:
            return True
        else:
            return False

# ВСЕ что делаете с переменными тоже самое можно делать и с функциями те одна земля - Нежелательно вызывать - две земли только если уверены
# вызов даст ошибку Dice_inc' object has no attribute '__throw_dices'
# но можем посмотреть через метод dir(object) и хотя она будет скрыта (к ней нет доступа) но ее можно будте увидеть но вызвать не можем
# для методов все тоже самое что для переменных но для них доступ тоже можно организовать через функцию (мы можем вернуть фун-ю как объект)
# у методов нет отличий от атрибутов
    def __throw_dices(self):
        pass


if __name__ == '__main__':
    dice_game = Dice_inc(2)
    dice_game.set_hidden_numbers()
    print(dir(dice_game))
    # Dice_inc' object has no attribute '__throw_dices'
    # dice_game.__throw_dices()
    # 'Dice_inc' object has no attribute '__hidden_num_1'
    #  __ две земли перекрывают доступ к этим переменным - ПОЭТОМУ ПОЛЬЗУЕСЯ МЕТОДАМИ get (которые мы написали)
    #print(dice_game.__hidden_num_1, dice_game.__hidden_num_2)
    # print(dice_game.get_dices1(), dice_game.get_dices2())

    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    # dice_game.set_dices1(5)
    dice_game.hidden_num_1 = 5
    # dice_game.set_dices2(4)
    dice_game.hidden_num_2 = 4
    # print(dice_game.get_dices1(), dice_game.get_dices2())
    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    for i in range(4):
        try:
            print(dice_game.throw_dices())
        except:
            print('Игра закончена')