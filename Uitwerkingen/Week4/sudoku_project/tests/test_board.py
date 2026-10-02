import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sudoku.board import SudokuBoard


def test_valid_move():
    board = SudokuBoard()

    # Geldige zet op leeg bord
    assert board.is_valid_move(0, 0, 5) is True

    # Zet uitvoeren
    board.set_cell(0, 0, 5)

    # Ongeldige zet: dubbele 5 in dezelfde rij
    assert board.is_valid_move(0, 4, 5) is False

    # Ongeldige zet: dubbele 5 in dezelfde kolom
    assert board.is_valid_move(4, 0, 5) is False

    # Ongeldige zet: dubbele 5 in hetzelfde 3x3 blok
    assert board.is_valid_move(1, 1, 5) is False

    print("test_valid_move: GESLAAGD!")


def test_initial_clues_protection():
    initial_grid = [[0] * 9 for _ in range(9)]
    initial_grid[0][0] = 7

    board = SudokuBoard(initial_grid)

    # Probeer een initiële clue te overschrijven
    success = board.set_cell(0, 0, 3)
    assert success is False
    assert board.grid[0][0] == 7

    print("test_initial_clues_protection: GESLAAGD!")


if __name__ == "__main__":
    test_valid_move()
    test_initial_clues_protection()