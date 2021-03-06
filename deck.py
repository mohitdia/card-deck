#!/usr/bin/python
"""
This module defines the structure of a Deck class which includes method to
initialize a deck of cards, shuffle the deck and a method to deal a card from
the deck.
"""

import random
from card import Card, CARD_VALUES, CARD_TYPES

class Deck(object):
    """
    Deck of cards
    """
    def __init__(self):
        self.deck = self.create_deck()

    @staticmethod
    def create_deck():
        """
        Creates the deck of cards using the Card class.
        @return List of card objects
        """
        deck = []
        for card_type in CARD_TYPES:
            for card_val in CARD_VALUES:
                card = Card(card_val, card_type)
                deck.append(card)
        return deck

    def list_deck_of_cards(self):
        """
        Prints the cards in the current deck
        """
        for card in self.deck:
            print(card)

    def shuffle(self):
        """
        Shuffles the deck of cards which returns a new set of deck of cards.
        @return List of shuffled card objects
        """
        index_choices = list(range(len(self.deck)))
        new_deck = []
        for card in self.deck:
            random_index = random.choice(index_choices)
            new_deck.append(self.deck[random_index])
            index_choices.remove(random_index)
        self.deck = new_deck

    def deal_one_card(self):
        """
        Returns a card if the deck is not empty
        @return Card object
        """
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return 'Deck is empty'
