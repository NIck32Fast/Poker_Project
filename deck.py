import random
class PlayingCard:
    SUITS = ("♣", "♦", "♥", "♠")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    def __init__(self, suit, rank):
       # check if the suit and rank are ok
        if suit not in self.SUITS:
            raise ValueError(f"suit must be in {self.SUITS}")
        if rank not in self.RANKS:
            raise ValueError(f"rank must be in {self.RANKS}")
        self._suit = suit
        self._rank = rank
    @property
    def suit(self):
        return self._suit
    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}" #so i can print the card
    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self._cards = []
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                self._cards.append(PlayingCard(suit, rank))
    @property
    def cards(self):
        return self._cards[:]
    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop(0)

if __name__ == "__main__":
    # card = PlayingCard("♦", "7")
    print(card)
    # card.rank = "A" # cheater, we dont like cheaters
    # print(card)
    deck = Deck()
    print(deck)
    # deck.cards.append(card)
    # print(deck)
    deck.shuffle()
    print(deck)
    card = deck.deal()
    print(card)
    print(deck)
