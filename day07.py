from collections import defaultdict
from itertools import accumulate
LIMIT = 100000


def part_01():
    with open("day_07.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    # parse file into dict of dicts
    dir_to_size,  dir_stack= defaultdict(int), []
    for line in lines:
        if line.startswith('$'):
            if 'cd' in line:
                if ".." in line:
                    dir_stack.pop()
                else:
                    dir_stack.append(line.split()[-1])
        elif not line.startswith("dir"):
            for full_path in accumulate(dir_stack):
                dir_to_size[full_path] += int(line.split()[0])

    return sum([size for dir, size in dir_to_size.items() if size < LIMIT])

def part_02():
    with open("day_07.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    # parse file into dict of dicts
    dir_to_size,  dir_stack= defaultdict(int), []
    for line in lines:
        if line.startswith('$'):
            if 'cd' in line:
                if ".." in line:
                    dir_stack.pop()
                else:
                    dir_stack.append(line.split()[-1])
        elif not line.startswith("dir"):
            for full_path in accumulate(dir_stack):
                dir_to_size[full_path] += int(line.split()[0])

    needed_size = 30000000 - (70000000 - dir_to_size["/"])
    for dir in sorted(dir_to_size, reverse=True):
        if dir_to_size[dir] > needed_size:
            return dir_to_size[dir]


if __name__ == '__main__':
    print(part_01())
    print(part_02())
