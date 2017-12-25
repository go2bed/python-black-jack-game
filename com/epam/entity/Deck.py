import random

from com.epam.entity.Card import Card


class Deck:
    def __init__(self):
        '''Create a deck in order'''
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        '''Shuffle the deck, python actually already has a shuffle
          method on its random lib'''
        random.shuffle(self.deck)

    def deal(self):
        '''Grab the first item in the deck'''
        single_card = self.deck.pop()
        return single_card


suits = ('H', 'D', 'C', 'S')

ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

