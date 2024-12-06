import sys
import argparse
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation

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

        self.guard_pos = None
        self.guard_dir = None
        self.covered_areas = set()
        self.directions = {
            "^": (-1, 0),  # Up
            ">": (0, 1),  # Right
            "v": (1, 0),  # Down
            "<": (0, -1),  # Left
        }
        self.turn_order = ["^", ">", "v", "<"]

        for i, row in enumerate(self.grid):
            for j, char in enumerate(row):
                if char in self.directions:
                    self.guard_pos = (i, j)
                    self.guard_dir = char

    def is_in_bounds(self, x, y):
        """Check if a position (x, y) is within the bounds of the grid."""
        return 0 <= x < self.rows and 0 <= y < self.cols

    def move_guard(self):
        """Simulate one step of the guard's movement."""
        x, y = self.guard_pos
        dx, dy = self.directions[self.guard_dir]
        next_x, next_y = x + dx, y + dy

        if self.is_in_bounds(next_x, next_y) and self.grid[next_x][next_y] != "#":
            self.guard_pos = (next_x, next_y)
        else:
            current_index = self.turn_order.index(self.guard_dir)
            self.guard_dir = self.turn_order[(current_index + 1) % 4]

        self.covered_areas.add(self.guard_pos)

    def p1(self):
        """Simulate the guard's patrol and count distinct visited positions."""
        self.covered_areas.add(self.guard_pos)

        while True:
            x, y = self.guard_pos
            dx, dy = self.directions[self.guard_dir]
            next_x, next_y = x + dx, y + dy
            if not self.is_in_bounds(next_x, next_y):
                break
            self.move_guard()

        return len(self.covered_areas)

    def p2(self):
        """Placeholder for Part 2 logic."""
        return "Part 2 solution not implemented yet."


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
