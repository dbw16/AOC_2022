from collections import deque
M = f"\033[91m#\033[0m"


def part_1():
    with open("day_10.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    que = deque()
    cycle = 1
    register_count = 1
    results = []
    cycles = {20 + 40 * i for i in range(0, 100)}
    for line in lines:
        if "noop" in line:
            if que:
                register_count += que.pop()
            cycle += 1
            if cycle in cycles:
                results.append(cycle * register_count)
            print(f"after cycle {cycle} the count is {register_count}")
        elif "addx" in line:
            size = int(line.split()[-1])
            que.appendleft(0)
            que.appendleft(size)
            if que:
                register_count += que.pop()
            cycle += 1
            if cycle in cycles:
                results.append(cycle * register_count)
            print(f"after cycle {cycle} the count is {register_count}")
            if que:
                register_count += que.pop()
            cycle += 1
            if cycle in cycles:
                results.append(cycle * register_count)
            print(f"after cycle {cycle} the count is {register_count}")
    print(sum(results))


def part_2():
    with open("day_10.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    que = deque()
    cycle = 1
    register_count = 1
    cycle_to_reg = dict()
    for line in lines:
        if "noop" in line:
            if que:
                register_count += que.pop()
            cycle += 1
            cycle_to_reg[cycle] = register_count
        elif "addx" in line:
            size = int(line.split()[-1])
            que.appendleft(0)
            que.appendleft(size)
            if que:
                register_count += que.pop()
            cycle += 1
            cycle_to_reg[cycle] = register_count
            if que:
                register_count += que.pop()
            cycle += 1
            cycle_to_reg[cycle] = register_count

    cycle_to_reg[1] = 1
    for row in range(0, cycle // 40):
        for pixel in range(40):
            cycle_n = pixel + 1 + row * 40
            sprite_center = cycle_to_reg[cycle_n]
            if pixel in range(sprite_center-1, sprite_center+2):
                print(M, end="")
            else:
                print(" ", end="")
        print("")


if __name__ == '__main__':
    part_2()
