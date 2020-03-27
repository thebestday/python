import unittest
from module import Deck

class TestDeck_unittest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        print('Test done!!!')
        # обычно происходит освобождение кеша
        del self.deck

    def test_init(self):
        self.assertEqual(len(self.deck.ranks), 9)
        self.assertFalse(len(self.deck.ranks) > 10)

    def test_deck(self):
        self.assertEqual(len(self.deck._cards),36)

    def test_suits(self):
        self.assertEqual(len(self.deck.suits), 4)

    def test_list_card(self):
        self.deck.mix_cards()
        self.deck.list_card()
        self.assertEqual(len(self.deck.list_num_card), 36)

    def test_player_hand(self):
        self.deck.mix_cards()
        self.deck.list_card()
        self.deck.player_card()
        self.deck.player_hand()
        self.assertEqual(len(self.deck.cards_pl), 6)