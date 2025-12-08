import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid


def find_start(grid: list[str]) -> int:
    for i, char in enumerate(grid[0]):
        if char == "S":
            return i

    raise IndexError


def part1(grid: list[str]):
    start: int = find_start(grid)
    beam_cols: set[int] = {start}
    split_count = 0

    for row in grid:
        new_beam_cols: set[int] = set()

        for beam_pos in beam_cols:
            if row[beam_pos] == "^":
                split_count += 1
                new_beam_cols.add(beam_pos - 1)
                new_beam_cols.add(beam_pos + 1)
            else:
                new_beam_cols.add(beam_pos)

        beam_cols = new_beam_cols.copy()

    return split_count


def part2(grid: list[str]) -> int:
    from functools import lru_cache

    # number of possible paths to the end from a given spot never changes
    # memoization prevents recalculation of those prefound paths
    #
    # Specifically, lru_cache stores the output for each function with its inputs as keys. Same inputs -> use cached output
    # Therefore, memoization requires pure functions
    # Using nonlocal timeline closure is not valid, since incrementing it is a side effect that requires the function to acc be run

    @lru_cache(None)
    def _timelines_recursion(row_index: int, beam_index: int) -> int:
        for i, row in enumerate(grid[row_index + 1 :]):
            if row[beam_index] == "^":
                left_path = _timelines_recursion(i + row_index + 1, beam_index - 1)
                right_path = _timelines_recursion(i + row_index + 1, beam_index + 1)
                return left_path + right_path

        # reached bottom of graph. One timeline complete
        return 1

    start = find_start(grid)
    return _timelines_recursion(0, start)


def main():
    grid = load_grid(False)

    result1 = part1(grid)
    print("Part 1: ", result1)

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
