class SudokuSolver:
    """Klasse voor het oplossen van het Sudoku-bord en het genereren van hints."""

    def __init__(self, board):
        self.board = board

    def solve(self) -> bool:
        """Lost het Sudoku-bord op met een backtracking algoritme."""
        empty_cell = self._find_empty()
        if not empty_cell:
            return True  # Geen lege cellen meer, bord is opgelost

        row, col = empty_cell
        for num in range(1, 10):
            if self.board.is_valid_move(row, col, num):
                self.board.grid[row][col] = num

                if self.solve():
                    return True

                # Backtrack als het niet leidt tot een oplossing
                self.board.grid[row][col] = 0

        return False

    def get_hint(self):
        """Geeft een hint terug in de vorm van (row, col, correct_num)."""
        import copy
        from sudoku.board import SudokuBoard

        # Maak een kopie om de oplossing te berekenen
        temp_board = SudokuBoard(self.board.grid)
        temp_solver = SudokuSolver(temp_board)

        if temp_solver.solve():
            for r in range(9):
                for c in range(9):
                    if self.board.grid[r][c] == 0:
                        return r, c, temp_board.grid[r][c]
        return None

    def _find_empty(self):
        """Zoekt naar de eerste lege cel (waarde 0)."""
        for r in range(9):
            for c in range(9):
                if self.board.grid[r][c] == 0:
                    return r, c
        return None