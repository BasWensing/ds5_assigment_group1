from blackjack import cards, game


def main():
    deck = cards.create_deck()
    cards.shuffle_deck(deck)

    hand = [cards.deal_card(deck), cards.deal_card(deck)]

    print(f"Getrokken kaarten: {hand}")
    print(f"Handwaarde: {game.calculate_hand_value(hand)}")
    print(f"Kaarten over: {len(deck)}")


if __name__ == "__main__":
    main()

from blackjack import game


def main():
    player_hand = [("aas", "harten"), ("heer", "schoppen")]
    dealer_hand = [(10, "ruiten"), (7, "klaveren")]

    print(f"Spelerscore: {game.calculate_hand_value(player_hand)}")
    print(f"Dealerscore: {game.calculate_hand_value(dealer_hand)}")
    print(f"Uitslag: {game.determine_winner(player_hand, dealer_hand)}")


if __name__ == "__main__":
    main()