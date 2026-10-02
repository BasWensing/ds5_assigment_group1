import tkinter as tk
from tkinter import filedialog, messagebox
from sudoku.board import SudokuBoard
from sudoku.file_loader import load_puzzle_from_file
from sudoku.solver import SudokuSolver


class SudokuGUI:
    """Tkinter Grafische User Interface voor de Sudoku applicatie."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Python 9x9 Sudoku")
        self.root.geometry("450 x 550")
        self.root.resizable(False, False)

        # Standaard voorbeeldpuzzel
        default_grid = [
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

        self.board = SudokuBoard(default_grid)
        self.cells = {}

        self._create_widgets()
        self._update_gui_from_board()

    def _create_widgets(self):
        """Bouwt de Tkinter-grid en bedieningsknoppen op."""
        # Grid Frame
        grid_frame = tk.Frame(self.root, bg="black", bd=2)
        grid_frame.pack(pady=15)

        vcmd = (self.root.register(self._validate_input), "%P")

        # Maak 9x9 cellen met extra dikke randen voor 3x3 blokken
        for r in range(9):
            for c in range(9):
                pad_y = (2 if r % 3 == 0 and r != 0 else 0, 1)
                pad_x = (2 if c % 3 == 0 and c != 0 else 0, 1)

                cell_frame = tk.Frame(grid_frame, bg="gray")
                cell_frame.grid(
                    row=r, column=c, padx=pad_x, pady=pad_y, sticky="nsew"
                )

                entry = tk.Entry(
                    cell_frame,
                    width=2,
                    font=("Helvetica", 18, "bold"),
                    justify="center",
                    bd=0,
                    validate="key",
                    validatecommand=vcmd,
                )
                entry.pack(fill="both", expand=True)

                # Bind event bij handmatige invoer
                entry.bind(
                    "<KeyRelease>",
                    lambda e, row=r, col=c: self._on_cell_edit(row, col),
                )
                self.cells[(r, c)] = entry

        # Knoppen Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Hint",
            width=10,
            command=self._get_hint,
            bg="#e1f5fe",
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame,
            text="Oplossen",
            width=10,
            command=self._solve_puzzle,
            bg="#c8e6c9",
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            btn_frame,
            text="Laden",
            width=10,
            command=self._load_file,
            bg="#fff9c4",
        ).grid(row=0, column=2, padx=5)

        # Status Bar
        self.status_label = tk.Label(
            self.root,
            text="Welkom bij Sudoku!",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def _validate_input(self, P: str) -> bool:
        """Zorgt ervoor dat de gebruiker alleen cijfers 1-9 kan invoeren."""
        return P == "" or (P.isdigit() and len(P) == 1 and P != "0")

    def _on_cell_edit(self, row: int, col: int):
        """Verwerkt handmatige invoer in een cel."""
        val = self.cells[(row, col)].get()
        num = int(val) if val.isdigit() else 0

        if not self.board.set_cell(row, col, num):
            self.status_label.config(
                text=f"Ongeldige zet op rij {row+1}, kolom {col+1}!"
            )
            self.cells[(row, col)].config(fg="red")
        else:
            self.cells[(row, col)].config(fg="blue")
            if self.board.is_complete():
                messagebox.showinfo("Gefeliciteerd!", "Sudoku succesvol opgelost!")
                self.status_label.config(text="Sudoku Voltooid!")
            else:
                self.status_label.config(text="Zet geaccepteerd.")

    def _get_hint(self):
        """Haalt een hint op en plaatst deze op het bord."""
        solver = SudokuSolver(self.board)
        hint = solver.get_hint()
        if hint:
            r, c, num = hint
            self.board.grid[r][c] = num
            self.cells[(r, c)].delete(0, tk.END)
            self.cells[(r, c)].insert(0, str(num))
            self.cells[(r, c)].config(fg="green")
            self.status_label.config(
                text=f"Hint toegevoegd op rij {r+1}, kolom {c+1}."
            )
        else:
            messagebox.showwarning(
                "Geen Hint", "Kan geen hint geven voor de huidige staat."
            )

    def _solve_puzzle(self):
        """Lost de gehele Sudoku op."""
        solver = SudokuSolver(self.board)
        if solver.solve():
            self._update_gui_from_board()
            self.status_label.config(text="Puzzel opgelost!")
        else:
            messagebox.showerror(
                "Fout", "Deze puzzel heeft geen geldige oplossing."
            )

    def _load_file(self):
        """Opent een bestandskiezer om een .txt of .json puzzel te laden."""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Sudoku Files", "*.txt *.json"),
                ("Text Files", "*.txt"),
                ("JSON Files", "*.json"),
            ]
        )
        if file_path:
            try:
                grid = load_puzzle_from_file(file_path)
                self.board = SudokuBoard(grid)
                self._update_gui_from_board()
                self.status_label.config(
                    text=f"Bestand geladen: {os.path.basename(file_path)}"
                )
            except Exception as e:
                messagebox.showerror("Fout bij laden", str(e))

    def _update_gui_from_board(self):
        """Ververst alle velden in het scherm op basis van de board.grid waarden."""
        for r in range(9):
            for c in range(9):
                val = self.board.grid[r][c]
                entry = self.cells[(r, c)]
                entry.delete(0, tk.END)

                if val != 0:
                    entry.insert(0, str(val))
                    if self.board.initial_clues[r][c]:
                        entry.config(
                            state="normal",
                            fg="black",
                            font=("Helvetica", 18, "bold"),
                        )
                    else:
                        entry.config(state="normal", fg="blue")
                else:
                    entry.config(state="normal", fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()