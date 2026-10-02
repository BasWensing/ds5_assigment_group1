import sys
import tkinter as tk
from pathlib import Path

# Voeg de root-map toe aan sys.path zodat 'sudoku' geïmporteerd kan worden
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sudoku.gui import SudokuGUI


def main():
    """Start de Sudoku GUI applicatie vanuit de examples-map."""
    print("=== Sudoku GUI Voorbeeld ===")
    print("De grafische interface wordt nu gestart...")

    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()