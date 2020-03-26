
import pytest
import module

def test_deck():
    deck = module.Deck()
    assert len(deck._cards) == 36

def test_suits():
    deck = module.Deck()
    assert len(deck.suits) == 4

def test_list_card():
    deck = module.Deck()
    deck.mix_cards()
    deck.list_card()
    assert len(deck.list_num_card) == 36

def test_player_hand():
    deck = module.Deck()
    deck.mix_cards()
    deck.list_card()
    deck.player_card()
    deck.player_hand()
    assert len(deck.cards_pl) == 6

# def test_computer_hand():
#     deck = module.Deck()
#     deck.mix_cards()
#     deck.list_card()
#     deck.player_card()
#     deck.player_hand()
#     deck.computer_hand()
#     assert len(deck.cards_comp) == 6

# def test_coloda():
#     deck = module.Deck()
#     deck.mix_cards()
#     deck.list_card()
#     deck.player_card()
#     deck.player_hand()
#     deck.computer_hand()
#     deck.coloda()

#     assert len(deck.coloda_after) == 24