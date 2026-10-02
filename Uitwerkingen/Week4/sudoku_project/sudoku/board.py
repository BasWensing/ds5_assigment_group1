class SudokuBoard:
    """Klasse die het 9x9 Sudoku-bord beheert en zet-validatie uitvoert."""

    def __init__(self, grid=None):
        # Als er geen grid wordt meegegeven, maken we een leeg 9x9 grid
        if grid is None:
            self.grid = [[0] * 9 for _ in range(9)]
        else:
            self.grid = [row[:] for row in grid]

        # Onthoud de initiële staat (de 'clues'/aanwijzingen die niet gewijzigd mogen worden)
        self.initial_clues = [[cell != 0 for cell in row] for row in self.grid]

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """Controleert of het plaatsen van 'num' op (row, col) geldig is volgens de regels."""
        if num < 1 or num > 9:
            return False

        # Check rij
        for c in range(9):
            if c != col and self.grid[row][c] == num:
                return False

        # Check kolom
        for r in range(9):
            if r != row and self.grid[r][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r != row or c != col) and self.grid[r][c] == num:
                    return False

        return True

    def set_cell(self, row: int, col: int, num: int) -> bool:
        """Plaatst een getal in een cel als het een geldige zet is en geen initiële clue is."""
        if self.initial_clues[row][col]:
            return False  # Initiële cijfers mogen niet aangepast worden

        if num == 0 or self.is_valid_move(row, col, num):
            self.grid[row][col] = num
            return True
        return False

    def is_complete(self) -> bool:
        """Controleert of het hele bord correct is ingevuld."""
        for r in range(9):
            for c in range(9):
                val = self.grid[r][c]
                if val == 0 or not self.is_valid_move(r, c, val):
                    return False
        return True