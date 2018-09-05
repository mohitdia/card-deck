#!/usr/bin/python
"""
This module defines the structure of a Card class
to be used in a deck.
"""

CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
CARD_TYPES = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
INVALID_CARD_VALUE_MESSAGE = 'Invalid card value supplied. Should be between 2-10, Ace, King, Queen or Jack'
INVALID_CARD_TYPE_MESSAGE = 'Invalid card type supplied. Should be Spades, Diamonds, Hearts or Clubs'

class Card(object):
    """
    Class which represents a card in a deck.
    """
    def __init__(self, card_value=None, card_type=None):
        """
        Initializes a card object

        @param value - string: 2 - 10, Q, K, A, J
        @param type - string: Spades, Diamonds, Hearts, Clubs
        """
        if card_value in CARD_VALUES:
            self.card_value = card_value
        else:
            raise ValueError(INVALID_CARD_VALUE_MESSAGE)
        if card_type in CARD_TYPES:
            self.card_type = card_type
        else:
            raise ValueError(INVALID_CARD_TYPE_MESSAGE)

    def __repr__(self):
        """
        Representation of a card object in string form.
        """
        return self.card_value + ' of ' + self.card_type
