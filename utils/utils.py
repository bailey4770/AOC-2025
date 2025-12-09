def load_grid(test: bool):
    file_name = "test_input.txt" if test else "input.txt"

    with open(file_name, "r") as f:
        return f.read().splitlines()


def load_coordinates(test: bool) -> list[tuple[int, int, int]]:
    file_name = "test_input.txt" if test else "input.txt"

    with open(file_name, "r") as f:
        lines = f.read().splitlines()

    coordinates: list[tuple[int, int, int]] = []
    for line in lines:
        parts = line.split(",")
        curr: tuple[int, int, int] = (int(parts[0]), int(parts[1]), int(parts[2]))
        coordinates.append(curr)

    return coordinates


def _find_neighbours(
    grid: list[str], row: int, col: int, dirs: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    neighbours: list[tuple[int, int]] = []

    for d in dirs:
        n_row = row + d[0]
        n_col = col + d[1]

        if (0 <= n_row < len(grid)) and (0 <= n_col < len(grid[0])):
            neighbours.append((n_row, n_col))

    return neighbours


def find_neighbours8(grid: list[str], row: int, col: int) -> list[tuple[int, int]]:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    return _find_neighbours(grid, row, col, dirs)


def find_neighbours4(grid: list[str], row: int, col: int) -> list[tuple[int, int]]:
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return _find_neighbours(grid, row, col, dirs)
