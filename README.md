# Card deck project

This project defines two classes - Card(in card.py) and Deck(in deck.py). The Card class represents a card in a deck. The Deck class represents a deck of cards and has methods to initialize the deck, list cards in a deck, shuffle cards in the deck and to deal one card from the deck. When the deck is empty after dealing one card 52 items we return a `Deck is empty` message from the `deal_one_card` method

To run the code follow these steps:

1. Open the python or ipython prompt
2. Run `from deck import Deck`
3. Create a card_deck object using `card_deck = Deck()`
4. List the cards in the deck using `card_deck.list_deck_of_cards()`
5. Shuffle the cards using `card_deck.shuffle()`
6. Deal one card in the deck using `card_deck.deal_one_card()`

There are associated unit tests in this project which can be run using `python -m unittest -v test_deck.py`
