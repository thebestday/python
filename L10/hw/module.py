import random

class Deck:
    ranks = [str(n) for n in range(6, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def mix_cards(self):
        mix =  random.shuffle(deck._cards)
        return mix

    def allranks(self, x):
        if x == '6' : return 6
        if x == '7' : return 7
        if x == '8' : return 8
        if x == '9' : return 9
        if x == '10': return 10
        if x == 'J' : return 11
        if x == 'Q' : return 12
        if x == 'K' : return 13
        if x == 'A' : return 14

    def list_card(self):
        self.list_num_card = [int(i) for i in range(0, 36)]
        # print(deck._cards)
        # print('list_num_card', self.list_num_card)
        # for i in self.list_num_card:
        #     print('КАРТа после ПЕРЕМЕШИВАНИЯ', deck._cards[i], self.list_num_card[i])
        # print(deck.list_num_card)
        return self.list_num_card


    def player_card(self):
        # лучше self.list_num_card чем deck.list_card()
        self.pl_c = random.choice(self.list_card())
        return self.pl_c

    # Раздача игроку
    def player_hand(self):
        self.cards_pl = []
        card_pl_number = []
        while len(self.cards_pl) <= 5:
            a = deck.player_card()
            card_pl_number.append(a)
            self.cards_pl.append(deck[a])
            self.list_num_card.remove(a)
        # print('карты игрока cards_pl', self.cards_pl, card_pl_number)


    def computer_hand(self):
        self.cards_comp = []
        cards_comp_number = []
        while len(self.cards_comp) <= 5:
            b = deck.player_card()
            cards_comp_number.append(b)
            self.cards_comp.append(deck[b])
            self.list_num_card.remove(b)
        # print('карты компа cards_comp', self.cards_comp, cards_comp_number)
        # print("---cards_comp_number--", cards_comp_number, type(cards_comp_number))

    def coloda(self):
        # print(self.list_num_card)
        self.coloda_after = []
        for i in range(len(self.list_num_card)):
            # print(i,  deck[list_num_card[i]] )
            self.coloda_after.append(self.list_num_card[i])
        # print(len(deck.coloda_after))
        # print('--Цифры которые были раньше(после перемешивания) для каждой карты после раздачи', self.coloda_after)

    def check_cards(self):
        # for i in range(len(self.coloda_after)):
        #     print(i, deck._cards[i], deck.list_num_card[i])
        if self.cards_pl not in self.coloda_after:
            print('Совпадений не обнаружено')
        if self.cards_comp not in self.coloda_after:
            print('Совпадений не обнаружено')
        if self.cards_pl not in self.cards_comp:
            print('Раздача карт- все верно!!!')

    def turn(self):
        print('Ваши карты:\n{}'.format(self.cards_pl))
        self.player_cards = []
        self.player_hand_len = []
        for i in range(len(self.cards_pl)):  # выводим для удобства цифры (сколько карт в рукаве) для пользователя
            self.player_hand_len.append(i)
        self.player_choice = int(input('Введите карту, которой желаете пойти: {}'.format(self.player_hand_len)))
        self.player_cards.append(self.cards_pl[self.player_choice])
        self.cards_pl.remove(self.cards_pl[self.player_choice])
        print('Вы выбрали карту:\n{}'.format(self.player_cards ))
    def computer_answer(self):
        print('Карты компрьютера:\n{}'.format(self.cards_comp))
        self.answer_cards = []
        for card in self.cards_comp:
            if card[1] == self.player_cards[0][1]:
                if deck.allranks(card[0]) > deck.allranks(self.player_cards[0][0]):
                    self.answer_cards.append(card)

        # print('--self.answer_cards---', self.answer_cards)

        # print(len(self.answer_cards))
        if len(self.answer_cards) == 1:
            self.computer_move = self.answer_cards[0]
            self.cards_comp.remove(self.computer_move)
            print('Компьютер бьет Вашу карту картой {}.'.format(self.computer_move))

        if len(self.answer_cards) > 1:
            newl = []
            for i in range(1, len(self.answer_cards)):
                # print(self.answer_cards[i])
                if deck.allranks(self.answer_cards[i][0]) < deck.allranks(self.answer_cards[i-1][0]):
                    # newl.append(deck.allranks(self.answer_cards[i][0]))
                    newl.append(self.answer_cards[i])
                else:
                    newl.append(self.answer_cards[i-1])
            # print("--newl--************************************************************", newl, type(newl))
            # print(len(newl))
            if len(newl) >=2:
                if  deck.allranks(newl[0][0]) > deck.allranks(newl[1][0]):
                    newl.reverse()

            # print("--newl--************************************************************", newl, type(newl))

            self.computer_move = newl[0]
            # self.computer_move = self.answer_cards[0]
            self.cards_comp.remove(self.computer_move)
            print('Компьютер бьет Вашу карту картой {}.'.format(self.computer_move))

        if len(self.answer_cards) == 0:
            print('Компьютер берет.')
            self.cards_comp.append(self.player_cards)


deck = Deck()
# deck.mix_cards()

if __name__ == "__main__":
    deck = Deck()
    deck.mix_cards()
    deck.list_card()
    deck.player_card()
    deck.player_hand()
    deck.computer_hand()
    deck.coloda()
    deck.check_cards()
    deck.turn()
    deck.computer_answer()