from collections import OrderedDict

ranks_in_order = [
    ('King', 'K'), ('Queen', 'Q'), ('Jack', 'J'), ('Ten', '10'), ('Nine', '9'),
    ('Eight', '8'), ('Seven', '7'), ('Six', '6'), ('Five', '5'), ('Four', '4'),
    ('Three', '3'), ('Two', '2'), ('Ace', 'A')
]

all_ranks = OrderedDict(ranks_in_order)


class Rank:

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __str__(self):
        return self.__class__.__name__


RANKS = {}
for key, element in ranks_in_order:
    RANKS[key] = type(key, (Rank, ), {'symbol': element})

suits_in_order = [
    ('Diamonds','red'), ('Clubs','black'),
    ('Hearts','red'), ('Spades','black')
]

all_suits = OrderedDict(suits_in_order)


class Suit:

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    def __str__(self):
        return "{}".format(self.__class__.__name__)


SUITS = {}
for key, element in all_suits.items():
    SUITS[key] = type(key, (Suit, ), {'color': element})


class Card:

    def __init__(self, rank, suit):
        object.__setattr__(self, 'rank', rank())
        object.__setattr__(self, 'suit', suit())

    def __setattr__(self, index, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class CardCollection:

    def __init__(self, collection=list()):
        self.card_collection = list(collection)

    def __getitem__(self, i):
        return self.card_collection.__getitem__(i)

    def __iter__(self):
        return self.card_collection.__iter__()

    def __len__(self):
        return len(self.card_collection)

    def __str__(self, index):
        return "Card {}".format(self.card_collection[index])

    def add(self, card):
        self.card_collection.append(card)

    def draw(self, index):
        return self.card_collection.pop(index)

    def draw_from_top(self):
        return self.card_collection.pop()

    def draw_from_bottom(self):
        return self.card_collection.pop(0)

    def top_card(self):
        return self.card_collection[len(self.card_collection) - 1]

    def bottom_card(self):
        return self.card_collection[0]

    def index(self, card):
        for index in range(len(self.card_collection)):
            if self.card_collection[index].rank == card.rank \
            and self.card_collection[index].suit == card.suit:
                return index
        raise ValueError("{} is not in list".format(card))


def StandardDeck():
    standart_deck = []
    for one_suit in all_suits:
        for one_rank in all_ranks:
            standart_deck.append(Card(RANKS[one_rank], SUITS[one_suit]))
    return CardCollection(standart_deck)


def BeloteDeck():
    belot_deck = []
    for one_suit in all_suits:
        for one_rank in range(0, 7):
            belot_deck.append(Card(RANKS[ranks_in_order[one_rank][0]],
                SUITS[one_suit]))

        belot_deck.append(Card(RANKS[ranks_in_order[-1][0]],
            SUITS[one_suit]))
    return CardCollection(belot_deck)


def SixtySixDeck():
    sixtysix_deck = []
    for one_suit in all_suits:
        for one_rank in range(0, 5):
            sixtysix_deck.append(Card(RANKS[ranks_in_order[one_rank][0]], SUITS[one_suit]))
        sixtysix_deck.append(Card(RANKS[ranks_in_order[-1][0]],
            SUITS[one_suit]))
    return CardCollection(sixtysix_deck)