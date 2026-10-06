## Plan: Tkinter Minesweeper

Build a small, modular Python Minesweeper application. Keep the game rules independent of Tkinter so they can be tested with deterministic boards; let the GUI translate clicks into game actions and display the resulting state.

**Steps**
1. **Create the project structure and baseline.** Add a `minesweeper_project/` root with `minesweeper/` source package, `examples/`, `tests/`, and `data/`, plus a README describing setup and launch. Use Python's standard-library `unittest`; Tkinter is generally included with Python and does not need a pip dependency.
2. **Implement difficulty configuration and board logic.** In `minesweeper/config.py`, define Beginner (9 rows x 9 columns, 10 mines), Intermediate (16 x 16, 40 mines), and Expert (16 rows x 30 columns, 99 mines). In `minesweeper/board.py`, represent cells by row and column, generate a mine layout, calculate adjacent-mine counts, reveal cells, iteratively expand connected zero-count cells, toggle flags, and detect when every safe cell is revealed. Allow tests to supply fixed mine positions.
3. **Implement game state and scoring.** In `minesweeper/game.py`, coordinate board actions and statuses (ready, playing, won, lost, given up). Count each newly revealed safe cell once as the score. Start elapsed-time measurement on the first reveal and freeze it at any end state. Ignore actions that are invalid after game end; flags do not reveal cells or change score.
4. **Build the Tkinter interface.** In `minesweeper/gui.py`, render a button grid sized to the selected difficulty, show score and elapsed time, bind left click to reveal and right click to flag, and provide a Settings menu for the three presets. Refresh only the affected display state after actions where practical. Schedule timer display updates with Tk's `after` loop rather than a background thread.
5. **Complete game flows and application entry point.** Show a game-over view for wins, mine hits, and Give Up, including final score and elapsed time. Give Up reveals all mines and ends the game. Add Play Again to start a fresh board at the current difficulty and Exit to close the application. Put window creation and launch in `minesweeper/app.py` (also callable as a package entry point if desired).
6. **Add examples, fixtures, tests, and usage notes.** Put small deterministic board fixtures in `data/` for examples/tests, not as runtime requirements. Keep `examples/` for a minimal launch or fixed-board demonstration. Add focused model/game tests and document launching, controls, difficulty sizes, and the score definition in `README.md`.

**Relevant components**
- `minesweeper/config.py` — named difficulty settings and dimensions/mine counts.
- `minesweeper/board.py` — grid data, mine placement, neighbor counts, reveal/flood-fill, flags, and safe-cell completion detection.
- `minesweeper/game.py` — turn rules, score, timer state, and terminal outcomes; no Tk widget code.
- `minesweeper/gui.py` — Tkinter widgets, menu, input bindings, rendering, timer refresh, and end screen.
- `minesweeper/app.py` — application startup and initial window creation.
- `tests/` — unit tests for board and game behavior; `data/` — fixed board cases; `examples/` — runnable usage demonstration.

**Verification**
1. Run `python -m unittest discover -s tests` from `minesweeper_project/` after each model/game phase.
2. Test configuration dimensions and mine totals, neighbor counts at edges/corners, revealing numbered cells, zero-cell expansion, flag toggle behavior, score deduplication, loss, win detection, and Give Up using fixed mine layouts.
3. Launch the GUI and manually verify each difficulty's grid shape, left/right clicks, score/timer updates, timer start/stop, all three end conditions, Play Again reset, and Exit.

**Decisions**
- Interpret Expert `30x16` as 30 columns by 16 rows; model dimensions are rows and columns, so the grid supports rectangular boards despite the general `N x N` wording.
- Score is the count of uniquely revealed safe cells, a simple and testable interpretation of the requested counter.
- Keep mine generation and rules in the model; use a fixed-mine setup only for deterministic tests/examples. No persistence, hints, animations, leaderboard, or advanced scoring are in scope.
- The plan only; no Python code is to be written at this stage.
