# -*- coding: utf-8 -*-
"""
poker hand imit
"""

from functools import total_ordering
from collections import Counter

SUITS = ("C", "D", "H", "S")
VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
HANDS = ("High Card", "Pair", "Two Pairs", "Three of a Kind",
         "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush",
         "Royal Flush")


@total_ordering
class Card:
    """
    card present
    """
    def __init__(self, value, suit):
        assert suit in SUITS, suit
        assert value in VALUES, value
        self.suit = suit
        self.value = value

    @classmethod
    def from_string(cls, strc):
        """
        from string
        """
        return cls(strc[:-1], strc[-1])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{}{}".format(self.value, self.suit)

    def __eq__(self, other):
        return self.value.__eq__(other.value)

    def __lt__(self, other):
        return VALUES.index(self.value) < VALUES.index(other.value)

    def __int__(self):
        return VALUES.index(self.value)



class PokerHand:
    """PokerHand class"""
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.cards = list(map(Card.from_string, args))
        else:
            self.cards = list(map(Card, args))

    @classmethod
    def from_string(cls, string):
        return cls(*string.split(' '))

    def __str__(self):
        return " ".join(map(str, self.cards))

    def is_flush(self):
        return len({card.suit for card in self.cards}) == 1

    def is_straight(self):
        mc = min(self.cards)
        mxc = max(self.cards)
        if int(mc) == 0 and int(mxc) == 12:
            sm_cards = self.cards[::]
            sm_cards.remove(mc)
            sm_cards.remove(mxc)
            return PokerHand(*map(str, sm_cards)).is_straight()
        l1 = list(sorted(map(int, self.cards)))
        l2 = list(range(int(mc), int(mxc)+1))
        return l1 == l2

    def counts(self):
        c = Counter(card.value for card in self.cards)
        cv = Counter(c.values())
        return  cv[2], cv[3], cv[4]

    def classif(self):
        c2, c3, c4 = self.counts()
        flush = self.is_flush()
        straight = self.is_straight()
        hc = max(self.cards)
        lc = min(self.cards)
        if hc.value == "A" and lc.value == '10' and straight and flush:
            return HANDS[-1]
        elif straight and flush:
            return HANDS[-2]
        elif c4:
            return HANDS[-3]
        elif c2 and c3:
            return HANDS[-4]
        elif flush:
            return HANDS[-5]
        elif straight:
            return HANDS[-6]
        elif c3:
            return HANDS[-7]
        elif c2 == 2:
            return HANDS[-8]
        elif c2 == 1:
            return HANDS[-9]
        else:
            return HANDS[0]



if __name__ == '__main__':

    """
    with open('poker_test', 'r') as tf:
        for rawline in tf:
            rawline = rawline.strip()
            inp, ans = rawline.split(" _ ")
            my_ans  = PokerHand.from_string(inp).classif()
            print(inp, ans, my_ans)
    """
    ph = PokerHand.from_string(input())
    print(ph.classif())

