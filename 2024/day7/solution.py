import sys
import argparse
from itertools import product

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation

DAY = 7


class DaySevenSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.equations = self._parse_input(self.file)

    def _parse_input(self, file_content):
        """Parses the input into test values and associated numbers."""
        equations = []
        for line in file_content.splitlines():
            test_value, numbers = line.split(": ")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
        return equations

    def _evaluate_expression(self, numbers, operators):
        """
        Evaluates the expression formed by inserting operators between numbers.
        Evaluates left-to-right regardless of operator precedence.
        """
        result = numbers[0]
        for num, op in zip(numbers[1:], operators):
            if op == "+":
                result += num
            elif op == "*":
                result *= num
            elif op == "||":
                result = int(f"{result}{num}")  # Concatenation
        return result

    def _is_valid_equation(self, test_value, numbers):
        """
        Checks if the test value can be formed by inserting any combination
        of `+`, `*`, and `||` between the numbers.
        """
        num_operators = len(numbers) - 1
        for operators in product(["+", "*", "||"], repeat=num_operators):
            if self._evaluate_expression(numbers, operators) == test_value:
                return True
        return False

    def p1(self):
        """
        Solve Part 1: Determine the total calibration result using only `+` and `*`.
        """
        total = 0
        for test_value, numbers in self.equations:
            if self._is_valid_equation(test_value, numbers):
                total += test_value
        return total

    def p2(self):
        """
        Solve Part 2: Determine the total calibration result using `+`, `*`, and `||`.
        """
        total = 0
        for test_value, numbers in self.equations:
            if self._is_valid_equation(test_value, numbers):
                total += test_value
        return total


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
        solution = DaySevenSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
