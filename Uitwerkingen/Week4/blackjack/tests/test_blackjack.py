import contextlib
import io
import unittest
from unittest import mock

from blackjack import cards, cli, game


def card(rank, suit="klaveren"):
	return (rank, suit)


class TestCards(unittest.TestCase):
	def test_create_deck_contains_52_unique_cards(self):
		deck = cards.create_deck()

		self.assertEqual(len(deck), 52)
		self.assertEqual(len(set(deck)), 52)
		self.assertEqual(
			{suit for _, suit in deck},
			{"klaveren", "ruiten", "harten", "schoppen"},
		)

	def test_shuffle_deck_shuffles_the_existing_deck(self):
		deck = cards.create_deck()
		original_cards = set(deck)

		with mock.patch("blackjack.cards.random.shuffle") as shuffle:
			result = cards.shuffle_deck(deck)

		shuffle.assert_called_once_with(deck)
		self.assertIs(result, deck)
		self.assertEqual(set(deck), original_cards)

	def test_deal_card_removes_and_returns_a_card(self):
		deck = [card(2), card(10, "harten")]

		dealt_card = cards.deal_card(deck)

		self.assertEqual(dealt_card, card(10, "harten"))
		self.assertEqual(deck, [card(2)])

	def test_deal_card_rejects_an_empty_deck(self):
		with self.assertRaises(ValueError):
			cards.deal_card([])


class TestHandRules(unittest.TestCase):
	def test_numeric_and_face_cards_have_correct_values(self):
		hand = [card(2), card(10, "ruiten"), card("boer", "harten")]

		self.assertEqual(game.calculate_hand_value(hand), 22)

	def test_ace_counts_as_eleven_when_hand_does_not_bust(self):
		hand = [card("aas"), card(7, "schoppen")]

		self.assertEqual(game.calculate_hand_value(hand), 18)

	def test_ace_counts_as_one_when_eleven_would_bust(self):
		hand = [card("aas"), card(9, "ruiten"), card(5, "harten")]

		self.assertEqual(game.calculate_hand_value(hand), 15)

	def test_multiple_aces_are_adjusted_independently(self):
		hand = [card("aas"), card("aas", "ruiten"), card(9, "harten")]

		self.assertEqual(game.calculate_hand_value(hand), 21)

	def test_blackjack_requires_two_cards_with_value_21(self):
		natural = [card("aas"), card("heer", "harten")]
		three_card_21 = [card(7), card(7, "ruiten"), card(7, "harten")]

		self.assertTrue(game.is_blackjack(natural))
		self.assertFalse(game.is_blackjack(three_card_21))

	def test_bust_is_a_hand_over_21(self):
		self.assertFalse(game.is_bust([card(10), card(9, "ruiten")]))
		self.assertTrue(game.is_bust([card(10), card(9, "ruiten"), card(3, "harten")]))

	def test_determine_winner_handles_win_loss_tie_and_bust(self):
		self.assertEqual(
			game.determine_winner([card(10), card(8)], [card(10, "ruiten"), card(7)]),
			"player",
		)
		self.assertEqual(
			game.determine_winner([card(10), card(7)], [card(10, "ruiten"), card(9)]),
			"dealer",
		)
		self.assertEqual(
			game.determine_winner([card(10), card(8)], [card(10, "ruiten"), card(8, "harten")]),
			"tie",
		)
		self.assertEqual(
			game.determine_winner([card(10), card(9), card(3)], [card(10, "ruiten"), card(8)]),
			"dealer",
		)

	def test_natural_blackjack_beats_a_non_natural_21(self):
		player_natural = [card("aas"), card("heer", "harten")]
		dealer_natural = [card("aas", "ruiten"), card("vrouw", "schoppen")]
		non_natural_21 = [card(7), card(7, "ruiten"), card(7, "harten")]

		self.assertEqual(game.determine_winner(player_natural, non_natural_21), "player")
		self.assertEqual(game.determine_winner(non_natural_21, dealer_natural), "dealer")
		self.assertEqual(game.determine_winner(player_natural, dealer_natural), "tie")


class TestTurnsAndConsole(unittest.TestCase):
	def test_dealer_draws_until_at_least_17(self):
		dealer_hand = [card(10), card(5, "harten")]
		deck = [card(2, "ruiten"), card(2, "schoppen")]

		game.dealer_turn(deck, dealer_hand)

		self.assertEqual(game.calculate_hand_value(dealer_hand), 17)
		self.assertEqual(deck, [card(2, "ruiten")])

	def test_dealer_stands_on_17(self):
		dealer_hand = [card(10), card(7, "harten")]
		deck = [card(2, "ruiten")]

		game.dealer_turn(deck, dealer_hand)

		self.assertEqual(len(dealer_hand), 2)
		self.assertEqual(len(deck), 1)

	def test_invalid_input_is_rejected_until_valid_action(self):
		output = io.StringIO()
		with mock.patch("builtins.input", side_effect=["double", " HIT "]), contextlib.redirect_stdout(output):
			action = cli.get_player_action()

		self.assertEqual(action, "hit")
		self.assertIn("hit", output.getvalue().lower())
		self.assertIn("stand", output.getvalue().lower())

	def test_player_turn_prints_both_hands_and_scores_before_each_decision(self):
		player_hand = [card(5), card(6, "harten")]
		dealer_hand = [card(10, "ruiten"), card(7, "schoppen")]
		deck = [card(2, "klaveren")]
		output = io.StringIO()

		with mock.patch("builtins.input", side_effect=["invalid", "hit", "stand"]), contextlib.redirect_stdout(output):
			cli.player_turn(deck, player_hand, dealer_hand)

		transcript = output.getvalue()
		self.assertGreaterEqual(transcript.count("Speler:"), 3)
		self.assertGreaterEqual(transcript.count("Dealer:"), 3)
		self.assertIn("11", transcript)
		self.assertIn("17", transcript)
		self.assertEqual(game.calculate_hand_value(player_hand), 13)


if __name__ == "__main__":
	unittest.main()
