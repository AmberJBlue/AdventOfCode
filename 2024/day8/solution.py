import sys
import argparse
from math import gcd
from itertools import product
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation

DAY = 8


class DayEightSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.lines = self.file.strip("\n").split("\n")
        self.height = len(self.lines)
        self.width = len(self.lines[0]) if self.height > 0 else 0

    def _read_antennas(self):
        """Read the grid and return a dictionary {freq: [(x,y), ...]} of antenna positions."""
        freq_map = {}
        for r in range(self.height):
            for c in range(self.width):
                ch = self.lines[r][c]
                if ch != ".":
                    freq_map.setdefault(ch, []).append((r, c))
        return freq_map

    def _line_id(self, x1, y1, x2, y2):
        """
        Compute a normalized line identifier given two points (x1,y1), (x2,y2).
        Returns (dx', dy', k) where dy'*x - dx'*y = k, with direction normalized.
        """
        dx = x2 - x1
        dy = y2 - y1
        g = gcd(dx, dy)
        dxp = dx // g
        dyp = dy // g

        if dxp < 0:
            dxp = -dxp
            dyp = -dyp
        elif dxp == 0 and dyp < 0:
            dyp = -dyp

        # k: dy'*x - dx'*y = k
        k = dyp * x1 - dxp * y1
        return dxp, dyp, k

    def p1(self):
        """
        For each pair of antennas with the same frequency:
          - Compute two antinodes: P1=2B-A and P2=2A-B
        Return a set of antinode coordinates within the grid.
        """
        freq_map = self._read_antennas()
        antinodes = set()
        for _, antennas in freq_map.items():
            if len(antennas) < 2:
                continue
            for i in range(len(antennas)):
                x1, y1 = antennas[i]
                for j in range(i + 1, len(antennas)):
                    x2, y2 = antennas[j]
                    # Compute antinodes
                    px1, py1 = 2 * x2 - x1, 2 * y2 - y1
                    px2, py2 = 2 * x1 - x2, 2 * y1 - y2
                    if 0 <= px1 < self.height and 0 <= py1 < self.width:
                        antinodes.add((px1, py1))
                    if 0 <= px2 < self.height and 0 <= py2 < self.width:
                        antinodes.add((px2, py2))
        return len(antinodes)

    def p2(self):
        """
        For each frequency, each pair of antennas defines a line on which
        all integer points within the grid are antinodes.

        Steps:
        - Collect all unique lines that have at least two antennas of the same frequency.
        - For each line, enumerate all valid grid points on that line and mark them as antinodes.
        """
        freq_map = self._read_antennas()
        lines_set = set()

        for freq, antennas in freq_map.items():
            if len(antennas) < 2:
                continue
            for i in range(len(antennas)):
                x1, y1 = antennas[i]
                for j in range(i + 1, len(antennas)):
                    x2, y2 = antennas[j]
                    dxp, dyp, k = self._line_id(x1, y1, x2, y2)
                    line_id = (freq, dxp, dyp, k)
                    lines_set.add(line_id)

        antinodes = set()

        # Enumerate all integer points on each line
        for freq, dxp, dyp, k in lines_set:
            if dxp == 0:
                # vertical
                if k % dyp == 0:
                    x = k // dyp
                    if 0 <= x < self.height:
                        for y in range(self.width):
                            antinodes.add((x, y))
            elif dyp == 0:
                # horizontal
                if k % dxp == 0:
                    y = (-k) // dxp
                    if 0 <= y < self.width:
                        for x in range(self.height):
                            antinodes.add((x, y))
            else:
                # general
                for x in range(self.height):
                    numerator = dyp * x - k
                    if numerator % dxp == 0:
                        y = numerator // dxp
                        if 0 <= y < self.width:
                            antinodes.add((x, y))
        return len(antinodes)


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
        solution = DayEightSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
