import unittest

from minesweeper.settings import (
    DIFFICULTIES,
    get_difficulty
)


class TestSettings(unittest.TestCase):

    def test_beginner_settings(self):
        settings = get_difficulty(
            "beginner"
        )

        self.assertEqual(
            settings["rows"],
            9
        )

        self.assertEqual(
            settings["cols"],
            9
        )

        self.assertEqual(
            settings["mines"],
            10
        )

    def test_intermediate_settings(self):
        settings = get_difficulty(
            "intermediate"
        )

        self.assertEqual(
            settings["rows"],
            16
        )

        self.assertEqual(
            settings["cols"],
            16
        )

        self.assertEqual(
            settings["mines"],
            40
        )

    def test_expert_settings(self):
        settings = get_difficulty(
            "expert"
        )

        self.assertEqual(
            settings["rows"],
            16
        )

        self.assertEqual(
            settings["cols"],
            30
        )

        self.assertEqual(
            settings["mines"],
            99
        )

    def test_invalid_difficulty(self):
        with self.assertRaises(
            ValueError
        ):
            get_difficulty(
                "impossible"
            )


if __name__ == "__main__":
    unittest.main()