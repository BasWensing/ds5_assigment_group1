import random


SUITS = ("klaveren", "ruiten", "harten", "schoppen")
CARD_VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, "boer", "vrouw", "heer", "aas")
FACE_CARD_VALUES = {"boer": 10, "vrouw": 10, "heer": 10}


def create_deck():
	"""Maak een standaard deck van 52 unieke kaarten."""
	return [(value, suit) for suit in SUITS for value in CARD_VALUES]


def format_card(card):
	"""Geef een kaart leesbaar weer."""
	value, suit = card
	return f"{value} {suit}"


def format_hand(hand):
	return ", ".join(format_card(card) for card in hand)


def calculate_hand_value(hand):
	"""Bereken de beste handwaarde waarbij een aas 1 of 11 kan zijn."""
	value = 0
	aces = 0

	for card_value, _ in hand:
		if card_value == "aas":
			value += 11
			aces += 1
		elif isinstance(card_value, int):
			value += card_value
		else:
			value += FACE_CARD_VALUES[card_value]

	while value > 21 and aces:
		value -= 10
		aces -= 1

	return value


def deal_card(deck):
	"""Trek een kaart en verwijder die uit het deck."""
	if not deck:
		raise ValueError("Het deck bevat geen kaarten meer.")
	return deck.pop()


def print_status(player_hand, dealer_hand):
	print(f"Speler: {format_hand(player_hand)} | som: {calculate_hand_value(player_hand)}")
	print(f"Dealer: {format_hand(dealer_hand)} | som: {calculate_hand_value(dealer_hand)}")


def determine_winner(player_hand, dealer_hand):
	"""Bepaal de uitslag en geef deze terug als tekst."""
	player_value = calculate_hand_value(player_hand)
	dealer_value = calculate_hand_value(dealer_hand)

	if player_value > 21:
		return "verlies speler"
	if dealer_value > 21:
		return "winst speler"
	if player_value > dealer_value:
		return "winst speler"
	if player_value < dealer_value:
		return "verlies speler"
	return "gelijkspel"


def player_turn(deck, player_hand, dealer_hand):
	while calculate_hand_value(player_hand) <= 21:
		print_status(player_hand, dealer_hand)
		command = input("Kies 'hit' of 'stand': ").strip().lower()

		if command == "stand":
			return
		if command == "hit":
			player_hand.append(deal_card(deck))
			continue
		print("Ongeldige invoer. Gebruik alleen 'hit' of 'stand'.")


def dealer_turn(deck, player_hand, dealer_hand):
	while calculate_hand_value(dealer_hand) < 17:
		print_status(player_hand, dealer_hand)
		dealer_hand.append(deal_card(deck))

	print_status(player_hand, dealer_hand)


def play_round():
	deck = create_deck()
	random.shuffle(deck)

	player_hand = [deal_card(deck), deal_card(deck)]
	dealer_hand = [deal_card(deck), deal_card(deck)]

	player_turn(deck, player_hand, dealer_hand)

	if calculate_hand_value(player_hand) <= 21:
		dealer_turn(deck, player_hand, dealer_hand)

	print("\nEindstand:")
	print_status(player_hand, dealer_hand)
	print(f"Uitkomst: {determine_winner(player_hand, dealer_hand)}")


def main():
	play_round()


if __name__ == "__main__":
	main()
