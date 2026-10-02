from blackjack import cards, game


def format_card(card):
	value, suit = card
	return f"{value} {suit}"


def format_hand(hand):
	return ", ".join(format_card(card) for card in hand)


def print_status(player_hand, dealer_hand):
	print(f"Speler: {format_hand(player_hand)} | som: {game.calculate_hand_value(player_hand)}")
	print(f"Dealer: {format_hand(dealer_hand)} | som: {game.calculate_hand_value(dealer_hand)}")


def get_player_action(player_hand=None, dealer_hand=None):
	while True:
		if player_hand is not None and dealer_hand is not None:
			print_status(player_hand, dealer_hand)

		command = input("Kies 'hit' of 'stand': ").strip().lower()
		if command in ("hit", "stand"):
			return command
		print("Ongeldige invoer. Gebruik alleen 'hit' of 'stand'.")


def player_turn(deck, player_hand, dealer_hand):
	while not game.is_bust(player_hand):
		command = get_player_action(player_hand, dealer_hand)
		if command == "stand":
			return player_hand
		player_hand.append(cards.deal_card(deck))
	return player_hand


def play_round():
	deck = cards.create_deck()
	cards.shuffle_deck(deck)

	player_hand = [cards.deal_card(deck), cards.deal_card(deck)]
	dealer_hand = [cards.deal_card(deck), cards.deal_card(deck)]

	if not game.is_blackjack(player_hand) and not game.is_blackjack(dealer_hand):
		player_turn(deck, player_hand, dealer_hand)
		if not game.is_bust(player_hand):
			game.dealer_turn(deck, dealer_hand, lambda: print_status(player_hand, dealer_hand))

	print("\nEindstand:")
	print_status(player_hand, dealer_hand)
	outcome = game.determine_winner(player_hand, dealer_hand)
	labels = {"player": "winst speler", "dealer": "verlies speler", "tie": "gelijkspel"}
	print(f"Uitkomst: {labels[outcome]}")
	return outcome


def main():
	play_round()


if __name__ == "__main__":
	main()
