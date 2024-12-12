import sys
import argparse

from pathlib import Path
from collections import deque

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation

DAY = 10


class DayTenSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.grid = [list(map(int, line)) for line in self.file.splitlines()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def is_in_bounds(self, x, y):
        """Check if a position is within the bounds of the grid."""
        return 0 <= x < self.rows and 0 <= y < self.cols

    def calculate_score(self, start_x, start_y):
        """Perform BFS from a trailhead and calculate its score."""
        queue = deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])
        score = 0

        while queue:
            x, y = queue.popleft()

            if self.grid[x][y] == 9:
                score += 1

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if (
                    self.is_in_bounds(nx, ny)
                    and (nx, ny) not in visited
                    and self.grid[nx][ny] == self.grid[x][y] + 1
                ):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return score

    def calculate_rating(self, start_x, start_y):
        """Perform BFS from a trailhead and calculate its rating."""
        queue = deque([(start_x, start_y, [])])
        visited_trails = set()

        while queue:
            x, y, path = queue.popleft()
            new_path = path + [(x, y)]

            if self.grid[x][y] == 9:
                visited_trails.add(tuple(new_path))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    self.is_in_bounds(nx, ny)
                    and (nx, ny) not in new_path
                    and self.grid[nx][ny] == self.grid[x][y] + 1
                ):
                    queue.append((nx, ny, new_path))

        return len(visited_trails)

    def p1(self):
        """Calculate the sum of scores of all trailheads."""
        total_score = 0

        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] == 0:
                    total_score += self.calculate_score(x, y)

        return total_score

    def p2(self):
        """Calculate the sum of ratings of all trailheads."""
        total_rating = 0

        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] == 0:
                    total_rating += self.calculate_rating(x, y)

        return total_rating


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
        solution = DayTenSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
