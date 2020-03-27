import pytest
from module import Deck

class TestDeck_pytest:

    def setup(self):
        self.deck = Deck()

    def teardown(self):
        print('Test has done')

    def test_init(self):
        assert len(self.deck.ranks) == 9

    def test_deck(self):
        assert len(self.deck._cards) == 36

    def test_suits(self):
        assert len(self.deck.suits) == 4

    def test_list_card(self):
        self.deck.mix_cards()
        self.deck.list_card()
        assert len(self.deck.list_num_card) == 36

    def test_player_hand(self):
        self.deck.mix_cards()
        self.deck.list_card()
        self.deck.player_card()
        self.deck.player_hand()
        assert len(self.deck.cards_pl) == 6


