import sys
from pathlib import Path

# Voeg de root-map toe aan sys.path zodat 'sudoku' geïmporteerd kan worden
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sudoku.board import SudokuBoard
from sudoku.file_loader import load_puzzle_from_file
from sudoku.solver import SudokuSolver


def main():
    # Pad naar de JSON-puzzel
    json_path = project_root / "data" / "puzzle_02.json"

    print("=== Sudoku CLI Voorbeeld ===")
    print(f"Laden van puzzel uit: {json_path.name}\n")

    # 1. Puzzel laden
    grid = load_puzzle_from_file(str(json_path))
    board = SudokuBoard(grid)

    print("Initiële Puzzel:")
    for row in board.grid:
        print(row)

    # 2. Puzzel oplossen
    solver = SudokuSolver(board)
    if solver.solve():
        print("\nOpgeloste Sudoku:")
        for row in board.grid:
            print(row)
        print(f"\nBord correct voltooid? {board.is_complete()}")
    else:
        print("\nGeen oplossing gevonden.")


if __name__ == "__main__":
    main()