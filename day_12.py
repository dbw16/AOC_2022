import string
from itertools import chain
import igraph
import typing as t


def tuple_hash(t: t.Sequence[int]) -> str:
    return "-".join([str(i) for i in t])


def part_1():
    letter_to_number = {"S": 0, "E": 25} | {
        c: i for i, c in enumerate(string.ascii_lowercase)
    }
    directions: dict[str, tuple[int, int]] = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }
    start = None
    end = None
    with open("day_12.txt") as f:
        grid_y_x: list[list[tuple[int, int, int]]] = []
        for y, line in enumerate(f.readlines()):
            row = []
            for x, c in enumerate(line.strip()):
                if c == "S":
                    start = tuple_hash((letter_to_number[c], x, y))
                elif c == "E":
                    end = tuple_hash((letter_to_number[c], x, y))
                row.append((letter_to_number[c], x, y))
            grid_y_x.append(row)

    # for row in grid_y_x:
    #     print(row)

    # Build the edges of our graph
    edges = []
    for y, row in enumerate(grid_y_x):
        for x, vertex in enumerate(row):
            for direction in directions.values():
                if not (
                    y + direction[1] < 0
                    or x + direction[0] < 0
                    or y + direction[1] > len(grid_y_x) - 1
                    or x + direction[0] > len(row) - 1
                ):
                    candidate = grid_y_x[y + direction[1]][x + direction[0]]
                    if vertex[0] + 1 >= candidate[0]:
                        edges.append((tuple_hash(vertex), tuple_hash(candidate)))

    g = igraph.Graph(directed=True)
    g.add_vertices([tuple_hash(v) for v in chain.from_iterable(grid_y_x)])
    g.add_edges(edges)

    result = list(chain.from_iterable(g.distances(start, end)))
    if len(result) != 1:
        raise Exception(
            f"something went frong git multple values for distance {result}"
        )
    return result[0]


def part_2():
    letter_to_number = {"S": 0, "E": 25} | {
        c: i for i, c in enumerate(string.ascii_lowercase)
    }
    directions: dict[str, tuple[int, int]] = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }
    starts = []
    end = None
    with open("day_12.txt") as f:
        grid_y_x: list[list[tuple[int, int, int]]] = []
        for y, line in enumerate(f.readlines()):
            row = []
            for x, c in enumerate(line.strip()):
                if c == "S" or c == "a":
                    starts.append(tuple_hash((letter_to_number[c], x, y)))
                elif c == "E":
                    end = tuple_hash((letter_to_number[c], x, y))
                row.append((letter_to_number[c], x, y))
            grid_y_x.append(row)

    # for row in grid_y_x:
    #     print(row)

    # Build the edges of our graph
    edges = []
    for y, row in enumerate(grid_y_x):
        for x, vertex in enumerate(row):
            for direction in directions.values():
                if not (
                    y + direction[1] < 0
                    or x + direction[0] < 0
                    or y + direction[1] > len(grid_y_x) - 1
                    or x + direction[0] > len(row) - 1
                ):
                    candidate = grid_y_x[y + direction[1]][x + direction[0]]
                    if vertex[0] + 1 >= candidate[0]:
                        edges.append((tuple_hash(vertex), tuple_hash(candidate)))

    g = igraph.Graph(directed=True)
    g.add_vertices([tuple_hash(v) for v in chain.from_iterable(grid_y_x)])
    g.add_edges(edges)

    result = []
    for start in starts:
        result.append(list(chain.from_iterable(g.distances(start, end)))[0])

    return min(result)


if __name__ == "__main__":
    print(part_2())
