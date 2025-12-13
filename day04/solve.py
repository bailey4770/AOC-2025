import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import find_neighbours8, load_grid


def part1(grid: list[str]):
    total = 0

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char != "@":
                continue

            neighbours = find_neighbours8(grid, row, col)
            num_neighbours = sum(1 for r, c in neighbours if grid[r][c] == "@")
            if num_neighbours < 4:
                total += 1

    return total


def _search_and_remove(
    grid: list[str], removed: set[tuple[int, int]], total: int
) -> int:
    round_total = 0
    to_remove: set[tuple[int, int]] = set()

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char != "@" or (row, col) in removed:
                continue

            neighbours = find_neighbours8(grid, row, col)
            num_neighbours = sum(
                1 for r, c in neighbours if grid[r][c] == "@" and (r, c) not in removed
            )

            if num_neighbours < 4:
                round_total += 1
                to_remove.add((row, col))

    removed.update(to_remove)
    if round_total == 0:
        return total
    else:
        return _search_and_remove(grid, removed, total + round_total)


def part2(grid: list[str]):
    total = 0
    removed: set[tuple[int, int]] = set()

    return _search_and_remove(grid, removed, total)


def main():
    grid = load_grid(False)

    result1 = part1(grid)
    print(result1)

    result2 = part2(grid)
    print(result2)


if __name__ == "__main__":
    main()
