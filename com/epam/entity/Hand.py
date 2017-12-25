# Boolean used to know if hand is in play
playing = False

chip_pool = 100  # Could also make this a raw input.

bet = 1

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can be 1 or 11 so need to define it there
        self.ace = False

    def __str__(self):
        '''Return a string of current hand composition'''
        hand_comp = ""

        # Better way to do this? List comprehension?
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The hand has %s' % hand_comp

    def card__add(self, card):
        self.cards.append(card)

        # Check for aces
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        '''Calculate the value of the hand, make acs an 11 if
        they don't bust the hand'''
        if self.ace == True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0

        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
