import random


SUITS = ("klaveren", "ruiten", "harten", "schoppen")
CARD_VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, "boer", "vrouw", "heer", "aas")


def create_deck():
	"""Maak een standaard deck van 52 unieke kaarten."""
	return [(value, suit) for suit in SUITS for value in CARD_VALUES]


def shuffle_deck(deck):
	"""Schud de kaarten in het bestaande deck."""
	random.shuffle(deck)
	return deck


def deal_card(deck):
	"""Trek de bovenste kaart uit het deck en verwijder deze."""
	if not deck:
		raise ValueError("Het deck bevat geen kaarten meer.")
	return deck.pop()
