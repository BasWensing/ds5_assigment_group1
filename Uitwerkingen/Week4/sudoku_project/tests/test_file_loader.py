import sys
from pathlib import Path
import pytest

# Voeg de project-root toe aan sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sudoku.file_loader import load_puzzle_from_file


def test_load_txt_file():
    txt_path = project_root / "data" / "puzzle_01.txt"
    grid = load_puzzle_from_file(str(txt_path))
    
    # Controleer of de matrix 9x9 is
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)
    # Controleer de waarde van een specifieke bekende cel
    assert isinstance(grid[0][0], int)
    print("test_load_txt_file: GESLAAGD!")


def test_load_json_file():
    json_path = project_root / "data" / "puzzle_02.json"
    grid = load_puzzle_from_file(str(json_path))
    
    # Controleer of de matrix 9x9 is
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)
    assert grid[0][0] == 5
    print("test_load_json_file: GESLAAGD!")


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_puzzle_from_file("niet_bestaand_bestand.json")
    print("test_file_not_found: GESLAAGD!")


if __name__ == "__main__":
    test_load_txt_file()
    test_load_json_file()
    print("Alle file_loader tests zijn succesvol uitgevoerd!")