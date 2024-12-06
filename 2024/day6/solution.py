import sys
import argparse
import threading

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation, snowfall_progress


DAY = 6


class DaySixSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.grid = [list(line) for line in self.file.splitlines()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        # Guard's initial position and direction
        self.guard_pos = None
        self.guard_dir = None
        self.directions = {
            "^": (-1, 0),  # Up
            ">": (0, 1),  # Right
            "v": (1, 0),  # Down
            "<": (0, -1),  # Left
        }
        self.turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell in self.directions:
                    self.guard_pos = (i, j)
                    self.guard_dir = cell

    def is_in_bounds(self, x, y):
        """Check if a position (x, y) is within grid bounds."""
        return 0 <= x < self.rows and 0 <= y < self.cols

    def simulate_patrol(self, obstruction=None):
        """
        Simulate the guard's patrol.

        Parameters:
            obstruction (tuple): Coordinates of an obstruction to add temporarily.

        Returns:
            history (list): List of visited states (position + direction).
            loop_detected (bool): True if the guard gets stuck in a loop.
        """
        if obstruction:
            ox, oy = obstruction
            self.grid[ox][oy] = "#"

        current_pos = self.guard_pos
        current_dir = self.guard_dir
        visited_states = []
        history = []

        while True:
            state = (current_pos[0], current_pos[1], current_dir)
            if state in visited_states:
                loop_detected = True
                break
            visited_states.append(state)
            history.append(state)

            dx, dy = self.directions[current_dir]
            next_pos = (current_pos[0] + dx, current_pos[1] + dy)

            if not self.is_in_bounds(*next_pos):
                loop_detected = False
                break
            if self.grid[next_pos[0]][next_pos[1]] == "#":
                current_dir = self.turn_right[current_dir]
            else:
                current_pos = next_pos

        if obstruction:
            self.grid[ox][oy] = "."

        return history, loop_detected

    def p1(self):
        """
        Count the number of distinct positions the guard visits during the patrol.
        """
        history, _ = self.simulate_patrol()
        distinct_positions = {(x, y) for x, y, _ in history}
        return len(distinct_positions)

    def p2(self):
        """
        Count the number of valid positions where an obstruction causes a loop.
        """
        stop_animation = threading.Event()
        history, _ = self.simulate_patrol()
        visited_positions = list({(x, y) for x, y, _ in history})
        total_positions = len(visited_positions)
        valid_obstructions = 0
        progress = [0]

        def compute_progress():
            return progress[0], total_positions

        animation_thread = threading.Thread(
            target=snowfall_progress,
            args=(20, 50),
            kwargs={
                "progress": compute_progress,
                "context": "Simulating guard positions... ",
                "show_fraction": True,
            },
            daemon=True,
        )
        animation_thread.start()

        try:
            for idx, (x, y) in enumerate(visited_positions):
                _, is_loop = self.simulate_patrol(obstruction=(x, y))
                if is_loop:
                    valid_obstructions += 1

                progress[0] = idx + 1

            return valid_obstructions
        finally:
            stop_animation.set()
            animation_thread.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(f"Day {DAY} Solution")
    parser.add_argument(
        "--part", required=False, default=1, type=int, help="Part (1|2)"
    )
    parser.add_argument(
        "--test", required=False, default="False", type=str, help="Test? (True|False)"
    )
    parser.add_argument(
        "--snow",
        nargs="?",
        const=10,
        type=int,
        help="Make it snow in the terminal! Optionally specify duration in seconds (default: 10).",
    )
    args = parser.parse_args()
    test = True if args.test.lower() == "true" else False

    if args.snow is not None:
        snowfall_animation(duration=args.snow)
    else:
        solution = DaySixSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
