from itertools import count

from deck import Deck, PlayingCard


class PokerHand:
    def __init__(self):
        """
        Create a brand-new Deck, shuffle it and deal 5 cards!
        """
        deck = Deck()  # Create a new deck
        deck.shuffle()  # Shuffle the deck
        self._cards = []  # Create an empty hand
        for _ in range(5):  # We deal 5 cards!
            self._cards.append(deck.deal())  # Add a card to the hand, until 5

    @property
    def cards(self):
        return tuple(self._cards)

    @property
    def is_flush(self):
        """
        Check if the hand is a flush
        :return: True or False
        """
        for card in self._cards[1:]:
            if self._cards[0].suit != card.suit:
                return False
        if self.is_straight:
            return False
        return True

    @property
    def is_straight_flush(self):
        return self.is_flush and self.is_straight

    @property
    def is_normal_flush(self):
        return self.is_flush and not self.is_straight

    @property
    def num_matches(self):
        count = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self._cards[i].rank == self._cards[j].rank:
                    count += 1
        return count

    @property
    def is_pair(self):
        return self.num_matches == 2

    @property
    def is_2_pair(self):
        return self.num_matches == 4

    @property
    def is_trips(self):
        return self.num_matches == 6

    @property
    def is_full_house(self):
        return self.num_matches == 8

    @property
    def is_4_kind(self):
        return self.num_matches == 12

    @property
    def is_straight(self):
        if self.num_matches != 0:
            return False
        cards = list(self._cards)
        cards.sort(key=lambda card: PlayingCard.RANKS.index(card.rank))
        first_card_index = PlayingCard.RANKS.index(cards[0].rank)
        last_card_index = PlayingCard.RANKS.index(cards[-1].rank)
        if first_card_index + 4 == last_card_index:
            return True
        # Bicycle
        if cards[-1].rank == "A" and cards[-2].rank == "5":
            return True
        return False

    def __str__(self):
        return str(self.cards)


tries = 0
total_hits = 1000
hits = 0
while True:
    hand = PokerHand()
    tries += 1
    if hand.is_flush:
        hits = hits + 1
    if hits == total_hits:
        print(f"probability of a flush is {hits / tries * 100}%")
        break

tries = 0
total_hits = 500
hits = 0
while True:
    hand = PokerHand()
    tries += 1
    if hand.is_full_house:
        hits = hits + 1
    if hits == total_hits:
        print(f"probability of a full house is {hits / tries * 100}%")
        break

tries = 0
total_hits = 100
hits = 0
while True:
    hand = PokerHand()
    tries += 1
    if hand.is_straight:
        hits = hits + 1
    if hits == total_hits:
        print(f"probability of a straight is {hits / tries * 100}%")
        break

tries = 0
total_hits = 25
hits = 0
while True:
    hand = PokerHand()
    tries += 1
    if hand.is_straight_flush:
        hits = hits + 1
    if hits == total_hits:
        print(f"probability of a straight flush is {hits / tries * 100}%")
        break

hand = PokerHand()
print(hand)
