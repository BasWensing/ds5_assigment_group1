import unittest

from minesweeper.board import Board


class TestBoard(unittest.TestCase):

    def test_mine_position(self):
        board = Board(
            3,
            3,
            1,
            mine_positions={(0, 0)}
        )

        self.assertTrue(
            board.is_mine(0, 0)
        )

        self.assertFalse(
            board.is_mine(1, 1)
        )

    def test_count_neighbouring_mines(self):
        board = Board(
            3,
            3,
            1,
            mine_positions={(0, 0)}
        )

        result = (
            board.count_neighbouring_mines(
                1,
                1
            )
        )

        self.assertEqual(
            result,
            1
        )

    def test_flag(self):
        board = Board(
            3,
            3,
            1,
            mine_positions={(0, 0)}
        )

        board.toggle_flag(1, 1)

        self.assertIn(
            (1, 1),
            board.flags
        )

        board.toggle_flag(1, 1)

        self.assertNotIn(
            (1, 1),
            board.flags
        )

    def test_reveal_empty_area(self):
        board = Board(
            3,
            3,
            1,
            mine_positions={(2, 2)}
        )

        board.reveal_safe_cells(
            0,
            0
        )

        self.assertIn(
            (0, 0),
            board.revealed
        )

        self.assertNotIn(
            (2, 2),
            board.revealed
        )


if __name__ == "__main__":
    unittest.main()