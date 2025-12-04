from utils import *


def test_load_grid():
    grid = load_grid(True)
    print(grid)
    return grid


def test_find_neighbours8(grid):
    """grid = [
        "123",
        "456",
        "789",
    ]"""

    neighbours = find_neighbours8(grid, 2, 2)
    print(neighbours)


def main():
    grid = test_load_grid()
    test_find_neighbours8(grid)


if __name__ == "__main__":
    main()
