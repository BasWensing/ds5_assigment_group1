import tkinter as tk

from .game import MinesweeperGame
from .settings import DIFFICULTIES, get_difficulty


class MinesweeperGUI:
    def __init__(self, root, difficulty="beginner"):
        self.root = root

        self.root.title("Minesweeper")

        self.current_difficulty = difficulty
        self.buttons = []

        self.create_top_bar()
        self.create_board_frame()

        self.new_game(difficulty)

        self.update_timer()

    def create_top_bar(self):
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=5)

        self.score_label = tk.Label(
            self.top_frame,
            text="Score: 0",
            font=("Arial", 12)
        )

        self.score_label.pack(
            side=tk.LEFT,
            padx=10
        )

        self.timer_label = tk.Label(
            self.top_frame,
            text="Time: 0",
            font=("Arial", 12)
        )

        self.timer_label.pack(
            side=tk.LEFT,
            padx=10
        )

        self.settings_button = tk.Button(
            self.top_frame,
            text="Settings",
            command=self.show_settings
        )

        self.settings_button.pack(
            side=tk.LEFT,
            padx=10
        )

        self.give_up_button = tk.Button(
            self.top_frame,
            text="Give Up",
            command=self.give_up
        )

        self.give_up_button.pack(
            side=tk.LEFT,
            padx=10
        )

    def create_board_frame(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(padx=10, pady=10)

    def new_game(self, difficulty=None):
        if difficulty is not None:
            self.current_difficulty = difficulty

        settings = get_difficulty(
            self.current_difficulty
        )

        self.game = MinesweeperGame(
            settings["rows"],
            settings["cols"],
            settings["mines"]
        )

        self.create_grid()

        self.update_display()

    def create_grid(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.buttons = []

        for row in range(self.game.rows):
            button_row = []

            for col in range(self.game.cols):
                button = tk.Button(
                    self.board_frame,
                    width=2,
                    height=1,
                    font=("Arial", 10),
                    command=lambda r=row, c=col:
                    self.left_click(r, c)
                )

                button.bind(
                    "<Button-3>",
                    lambda event, r=row, c=col:
                    self.right_click(r, c)
                )

                button.grid(
                    row=row,
                    column=col
                )

                button_row.append(button)

            self.buttons.append(button_row)

    def left_click(self, row, col):
        if self.game.status in (
            "won",
            "lost",
            "given_up"
        ):
            return

        self.game.reveal(row, col)

        self.update_display()

        if self.game.status == "lost":
            self.show_game_over(
                "Game Over!"
            )

        elif self.game.status == "won":
            self.show_game_over(
                "You won!"
            )

    def right_click(self, row, col):
        if self.game.status in (
            "won",
            "lost",
            "given_up"
        ):
            return "break"

        self.game.toggle_flag(row, col)

        self.update_display()

        return "break"

    def update_display(self):
        for row in range(self.game.rows):
            for col in range(self.game.cols):

                button = self.buttons[row][col]
                position = (row, col)

                button.config(
                    text="",
                    relief=tk.RAISED,
                    state=tk.NORMAL,
                    bg="SystemButtonFace"
                )

                if position in self.game.board.revealed:

                    mine_count = (
                        self.game.board
                        .count_neighbouring_mines(
                            row,
                            col
                        )
                    )

                    if mine_count > 0:
                        button.config(
                            text=str(mine_count)
                        )

                    button.config(
                        relief=tk.SUNKEN,
                        state=tk.DISABLED
                    )

                elif position in self.game.board.flags:
                    button.config(
                        text="🚩"
                    )

        if self.game.status in (
            "lost",
            "given_up"
        ):
            self.show_mines()

        self.score_label.config(
            text=f"Score: {self.game.score}"
        )

    def show_mines(self):
        for row, col in self.game.board.mines:

            button = self.buttons[row][col]

            button.config(
                text="💣"
            )

            if (
                self.game.exploded_cell
                == (row, col)
            ):
                button.config(
                    bg="red"
                )

    def give_up(self):
        if self.game.status in (
            "won",
            "lost",
            "given_up"
        ):
            return

        self.game.give_up()

        self.update_display()

        self.show_game_over(
            "You gave up!"
        )

    def show_game_over(self, title):
        window = tk.Toplevel(self.root)

        window.title(title)

        window.transient(self.root)
        window.grab_set()

        message = tk.Label(
            window,
            text=(
                f"{title}\n\n"
                f"Score: {self.game.score}\n"
                f"Time: {self.game.elapsed_time} seconds"
            ),
            font=("Arial", 14)
        )

        message.pack(
            padx=30,
            pady=20
        )

        play_again = tk.Button(
            window,
            text="Play Again",
            command=lambda:
            self.restart_from_window(window)
        )

        play_again.pack(
            pady=5
        )

        exit_button = tk.Button(
            window,
            text="Exit",
            command=self.root.destroy
        )

        exit_button.pack(
            pady=5
        )

    def restart_from_window(self, window):
        window.destroy()

        self.new_game(
            self.current_difficulty
        )

    def show_settings(self):
        settings_window = tk.Toplevel(
            self.root
        )

        settings_window.title(
            "Difficulty Settings"
        )

        tk.Label(
            settings_window,
            text="Select difficulty:",
            font=("Arial", 12)
        ).pack(pady=10)

        selected = tk.StringVar(
            value=self.current_difficulty
        )

        for difficulty in DIFFICULTIES:

            settings = DIFFICULTIES[
                difficulty
            ]

            text = (
                f"{difficulty.capitalize()} "
                f"({settings['cols']}x"
                f"{settings['rows']}, "
                f"{settings['mines']} mines)"
            )

            tk.Radiobutton(
                settings_window,
                text=text,
                variable=selected,
                value=difficulty
            ).pack(anchor="w", padx=20)

        apply_button = tk.Button(
            settings_window,
            text="Apply",
            command=lambda:
            self.apply_settings(
                selected.get(),
                settings_window
            )
        )

        apply_button.pack(pady=15)

    def apply_settings(
        self,
        difficulty,
        window
    ):
        window.destroy()

        self.new_game(difficulty)

    def update_timer(self):
        if hasattr(self, "game"):

            self.timer_label.config(
                text=(
                    f"Time: "
                    f"{self.game.elapsed_time}"
                )
            )

        self.root.after(
            500,
            self.update_timer
        )