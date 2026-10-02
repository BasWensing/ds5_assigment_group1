import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sudoku.board import SudokuBoard
from sudoku.solver import SudokuSolver


def test_solver_valid_puzzle():
    # Voorbeeld met een bekende, oplosbare Sudoku
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    board = SudokuBoard(grid)
    solver = SudokuSolver(board)

    # Controleer of de solver True returnt
    assert solver.solve() is True
    # Controleer of de opgeloste status geldig is
    assert board.is_complete() is True
    print("test_solver_valid_puzzle: GESLAAGD!")


def test_hint_generation():
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    board = SudokuBoard(grid)
    solver = SudokuSolver(board)

    hint = solver.get_hint()
    # De hint moet een tuple (row, col, value) zijn
    assert hint is not None
    r, c, val = hint
    assert board.grid[r][c] == 0  # Hint moet op een momenteel lege plek zijn
    assert 1 <= val <= 9
    print("test_hint_generation: GESLAAGD!")


if __name__ == "__main__":
    test_solver_valid_puzzle()
    test_hint_generation()
    print("Alle solver tests zijn succesvol uitgevoerd!")