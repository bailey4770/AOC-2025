import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid


def part1(grid):
    return


def part2(grid):
    return


def main():
    grid = load_grid(True)

    result1 = part1(grid)
    print("Part 1: ", result1)

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
