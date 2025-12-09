import sys
from pathlib import Path

# Add parent directory to path so we can import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.utils import load_coordinates

import heapq


class UnionFind:
    def __init__(self):
        self.parent: dict[tuple[int, int, int], tuple[int, int, int]] = dict()
        self.size: dict[tuple[int, int, int], int] = dict()
        self.rank: dict[tuple[int, int, int], int] = dict()

    def find(self, box: tuple[int, int, int]) -> tuple[int, int, int]:
        parent = self.parent[box]

        if parent != box:
            # flattens everytime we call find
            self.parent[box] = self.find(parent)
        return self.parent[box]

    def union(self, box1: tuple[int, int, int], box2: tuple[int, int, int]):
        root1 = self.find(box1)
        root2 = self.find(box2)

        if root1 == root2:
            # roots are the same, so two boxes are already in the same tree
            return

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            self.rank[root2] += 1

    def sort(self):
        roots: set[tuple[int, int, int]] = set()

        for parent in self.parent.values():
            roots.add(self.find(parent))

        return sorted(roots, key=lambda root: self.size[root], reverse=True)


def _calculate_distances(coordinates: list[tuple[int, int, int]]):
    # instead of dictionary relating pairs of coordinates to distances
    # we can build a min-heap of all distances. This auto-sorts distances as we add them
    # rather than comparing every single item with each other, it simply ensures that parent < children
    # therefore, the head is always the smallest item in the list. when we pop the head, the smallest of the children becomes the new head.
    # this saves us huge numbers of comparisons, and hence computation time
    distances: list[tuple[int, tuple[int, int, int], tuple[int, int, int]]] = []

    for i, box1 in enumerate(coordinates[:-1]):
        for box2 in coordinates[i + 1 :]:
            # Euclidean distance is always sqrt of sum of squares
            # however, relative order of distances is preserved without sqrt. this saves computation
            distance = (
                ((box1[0] - box2[0]) ** 2)
                + ((box1[1] - box2[1]) ** 2)
                + ((box1[2] - box2[2]) ** 2)
            )
            distances.append((distance, box1, box2))

    return distances


def part1(coordinates: list[tuple[int, int, int]], num_connections: int):
    distances = _calculate_distances(coordinates)

    # heapify can ensure smallest element is always popped from head in O(n) time.
    heapq.heapify(distances)

    uf = UnionFind()
    for box in coordinates:
        uf.parent[box] = box
        uf.size[box] = 1
        uf.rank[box] = 0

    for _ in range(num_connections):
        _, box1, box2 = heapq.heappop(distances)
        uf.union(box1, box2)

    sorted_circuits = uf.sort()
    result = (
        uf.size[sorted_circuits[0]]
        * uf.size[sorted_circuits[1]]
        * uf.size[sorted_circuits[2]]
    )
    return result


def part2(coordinates: list[tuple[int, int, int]]):
    distances = _calculate_distances(coordinates)
    heapq.heapify(distances)

    uf = UnionFind()
    for box in coordinates:
        uf.parent[box] = box
        uf.size[box] = 1
        uf.rank[box] = 0

    while True:
        _, box1, box2 = heapq.heappop(distances)
        uf.union(box1, box2)
        root = uf.find(box1)

        if uf.size[root] == len(coordinates):
            break

    return box1[0] * box2[0]


def main():
    test = False
    coordinates = load_coordinates(test)

    num_connections = 10 if test else 1000
    result1 = part1(coordinates, num_connections)
    print("Part 1: ", result1)

    result2 = part2(coordinates)
    print("Part 2: ", result2)


if __name__ == "__main__":
    main()
