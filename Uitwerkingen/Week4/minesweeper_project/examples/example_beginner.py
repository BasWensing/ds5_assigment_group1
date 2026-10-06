import tkinter as tk

from minesweeper.gui import MinesweeperGUI


root = tk.Tk()

MinesweeperGUI(
    root,
    difficulty="beginner"
)

root.mainloop()