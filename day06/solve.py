import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_grid


def _parse_grid(grid: list[str]) -> list[list[str]]:
    parsed: list[list[str]] = []

    for line in grid:
        parsed.append(line.split())

    return parsed


def _build_cols1(parsed: list[list[str]]) -> list[list[str]]:
    cols: list[list[str]] = [[] for _ in range(len(parsed[0]))]

    for line in parsed:
        for i, elem in enumerate(line):
            cols[i].append(elem)

    return cols


def _multiply_elements(operands: list[str]) -> int:
    total = 1

    for op in operands:
        total *= int(op)

    return total


def _sum_elements(operands: list[str]) -> int:
    return sum(int(op) for op in operands)


def part1(grid: list[str]):
    parsed = _parse_grid(grid)
    cols = _build_cols1(parsed)

    total = 0
    for col in cols:
        if col[-1] == "*":
            res = _multiply_elements(col[:-1])
            total += res
        else:
            res = _sum_elements(col[:-1])
            total += res

    return total


def _build_cols2(grid: list[str]) -> list[list[list[str]]]:
    cols: list[list[str]] = [[""] for _ in range(len(grid[0]))]
    num_problems = 0

    for line in grid:
        for i, char in enumerate(reversed(line)):
            cols[i] += char

            if char == "+" or char == "*":
                num_problems += 1

    problems: list[list[list[str]]] = [[] for _ in range(num_problems)]

    i = 0
    for col in cols:
        found_digit = any(char.isdigit() for char in col)
        if found_digit:
            problems[i].append(col)
        else:
            i += 1

    return problems


def part2(grid: list[str]) -> int:
    problems = _build_cols2(grid)

    total = 0

    for problem in problems:
        operator = problem[-1][-1]
        operands: list[str] = []
        for operand in problem:
            operands.append("".join(operand))

        operands[-1] = operands[-1][:-1]

        if operator == "+":
            res = _sum_elements(operands)
            total += res
        else:
            res = _multiply_elements(operands)
            total += res

    return total


def main():
    grid = load_grid(False)

    result1 = part1(grid)
    print("Part 1: ", result1)

    result2 = part2(grid)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
