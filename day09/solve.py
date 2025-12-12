import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_coordinates
from typing import cast


def _calculate_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    return abs(tile1[0] - tile2[0] + 1) * abs(tile1[1] - tile2[1] + 1)


def part1(red_tiles: list[tuple[int, int]]) -> int:
    largest = 0

    for i, tile1 in enumerate(red_tiles[:-1]):
        for tile2 in red_tiles[i + 1 :]:
            area = _calculate_area(tile1, tile2)
            largest = max(largest, area)

    return largest


def _add_edges(
    red_tiles: list[tuple[int, int]],
) -> tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]]:
    horizontal_edges: list[tuple[int, int, int]] = []
    vertical_edges: list[tuple[int, int, int]] = []

    for i, tile_curr in enumerate(red_tiles):
        tile_prev = red_tiles[i - 1]

        if tile_curr[0] != tile_prev[0]:
            # vertically aligned, not on the same x, must be same y
            edge_start = min(tile_curr[0], tile_prev[0])
            edge_end = max(tile_curr[0], tile_prev[0])
            horizontal_edges.append((tile_curr[1], edge_start, edge_end))
        elif tile_curr[1] != tile_prev[1]:
            # horizontally aligned, not the same y, must be same x
            edge_start = min(tile_curr[1], tile_prev[1])
            edge_end = max(tile_curr[1], tile_prev[1])
            vertical_edges.append((tile_curr[0], edge_start, edge_end))

    return horizontal_edges, vertical_edges


def _valid_corners(
    tile1: tuple[int, int],
    tile2: tuple[int, int],
    vertices: set[tuple[int, int]],
    vertical_edges: list[tuple[int, int, int]],
):
    def _check_corner(
        corner: tuple[int, int], vertical_edges: list[tuple[int, int, int]]
    ):
        point_x, point_y = corner
        inside = False

        for edge in vertical_edges:
            edge_x, edge_y_start, edge_y_end = edge

            if edge_x > point_x:
                if edge_y_start < point_y < edge_y_end:
                    inside = not inside

        return inside

    corners_to_check = [(tile1[0], tile2[1]), (tile1[1], tile2[0])]
    return all(
        corner in vertices or _check_corner(corner, vertical_edges)
        for corner in corners_to_check
    )


def _intersects_edge(
    tile1: tuple[int, int],
    tile2: tuple[int, int],
    vertical_edges: list[tuple[int, int, int]],
    horizontal_edges: list[tuple[int, int, int]],
) -> bool:
    rect_x_start, rect_x_end = min(tile1[0], tile2[0]), max(tile1[0], tile2[0])
    rect_y_start, rect_y_end = min(tile1[1], tile2[1]), max(tile1[1], tile2[1])

    for edge in vertical_edges:
        edge_x, edge_y_start, edge_y_end = edge

        if rect_x_start < edge_x < rect_x_end:
            if edge_y_start < rect_y_end and edge_y_end > rect_y_start:
                return True

    for edge in horizontal_edges:
        edge_y, edge_x_start, edge_x_end = edge

        if rect_y_start < edge_y < rect_y_end:
            if edge_x_start < rect_x_end and edge_x_end > rect_x_start:
                return True

    return False


def part2(red_tiles: list[tuple[int, int]]):
    vertices = set(red_tiles)
    horizontal_edges, vertical_edges = _add_edges(red_tiles)

    largest = 0

    for i, tile1 in enumerate(red_tiles[:-1]):
        for tile2 in red_tiles[i + 1 :]:
            area = _calculate_area(tile1, tile2)

            if area < largest:
                continue

            if _valid_corners(
                tile1, tile2, vertices, vertical_edges
            ) and not _intersects_edge(tile1, tile2, vertical_edges, horizontal_edges):
                largest = max(largest, area)

    return largest


def main():
    coordinates = load_coordinates(False)
    assert len(coordinates[0]) == 2, "Coordinates must be 2D"
    coordinates = cast(list[tuple[int, int]], coordinates)

    result1 = part1(coordinates)
    print("Part 1: ", result1)

    result2 = part2(coordinates)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
