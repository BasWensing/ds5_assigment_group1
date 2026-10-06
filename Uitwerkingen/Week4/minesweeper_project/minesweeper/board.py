import random
from collections import deque


class Board:
    def __init__(self, rows, cols, mine_count, mine_positions=None):
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count

        self.revealed = set()
        self.flags = set()

        if mine_positions is not None:
            self.mines = set(mine_positions)

            if len(self.mines) != mine_count:
                raise ValueError(
                    "Number of mine positions must match mine_count."
                )
        else:
            self.mines = self._generate_mines()

    def _generate_mines(self):
        positions = [
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
        ]

        return set(random.sample(positions, self.mine_count))

    def is_valid_position(self, row, col):
        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
        )

    def is_mine(self, row, col):
        return (row, col) in self.mines

    def get_neighbours(self, row, col):
        neighbours = []

        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):

                if row_offset == 0 and col_offset == 0:
                    continue

                new_row = row + row_offset
                new_col = col + col_offset

                if self.is_valid_position(new_row, new_col):
                    neighbours.append((new_row, new_col))

        return neighbours

    def count_neighbouring_mines(self, row, col):
        count = 0

        for neighbour in self.get_neighbours(row, col):
            if neighbour in self.mines:
                count += 1

        return count

    def toggle_flag(self, row, col):
        position = (row, col)

        if position in self.revealed:
            return False

        if position in self.flags:
            self.flags.remove(position)
            return False

        self.flags.add(position)
        return True

    def reveal_safe_cells(self, row, col):
        start = (row, col)

        if start in self.mines:
            return set()

        if start in self.flags:
            return set()

        cells_to_check = deque([start])
        newly_revealed = set()

        while cells_to_check:
            current_row, current_col = cells_to_check.popleft()
            position = (current_row, current_col)

            if position in self.revealed:
                continue

            if position in self.flags:
                continue

            if position in self.mines:
                continue

            self.revealed.add(position)
            newly_revealed.add(position)

            mine_count = self.count_neighbouring_mines(
                current_row,
                current_col
            )

            # Empty cell: reveal surrounding cells too
            if mine_count == 0:
                for neighbour in self.get_neighbours(
                    current_row,
                    current_col
                ):
                    if neighbour not in self.revealed:
                        if neighbour not in self.mines:
                            cells_to_check.append(neighbour)

        return newly_revealed

    def all_safe_cells_revealed(self):
        safe_cells = (
            self.rows * self.cols
            - self.mine_count
        )

        return len(self.revealed) == safe_cells