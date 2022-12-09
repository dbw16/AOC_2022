import datetime
import functools
import typing as t


def part_2() -> int:
    with open("day04.txt") as f:
        lines = (
            tuple(
                map(
                    lambda l: tuple(map(int, l)),
                    map(functools.partial(str.split, sep="-"), line.strip().split(",")),
                )
            )
            for line in f.readlines()
        )

    def over_lapping(a: t.Sequence, b: t.Sequence) -> bool:
        # we want a to always start before b
        if a[0] > b[0]:
            return over_lapping(b, a)
        return not a[1] < b[0]

    return sum([over_lapping(line[0], line[1]) for line in lines])


def part_1() -> int:
    with open("day04.txt") as f:
        lines = (
            tuple(
                map(
                    lambda l: tuple(map(int, l)),
                    map(functools.partial(str.split, sep="-"), line.strip().split(",")),
                )
            )
            for line in f.readlines()
        )

    count = 0
    for line in lines:
        a = line[0]
        b = line[1]
        if a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]:
            count += 1

    return count


if __name__ == "__main__":
    print(part_1())
    print(part_2())
