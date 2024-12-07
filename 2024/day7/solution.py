import sys
import argparse
from itertools import product

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

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
        """
        Parse the input into a list of (test_value, numbers) tuples.
        """
        equations = []
        for line in file_content.splitlines():
            test_value, numbers = line.split(": ")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
        return equations

    def _evaluate_with_operators(self, numbers, operators):
        """
        Evaluate the expression left-to-right with the given numbers and operators.
        """
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == "+":
                result += numbers[i + 1]
            elif operator == "*":
                result *= numbers[i + 1]
        return result

    def _is_valid_equation(self, test_value, numbers):
        """
        Check if any combination of operators can produce the test_value.
        """
        num_slots = len(numbers) - 1  # Number of operator slots
        for operator_combination in product(["+", "*"], repeat=num_slots):
            if (
                self._evaluate_with_operators(numbers, operator_combination)
                == test_value
            ):
                return True
        return False

    def p1(self):
        """
        Compute the total calibration result for valid equations.
        """
        total_calibration_result = 0
        for test_value, numbers in self.equations:
            if self._is_valid_equation(test_value, numbers):
                total_calibration_result += test_value
        return total_calibration_result

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
    args = parser.parse_args()
    test = True if args.test.lower() == "true" else False

    solution = DaySevenSolution2024(test=test)
    if args.part == 1:
        result = solution.p1()
    elif args.part == 2:
        result = solution.p2()
    else:
        raise ValueError("Invalid part specified. Use -part 1 or -part 2.")

    display_result(DAY, args.part, result)
