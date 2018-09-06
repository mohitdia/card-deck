#!/usr/bin/python
"""
This module contains tests for deck module.
"""

import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.card_deck = Deck()

    def test_deck_size(self):
        self.assertEqual(len(self.card_deck.deck), 52)
    
    def test_shuffle(self):
        self.card_deck.shuffle()
        self.assertEqual(len(self.card_deck.deck), 52)

    def test_deal_one_card(self):
        self.assertEqual(len(self.card_deck.deck), 52)
        self.card_deck.deal_one_card()
        #Assert that after dealing one card we are left with 51 cards
        self.assertEqual(len(self.card_deck.deck), 51)

    def test_deck_empty(self):
        self.assertEqual(len(self.card_deck.deck), 52)
        for i in range(len(self.card_deck.deck)):
            self.card_deck.deal_one_card()
        #Assert after calling deal_one_card 52 items we don't have any cards left
        self.assertEqual(len(self.card_deck.deck), 0)
        #If deal_one_card is called again the method returns Deck is empty message
        self.assertEqual(self.card_deck.deal_one_card(), 'Deck is empty')

if __name__ == '__main__':
    unittest.main()
