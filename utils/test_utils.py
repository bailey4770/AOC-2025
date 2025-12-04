from utils import load_grid, find_neighbours8, find_neighbours4


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

    neighbours = find_neighbours8(grid, 1, 1)
    print(neighbours)


def test_find_neighbours4(grid):
    neighbours = find_neighbours4(grid, 1, 1)
    print(neighbours)


def main():
    grid = test_load_grid()
    test_find_neighbours8(grid)
    test_find_neighbours4(grid)


if __name__ == "__main__":
    main()
