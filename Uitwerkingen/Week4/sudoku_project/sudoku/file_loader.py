import json
import os
from typing import List


def load_puzzle_from_file(filepath: str) -> List[List[int]]:
    """Laadt een Sudoku-puzzel uit een .txt of .json bestand.

    - .txt: Verwacht 81 cijfers (0 of . voor leeg) of 9 regels met 9 cijfers.
    - .json: Verwacht een JSON-object met een "grid" of "puzzle" sleutel
    bestaande uit een 2D-lijst.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Het bestand '{filepath}' is niet gevonden."
        )

    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".json":
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Accepteer "grid" of "puzzle" als sleutel in het JSON-bestand
            grid = data.get("grid") or data.get("puzzle")
            if not grid or len(grid) != 9 or any(len(row) != 9 for row in grid):
                raise ValueError(
                    "Ongeldig JSON-formaat. Verwacht een 9x9 matrix."
                )
            return grid

    elif ext == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()

        # Vervang punten of streepjes door 0 voor lege cellen
        clean_content = (
            content.replace(".", "0").replace("-", "0").replace("\n", "")
        )
        digits = [int(char) for char in clean_content if char.isdigit()]

        if len(digits) != 81:
            raise ValueError(
                f"Ongeldige tekstpuzzel. Verwacht 81 cijfers, maar vond er {len(digits)}."
            )

        # Converteer 81 cijfers naar een 9x9 2D-lijst
        return [digits[i * 9 : (i + 1) * 9] for i in range(9)]

    else:
        raise ValueError(
            f"Niet-ondersteunde bestandsextensie '{ext}'. Gebruik .txt of .json."
        )