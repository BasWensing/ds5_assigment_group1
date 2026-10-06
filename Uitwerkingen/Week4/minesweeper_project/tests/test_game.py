import unittest

from minesweeper.game import MinesweeperGame


class TestGame(unittest.TestCase):

    def test_clicking_mine_loses_game(self):
        game = MinesweeperGame(
            2,
            2,
            1,
            mine_positions={(0, 0)}
        )

        game.reveal(
            0,
            0
        )

        self.assertEqual(
            game.status,
            "lost"
        )

    def test_score(self):
        game = MinesweeperGame(
            2,
            2,
            1,
            mine_positions={(0, 0)}
        )

        game.reveal(
            1,
            1
        )

        self.assertEqual(
            game.score,
            1
        )

    def test_winning_game(self):
        game = MinesweeperGame(
            2,
            2,
            1,
            mine_positions={(0, 0)}
        )

        game.reveal(0, 1)
        game.reveal(1, 0)
        game.reveal(1, 1)

        self.assertEqual(
            game.status,
            "won"
        )

    def test_give_up(self):
        game = MinesweeperGame(
            2,
            2,
            1,
            mine_positions={(0, 0)}
        )

        game.give_up()

        self.assertEqual(
            game.status,
            "given_up"
        )


if __name__ == "__main__":
    unittest.main()