def part_1():
    with open("day1.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    groups = []
    group = []
    for line in lines:
        if not line:
            groups.append(sum([int(num) for num in group]))
            group = []
            continue
        group.append(line)
    return max(groups)


def part_1_refactor():
    with open("day1.txt") as f:
        groups = [map(int, group.split("\n")) for group in f.read().split("\n\n")]
    return max([sum(group) for group in groups])


def part_2():
    with open("day1.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    groups = []
    group = []
    for line in lines:
        if not line:
            groups.append(sum([int(num) for num in group]))
            group = []
            continue
        group.append(line)
    return sum(sorted(groups, reverse=True)[:3])


def part_2_refactor():
    with open("day1.txt") as f:
        groups = [map(int, group.split("\n")) for group in f.read().split("\n\n")]
    return sum(sorted([sum(group) for group in groups], reverse=True)[:3])


if __name__ == "__main__":
    print(part_2_refactor())
