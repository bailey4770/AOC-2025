import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid


def _parse_input(grid: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges: list[tuple[int, int]] = []
    ingredients: list[int] = []
    found_separator = False

    for line in grid:
        if line == "":
            found_separator = True
            continue

        if not found_separator:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ingredients.append(int(line))

    return ranges, ingredients


def part1(grid: list[str]):
    ranges, ingredients = _parse_input(grid)

    fresh = 0
    for ingr in ingredients:
        # any returns True if any of the elements in a list is truthy
        # stops checking as soon as it finds a truthy value
        # exactly the same outcome and performance as manually looping to check
        if any(start <= ingr <= end for start, end in ranges):
            fresh += 1

    return fresh


def _combine_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # if we pre-sort the ranges, then we only need to deal with overlap in one direction
    sorted_ranges = sorted(ranges)
    combined = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = combined[-1]

        if current_start <= last_end + 1:
            combined[-1] = (last_start, max(last_end, current_end))
        else:
            # no overlap
            combined.append((current_start, current_end))

    return combined


def part2(grid: list[str]):
    ranges, _ = _parse_input(grid)
    new_ranges = _combine_ranges(ranges)

    return sum(end + 1 - start for start, end in new_ranges)


def main():
    grid = load_grid(False)

    result1 = part1(grid)
    print("Part 1: ", result1)

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
