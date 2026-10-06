import time

from .board import Board


class MinesweeperGame:
    def __init__(
        self,
        rows,
        cols,
        mine_count,
        mine_positions=None
    ):
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count

        self.board = Board(
            rows,
            cols,
            mine_count,
            mine_positions
        )

        self.status = "ready"

        self.start_time = None
        self.end_time = None

        self.exploded_cell = None

    def start(self):
        if self.status == "ready":
            self.status = "playing"
            self.start_time = time.monotonic()

    def reveal(self, row, col):
        if self.status in ("won", "lost", "given_up"):
            return set()

        if (row, col) in self.board.flags:
            return set()

        self.start()

        if self.board.is_mine(row, col):
            self.status = "lost"
            self.end_time = time.monotonic()
            self.exploded_cell = (row, col)

            return set()

        revealed = self.board.reveal_safe_cells(
            row,
            col
        )

        if self.board.all_safe_cells_revealed():
            self.status = "won"
            self.end_time = time.monotonic()

        return revealed

    def toggle_flag(self, row, col):
        if self.status in ("won", "lost", "given_up"):
            return False

        self.start()

        return self.board.toggle_flag(row, col)

    def give_up(self):
        if self.status in ("won", "lost", "given_up"):
            return

        if self.start_time is None:
            self.start_time = time.monotonic()

        self.end_time = time.monotonic()
        self.status = "given_up"

    @property
    def score(self):
        return len(self.board.revealed)

    @property
    def elapsed_time(self):
        if self.start_time is None:
            return 0

        if self.end_time is not None:
            return int(self.end_time - self.start_time)

        return int(time.monotonic() - self.start_time)