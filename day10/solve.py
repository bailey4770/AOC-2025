import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid
import math
import time


def parse_grid(grid: list[str]):
    lights: list[int] = []
    lengths: list[int] = []
    buttons: list[list[int]] = [[] for _ in range(len(grid))]

    for i, line in enumerate(grid):
        for parts in line.split():
            if parts.startswith("["):
                binary = parts[1:-1].replace(".", "0").replace("#", "1")
                lengths.append(len(binary))
                lights.append(int(binary, 2))

            elif parts.startswith("("):
                button = set(map(int, parts[1:-1].split(",")))
                length = lengths[i]
                binary = "".join("1" if j in button else "0" for j in range(length))
                buttons[i].append(int(binary, 2))

    return lights, buttons


def part1(lights: list[int], buttons: list[list[int]]):
    def _xor_recursive(
        expected: int,
        actual: int,
        curr_buttons: list[int],
        steps: int,
        start_idx: int,
    ):
        nonlocal least_steps

        for i in range(start_idx, len(curr_buttons)):
            button = curr_buttons[i]
            # must explore option where button is NOT pressed. therefore, store new temp result to check, rather than modify original
            current = actual ^ button
            current_steps = steps + 1

            if current == expected:
                least_steps = min(least_steps, current_steps)
                return
            if current == 0:
                return
            elif current_steps >= least_steps:
                return
            elif len(curr_buttons) == start_idx - 1:
                return

            _xor_recursive(
                expected,
                current,
                curr_buttons,
                current_steps,
                i + 1,
            )

    total = 0
    for i, expected in enumerate(lights):
        least_steps = math.inf
        actual = int("0", 2)

        if actual == expected:
            print("starting as expected")
            continue

        for j in range(len(buttons[i])):
            # by passing an index pointer rather than repeatedly slicing the lists, we reduce time from 45 seconds to less than 0.02 seconds
            _xor_recursive(expected, actual, buttons[i], 0, j)

        # print(f"{i} out of {len(lights)} completed. Min steps: {least_steps}")
        if least_steps == math.inf:
            print(f"error on {i} {bin(expected)}")
        total += least_steps

    return total


def part2(grid):
    return


def main():
    start = time.perf_counter()
    grid = load_grid(False)
    lights, buttons = parse_grid(grid)

    result1 = part1(lights, buttons)
    print("Part 1: ", result1)
    end = time.perf_counter()
    print(f"Time taken {end - start}")

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
