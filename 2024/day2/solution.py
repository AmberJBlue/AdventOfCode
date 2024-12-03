import sys
import argparse
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

DAY = 2

class DayTwoSolution2024:
    input = 'input.txt'
    test_input = 'test_input.txt'

    def __init__(self, test=False):
        self.file = open(self.test_input, 'r').read() if test else open(self.input, 'r').read()
        self.reports = [list(map(int, line.split())) for line in self.file.splitlines()]

    def p1(self):
        """
        Counts the number of safe reports based on the given criteria:
        - All levels are either increasing or decreasing.
        - Adjacent levels differ by at least 1 and at most 3.
        """
        def is_safe(report):
            diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
            increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
            decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
            valid_diffs = all(1 <= diff <= 3 for diff in diffs)
            return (increasing or decreasing) and valid_diffs

        return sum(1 for report in self.reports if is_safe(report))

    def p2(self):
        """
        Counts the number of safe reports with the Problem Dampener applied:
        - A single level can be removed from an unsafe report to make it safe.
        """
        def is_safe(report):
            diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
            increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
            decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
            valid_diffs = all(1 <= diff <= 3 for diff in diffs)
            return (increasing or decreasing) and valid_diffs

        def is_safe_with_removal(report):
            if is_safe(report):
                return True
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    return True
            return False

        return sum(1 for report in self.reports if is_safe_with_removal(report))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=False, default=1, type=int, help='Part (1/2)')
    parser.add_argument('-test', required=False, default="False", type=str, help='Test mode (True/False)')
    args = parser.parse_args()
    test = True if args.test.lower() == 'true' else False

    solution = DayTwoSolution2024(test=test)
    if args.part == 1:
        result = solution.p1()
    elif args.part == 2:
        result = solution.p2()
    else:
        raise ValueError("Invalid part specified. Use -part 1 or -part 2.")

    display_result(DAY, args.part, result)
