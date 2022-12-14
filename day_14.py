from functools import cache
import time
from numpy import arange

X = 500

def part_1():
    with open("day_13.txt") as f:
        instructions = [[l.strip() for l in line.split(" -> ")] for line in f.readlines()]
    min_x, max_x = int(999999999999999), 0
    min_y, max_y = int(999999999999999), 0
    grid = [["." for _ in range(600)] for _ in range(500)]

    for instruction in instructions:
        for i1, i2 in zip(instruction, instruction[1:]):
            x1, y1 = map(int, i1.split(","))
            x2, y2 = map(int, i2.split(","))
            min_x, max_x = min(min_x, x1, x2),  max(max_x, x1, x2)
            min_y, max_y = min(min_y, y1, y2), max(max_y, y1, y2)
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = "#"
            for y in arange(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = "#"

    # for j in range(min_y-2, max_y + 2):
    #     for i in range(min_x - 2, max_x + 2):
    #         print(grid[j][i], end="")
    #     print("")
    count = -1
    try:
        while True:
            count += 1
            y = 0
            x = X
            while True:
                if grid[y+1][x] == ".":
                    y += 1
                    continue
                else:
                    if grid[y+1][x-1] == ".":
                        x -= 1
                        y += 1
                        continue
                    elif grid[y+1][x+1] == ".":
                        x += 1
                        y += 1
                        continue
                    else:
                        grid[y][x] = "s"
                        break
    except IndexError:
        print(count)

    for j in range(min_y-2, max_y + 2):
        for i in range(min_x - 2, max_x + 2):
            print(grid[j][i], end="")
        print("")

def part_2():
    with open("day_13.txt") as f:
        instructions = [[l.strip() for l in line.split(" -> ")] for line in f.readlines()]
    min_x, max_x = int(999999999999999), 0
    min_y, max_y = int(999999999999999), 0
    grid = [["." for _ in range(2000)] for _ in range(2000)]

    for instruction in instructions:
        for i1, i2 in zip(instruction, instruction[1:]):
            x1, y1 = map(int, i1.split(","))
            x2, y2 = map(int, i2.split(","))
            min_x, max_x = min(min_x, x1, x2),  max(max_x, x1, x2)
            min_y, max_y = min(min_y, y1, y2), max(max_y, y1, y2)
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = "#"
            for y in arange(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = "#"
    max_y += 2
    for x in range(len(grid[0])):
        grid[max_y][x] = "#"

    for j in range(min_y-2, max_y + 2):
        for i in range(min_x - 2, max_x + 2):
            print(grid[j][i], end="")
        print("")

    count = -1
    try:
        while True:
            count += 1
            y = 0
            x = X

            while True:
                if grid[0][500] == "s":
                    raise IndexError

                if grid[y+1][x] == ".":
                    y += 1
                    continue
                else:
                    if grid[y+1][x-1] == ".":
                        x -= 1
                        y += 1
                        continue
                    elif grid[y+1][x+1] == ".":
                        x += 1
                        y += 1
                        continue
                    else:
                        grid[y][x] = "s"
                        break

            if count == 92:
                pass
    except IndexError:
        print(count)

    print("")
    for j in range(0, max_y + 2):
        for i in range(min_x - 2, max_x + 2):
            print(grid[j][i], end="")
        print("")


if __name__ == '__main__':
    part_2()
