import sys
import argparse

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation

DAY = -1


class DayTEMPSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )

    def p1(self):
        """Placeholder for Part 1 logic."""
        return "Part 1 solution not implemented yet."

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
        solution = DayTEMPSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
