import pytest
from encapsulation import Dice_inc

class TestDice_pytest:
    def setup(self):
        self.dice_game = Dice_inc(3)
        print('Start test!')

    def teardown(self):
        self.dice_game.current_throw = 0
        print('Test has done')
# тестируем ф-ю __init__
# создаем объект
    def test_init(self):
        assert self.dice_game.throw_num == 3
        assert self.dice_game.current_throw == 0
    # тестируем setter
    def test_dice_setter(self):
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        assert (self.dice_game.hidden_num_1 == 5) & (self.dice_game.hidden_num_2 == 5)
            # МОЖНО ЛОВИТЬ КОНКРЕТНУЮ ОШИБКУ (похож на менеджер контекста)
            # протестируем фун-ю присваивания которую написали с помощью setter

        with pytest.raises(ValueError):
            # КОд вызывающий данную ошибку
            self.dice_game.hidden_num_1 = 8

# ПРОтестируем функ-ю throw_dices
    def test_throw_dices(self):
        self.dice_game.set_hidden_numbers()
        self.dice_game.throw_dices()
        assert self.dice_game.current_throw == 1
