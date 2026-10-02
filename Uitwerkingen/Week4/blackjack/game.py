from blackjack.cards import deal_card


FACE_CARD_VALUES = {"boer": 10, "vrouw": 10, "heer": 10}


def calculate_hand_value(hand):
	"""Bereken de handwaarde; een aas telt als 1 of 11."""
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


def is_blackjack(hand):
	"""Geef aan of een hand uit twee kaarten met waarde 21 bestaat."""
	return len(hand) == 2 and calculate_hand_value(hand) == 21


def is_bust(hand):
	return calculate_hand_value(hand) > 21


def determine_winner(player_hand, dealer_hand):
	"""Geef 'player', 'dealer' of 'tie' terug."""
	player_blackjack = is_blackjack(player_hand)
	dealer_blackjack = is_blackjack(dealer_hand)

	if player_blackjack and dealer_blackjack:
		return "tie"
	if player_blackjack:
		return "player"
	if dealer_blackjack:
		return "dealer"
	if is_bust(player_hand):
		return "dealer"
	if is_bust(dealer_hand):
		return "player"

	player_value = calculate_hand_value(player_hand)
	dealer_value = calculate_hand_value(dealer_hand)
	if player_value > dealer_value:
		return "player"
	if player_value < dealer_value:
		return "dealer"
	return "tie"


def dealer_turn(deck, dealer_hand, before_decision=None):
	"""Laat de dealer trekken tot minstens 17; retourneer de hand."""
	while True:
		if before_decision is not None:
			before_decision()
		if calculate_hand_value(dealer_hand) >= 17:
			return dealer_hand
		dealer_hand.append(deal_card(deck))
