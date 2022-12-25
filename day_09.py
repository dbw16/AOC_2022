import copy
import typing
from collections import defaultdict
import itertools
import matplotlib.pyplot as plt

X = f"\033[91mX\033[0m"
T = f"\033[91mT\033[0m"
H = f"\033[91mH\033[0m"


def print_grid(*, g, tx, ty, hx, hy):
    print(
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    )
    for y, line in enumerate(g):
        for x, c in enumerate(line):
            print(c, end="")
            # continue
            # if y==ty and x==tx:
            #     print(T,end="")
            # elif x==hx and y== hy:
            #     print(H,end="")
            # else:
            #     print(c, end="")
        print("")
    print(
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    )


def part1():
    letter_count = defaultdict(int)
    instructions = []
    with open("day09.txt") as f:
        for letter, number in [line.strip().split() for line in f.readlines()]:
            instructions.append((letter, number))
            letter_count[letter] += int(number)

    grid_size = 10000
    # not very memory efficient to keep tail pos's on a grid but it makes frawing the pic easy....
    grid = [["-" for _ in range(grid_size)] for _ in range(grid_size)]
    hx = grid_size // 2
    hy = grid_size // 2
    tx = grid_size // 2
    ty = grid_size // 2
    grid[tx][ty] = X

    for direction, number in instructions:
        for i in range(int(number)):
            # print_grid(g=grid, hx=hx, hy=hy, tx=tx, ty=ty)
            if direction == "U":
                hy -= 1
                if abs(hy - ty) <= 1:
                    continue
                tx = hx
                ty -= 1
            if direction == "D":
                hy += 1
                if abs(hy - ty) <= 1:
                    continue
                tx = hx
                ty += 1
                pass
            if direction == "L":
                hx -= 1
                if abs(hx - tx) <= 1:
                    continue
                ty = hy
                tx -= 1
            if direction == "R":
                hx += 1
                if abs(hx - tx) <= 1:
                    continue
                ty = hy
                tx += 1
            grid[ty][tx] = X

    return sum((1 for i in itertools.chain.from_iterable(grid) if i == X))


if __name__ == "__main__":
    part1()
