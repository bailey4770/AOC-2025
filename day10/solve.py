import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid
import math
import itertools as it
import functools as ft


def _parse_grid1(grid: list[str]):
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


def part1(grid: list[str]):
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

    lights, buttons = _parse_grid1(grid)

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


def _parse_grid2(grid: list[str]):
    all_buttons: list[list[set[int]]] = [[] for _ in range(len(grid))]
    all_joltage_requirements: list[list[int]] = []

    for i, line in enumerate(grid):
        for parts in line.split():
            if parts.startswith("("):
                buttons = set(map(int, parts[1:-1].split(",")))
                all_buttons[i].append(buttons)

            elif parts.startswith("{"):
                requirements = list(map(int, parts[1:-1].split(",")))
                all_joltage_requirements.append(requirements)

    return all_buttons, all_joltage_requirements


def find_button_cost(buttons: list[set[int]], joltage_requirements: tuple[int, ...]):
    def parity_pattern(t: tuple[int, ...]):
        return tuple(v % 2 for v in t)

    def effect(buttons: tuple[set[int], ...]):
        return tuple(
            # total effect on i column
            sum(i in button for button in buttons)
            # for i = 0 to length of joltage columns
            for i in range(len(joltage_requirements))
        )

    button_combos = [
        combo for n in range(len(buttons) + 1) for combo in it.combinations(buttons, n)
    ]
    button_patterns = {
        k: list(v)
        for k, v in it.groupby(
            sorted(button_combos, key=lambda combo: parity_pattern(effect(combo))),
            key=lambda combo: parity_pattern(effect(combo)),
        )
    }

    # can achieve slight speed up - pure function so we can reuse results for each input.
    @ft.cache
    def cost(current_joltage: tuple[int, ...]):
        current_pattern = parity_pattern(current_joltage)

        if not any(current_joltage):
            return 0
        elif any(j < 0 for j in current_joltage):
            return math.inf
        elif current_pattern not in button_patterns.keys():
            return math.inf

        min_cost = math.inf
        for combo in button_patterns[current_pattern]:
            resulting_joltage = tuple(
                (jr - pp) // 2 for jr, pp in zip(current_joltage, effect(combo))
            )
            min_cost = min(min_cost, len(combo) + 2 * cost(resulting_joltage))

        return min_cost

    return cost(joltage_requirements)


def part2(grid: list[str]):
    """
    Major credit to https://www.reddit.com/user/Kache/ and his python solution.
    Mine is altered for improved readability and to facilitate my own understanding.
    But would not have been able to solve without his solution as guide.

    Key insights:
    - use parity patterning to match which buttons to press
    - by halving the problem, we turn it into to O(log(n))
    - itertools has very handy pre-built combinations and groupby functions
    """
    all_buttons, all_joltage_requirements = _parse_grid2(grid)

    total = 0
    for i in range(len(grid)):
        buttons = all_buttons[i]
        joltage_requirements = tuple(all_joltage_requirements[i])

        total += find_button_cost(buttons, joltage_requirements)

    return total


def main():
    grid = load_grid(False)

    result1 = part1(grid)
    print("Part 1: ", result1)

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
