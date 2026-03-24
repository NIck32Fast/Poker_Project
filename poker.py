from deck import Deck

class PokerHand:
    def __init__(self):
        """
        Create a new deck shuffle and deal 5 cards
        """
        deck = Deck()
        deck.shuffle()
        self._cards = []
        for _ in range(5): #deal 5 cards
            self._cards.append(deck.deal())

    @property
    def cards(self):
        return tuple(self._cards)

    def __str__(self):
        return str(self.cards)

hand = PokerHand()
print(hand)