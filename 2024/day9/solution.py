import sys
import argparse
import threading

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result
from utils.animations import snowfall_animation, snowfall_progress

DAY = 9

end_loading = threading.Event()
loading = threading.Thread(
    target=snowfall_progress,
    args=(20, 50),
    kwargs={
        "context": "Rearranging amphipod files and eliminating fragmentation... please stand by. ",
        "show_fraction": True,
    },
    daemon=True,
)


class DayNineSolution2024:
    input = "input.txt"
    test_input = "test_input.txt"

    def __init__(self, test=False):
        self.file = (
            open(self.test_input, "r").read() if test else open(self.input, "r").read()
        )
        self.line = self.file.strip()

    def _parse_disk_map(self, line):
        """
        Parse the disk map line into a list of blocks.
        Each pair of digits: (file_length, free_length).
        file_length > 0 => add that many blocks with current file_id
        free_length > 0 => add that many free blocks (-1)

        Returns: A list of integers representing the disk:
                 -1 = free block
                 >=0 = file_id block
        """
        disk = []
        file_id = 0
        digits = list(map(int, line.strip()))

        i = 0
        while i < len(digits):
            file_len = digits[i]
            i += 1
            free_len = 0
            if i < len(digits):
                free_len = digits[i]
                i += 1

            if file_len > 0:
                disk.extend([file_id] * file_len)
                file_id += 1

            if free_len > 0:
                disk.extend([-1] * free_len)

        return disk

    def _find_file_positions(self, disk, file_id):
        """
        Find the contiguous positions of the given file_id in the disk.
        Return start_index, end_index (inclusive).
        If file does not exist (no blocks), return None.
        """
        # Since the original format guarantees contiguous blocks of a file,
        # just find min and max indices.
        positions = [i for i, b in enumerate(disk) if b == file_id]
        if not positions:
            return None
        return min(positions), max(positions)

    def _find_free_runs(self, disk, end_idx):
        """
        Find all free runs (continuous sequences of -1) that end strictly before end_idx.
        Return a list of tuples (start, length) for each free run found to the LEFT of end_idx.
        """
        runs = []
        start = None
        for i in range(end_idx):
            if disk[i] == -1:
                if start is None:
                    start = i
            else:
                if start is not None:
                    runs.append((start, i - start))
                    start = None
        if start is not None:
            runs.append((start, end_idx - start))
        return runs

    def _move_whole_file(self, disk, file_id):
        """
        Attempt to move the file with the given file_id according to the rules:
        - Identify the file's current block range.
        - Find a free run to the left that fits the entire file.
        - If found, move the file blocks there.
        - If not, do nothing.
        """
        file_pos = self._find_file_positions(disk, file_id)
        if file_pos is None:
            return
        start_idx, end_idx = file_pos
        file_length = end_idx - start_idx + 1

        free_runs = self._find_free_runs(disk, start_idx)
        suitable_runs = [r for r in free_runs if r[1] >= file_length]

        if not suitable_runs:
            return

        # the leftmost is just the first suitable run in order.
        suitable_runs.sort(key=lambda x: x[0])
        run_start, run_len = suitable_runs[0]

        file_blocks = disk[start_idx : end_idx + 1]

        for i in range(file_length):
            disk[run_start + i] = file_blocks[i]

        for i in range(start_idx, end_idx + 1):
            disk[i] = -1

    def _compact_disk(self, disk):
        """
        Compact the disk according to the problem:
        Move the rightmost file block to the leftmost free block repeatedly until no free block is to the left of a file block.
        """
        while True:
            try:
                left_free_idx = disk.index(-1)
            except ValueError:
                # No free block at all
                break

            right_file_idx = -1
            for i in range(len(disk) - 1, left_free_idx, -1):
                if disk[i] != -1:
                    right_file_idx = i
                    break

            if right_file_idx == -1:
                # No file block to the right of this free block -> no rearrangement possible
                break

            disk[left_free_idx] = disk[right_file_idx]
            disk[right_file_idx] = -1

            # loop continues until no more moves are needed.

        return disk

    def _compute_checksum(self, disk):
        """
        Compute the checksum:
        sum over (index * file_id) for each file block
        skip free blocks (-1)
        """
        checksum = 0
        for i, block in enumerate(disk):
            if block != -1:
                checksum += i * block
        return checksum

    def p1(self):
        loading.start()
        try:
            line = self.file.strip()
            disk = self._parse_disk_map(line)
            disk = self._compact_disk(disk)
            checksum = self._compute_checksum(disk)
            return checksum
        finally:
            end_loading.set()
            loading.join()

    def p2(self):
        loading.start()
        try:
            disk = self._parse_disk_map(self.line)
            max_file_id = (
                max(b for b in disk if b >= 0) if any(b >= 0 for b in disk) else -1
            )

            for fid in range(max_file_id, -1, -1):
                self._move_whole_file(disk, fid)

            checksum = self._compute_checksum(disk)
            return checksum
        finally:
            end_loading.set()
            loading.join()


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
        solution = DayNineSolution2024(test=test)
        if args.part == 1:
            result = solution.p1()
        elif args.part == 2:
            result = solution.p2()
        else:
            raise ValueError("Invalid part specified. Use --part 1 or --part 2.")
        display_result(DAY, args.part, result)
