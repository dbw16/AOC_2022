from operator import mul
from functools import reduce


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


def part_1():
    with open("day_08.txt") as f:
        grid_y_x = [[[int(i), "_"] for i in line.strip()] for line in f.readlines()]

    # we will only look west -> east and rotate the grid
    found = dict()
    count = 0
    for _ in range(4):
        for y, row in enumerate(grid_y_x):
            max_height = 0
            for x, tree in enumerate(row):
                if int(tree[0]) > max_height or x == 0:
                    if tree[1] != "-":
                        tree[1] = "-"
                        count += 1
                max_height = max(max_height, tree[0])

        grid_y_x = rotated(grid_y_x)

    return count


# 30373
# 25512
# 65332
# 33549
# 35390


def calculate_score(*, x, y, grid) -> int:
    value = grid[y][x]
    print(f"im starting on x={x} y={y} {value}")
    scores = []

    # right
    count = 0
    _max = -1
    print("looking right")
    for i in range(x + 1, len(grid[0])):
        count += 1
        print(f" seeing {grid[y][i]}")
        if grid[y][i] >= value:
            print(f"total count {count}")
            break
        _max = grid[y][i]
    else:
        print(f"total count {count}")
    scores.append(count)

    # left
    count = 0
    _max = -1
    print("looking left")
    for i in range(x - 1, -1, -1):
        count += 1
        print(f" seeing {grid[y][i]}")
        if grid[y][i] >= value:
            print(f"total count {count}")
            break
        _max = grid[y][i]
    else:
        print(f"total count {count}")
    scores.append(count)

    # up
    count = 0
    _max = -1
    print("looking up")
    for j in range(y - 1, -1, -1):
        count += 1
        print(f" seeing {grid[j][x]}")
        if grid[j][x] >= value:
            print(f"total count {count}")
            break
        _max = grid[j][x]
    else:
        print(f"total count {count}")
    scores.append(count)

    # down
    count = 0
    _max = -1
    print("looking down")
    for j in range(y + 1, len(grid)):
        count += 1
        print(f" seeing {grid[j][x]}")
        if grid[j][x] >= value:
            print(f"total count {count}")
            break
        _max = grid[j][x]
    else:
        print(f"total count {count}")
    scores.append(count)

    return reduce(mul, scores)


def part_2():
    with open("day_08.txt") as f:
        grid_y_x = [[int(i) for i in line.strip()] for line in f.readlines()]

    score = 0
    for y, row in enumerate(grid_y_x):
        for x, tree in enumerate(row):
            score = max(score, calculate_score(x=x, y=y, grid=grid_y_x))

    return score


if __name__ == "__main__":
    print(part_1())
    print(part_2())
