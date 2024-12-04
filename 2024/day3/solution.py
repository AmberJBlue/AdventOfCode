import sys
import argparse
import re
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

DAY = 3

class DayThreeSolution2024:
    input = 'input.txt'
    test_input = 'test_input.txt'

    def __init__(self, test=False):
        self.file = open(self.test_input, 'r').read() if test else open(self.input, 'r').read()
        self.memory = self.file.strip()

    def p1(self):
        """
        Scans the corrupted memory for valid mul(X,Y) instructions,
        calculates the result for each, and returns the total sum.
        """
        # Regular expression to match valid `mul(X,Y)` instructions
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, self.memory)
        # Calculate the result of each valid instruction and sum them up
        total = sum(int(x) * int(y) for x, y in matches)
        return total

    def p2(self):
        """
        Part 2: Processes `mul(X,Y)` instructions with conditional `do()` and `don't()` logic applied.
        """
        pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
        matches = re.findall(pattern, self.memory)

        enabled = True
        total = 0

        for match in matches:
            if "do()" in match[0]:
                enabled = True
            elif "don't()" in match[0]:
                enabled = False
            elif "mul" in match[0] and enabled:
                x, y = int(match[1]), int(match[2])
                total += x * y

        return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Day 3 Solution')
    parser.add_argument('-part', required=False, default=1, type=int, help='Part (1|2)')
    parser.add_argument('-test', required=False, default="False", type=str, help='Test? (True|False)')
    args = parser.parse_args()
    test = True if args.test.lower() == 'true' else False

    solution = DayThreeSolution2024(test=test)
    if args.part == 1:
        result = solution.p1()
    elif args.part == 2:
        result = solution.p2()
    else:
        raise ValueError("Invalid part specified. Use -part 1 or -part 2.")

    display_result(DAY, args.part, result)
