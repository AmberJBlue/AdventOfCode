import sys
import argparse
from itertools import product

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

DAY = 4


class DayFourSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.word = "XMAS"
        self.directions = list(product([-1, 0, 1], [-1, 0, 1]))
        self.grid = [list(line) for line in self.file.splitlines()]
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        self.found = 0

    def p1(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == self.word[0]:
                    for x, y in self.directions:
                        if x == y == 0:
                            continue
                        if all(
                            0 <= row + letter * x < self.rows
                            and 0 <= col + letter * y < self.cols
                            and self.grid[row + letter * x][col + letter * y]
                            == self.word[letter]
                            for letter in range(len(self.word))
                        ):
                            self.found += 1
        return self.found

    def p2(self):
        word = self.word[1:]
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                if self.grid[row][col] == self.word[2]:
                    criss = (
                        self.grid[row - 1][col - 1]
                        + self.grid[row][col]
                        + self.grid[row + 1][col + 1]
                    )
                    cross = (
                        self.grid[row - 1][col + 1]
                        + self.grid[row][col]
                        + self.grid[row + 1][col - 1]
                    )
                    if criss in [word, word[::-1]] and cross in [word, word[::-1]]:
                        self.found += 1
        return self.found


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Day 4 Solution")
    parser.add_argument("-part", required=False, default=1, type=int, help="Part (1|2)")
    parser.add_argument(
        "-test", required=False, default="False", type=str, help="Test? (True|False)"
    )
    args = parser.parse_args()
    test = True if args.test.lower() == "true" else False

    solution = DayFourSolution2024(test=test)
    if args.part == 1:
        result = solution.p1()
    elif args.part == 2:
        result = solution.p2()
    else:
        raise ValueError("Invalid part specified. Use -part 1 or -part 2.")

    display_result(DAY, args.part, result)
