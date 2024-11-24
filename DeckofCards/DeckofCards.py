#// Name: Marcus Bracken
#// Course: CIS261 Object Oriented Computer Programming I
#// Lab: DeckofCards


import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)
        print("I have shuffled a deck of 52 cards.")

    def deal(self, number_of_cards):
        if number_of_cards > len(self.cards):
            print("Not enough cards left in the deck!")
            return []
        dealt_cards = self.cards[:number_of_cards]
        self.cards = self.cards[number_of_cards:]
        return dealt_cards

    def count(self):
        return len(self.cards)


def main():
    print("Card Dealer")
    deck = Deck()
    deck.shuffle()

    while True:
        try:
            num_cards = int(input("How many cards would you like?: "))
            if num_cards <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        dealt_cards = deck.deal(num_cards)
        if not dealt_cards:
            continue

        print("\nHere are your cards:")
        for card in dealt_cards:
            print(card)

        print(f"\nThere are {deck.count()} cards left in the deck.")

        if deck.count() == 0:
            print("The deck is empty. Thanks for playing!")
            break

        print("\nGood luck!")
        break


if __name__ == "__main__":
    main()

