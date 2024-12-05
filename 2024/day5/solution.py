import sys
import argparse
from itertools import product

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

DAY = 5


class DayFiveSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.rules, self.updates = self._parse_input(self.file)

        self.rule_graph = self._build_rule_graph(self.rules)

    def _parse_input(self, file_content):
        lines = file_content.strip().split("\n")

        rules = []
        updates = []

        for line in lines:
            if "|" in line:
                rules.append(line)  # Add rules
            elif "," in line:
                updates.append(list(map(int, line.split(","))))  # Parse updates

        return rules, updates

    def _build_rule_graph(self, rules):
        rule_graph = {}
        for rule in rules:
            x, y = map(int, rule.split("|"))
            if x not in rule_graph:
                rule_graph[x] = []
            rule_graph[x].append(y)
        return rule_graph

    def _update_validator(self, update):
        positions = {page: idx for idx, page in enumerate(update)}

        for x in self.rule_graph:
            for y in self.rule_graph[x]:
                if x in positions and y in positions:
                    if positions[x] >= positions[y]:
                        return False

        return True

    def p1(self):
        total = 0

        for update in self.updates:
            if self._update_validator(update):
                print(update[len(update) // 2])
                total += update[len(update) // 2]

        return total

    def p2(self):
        return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(f"Day {DAY} Solution")
    parser.add_argument("-part", required=False, default=1, type=int, help="Part (1|2)")
    parser.add_argument(
        "-test", required=False, default="False", type=str, help="Test? (True|False)"
    )
    args = parser.parse_args()
    test = True if args.test.lower() == "true" else False

    solution = DayFiveSolution2024(test=test)
    if args.part == 1:
        result = solution.p1()
    elif args.part == 2:
        result = solution.p2()
    else:
        raise ValueError("Invalid part specified. Use -part 1 or -part 2.")

    display_result(DAY, args.part, result)
