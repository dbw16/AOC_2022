from collections import deque
from dataclasses import dataclass
import typing as t
import operator
import numpy as np

operation_dict = {"*": operator.mul, "+": operator.add}


@dataclass
class Monkey:
    items: t.Optional[deque] = None
    operation: t.Optional[t.Callable[int, int]] = None
    test: t.Optional[t.Callable[int, bool]] = None
    test_val: t.Optional[int] = None
    test_true: t.Optional[int] = None
    test_false: t.Optional[int] = None
    inspection_count = 0

    @classmethod
    def from_text_block(cls, text_block: str) -> "Monkey":
        monkey = cls()

        for line in text_block.splitlines():
            if "Starting items: " in line:
                monkey.items = deque(
                    map(int, map(str.strip, line.split(":")[-1].split(",")))
                )
            elif "Operation:" in line:
                line = line.split(":")[-1].strip()
                split_line = line.split()
                if split_line[2] == "old" and split_line[4] == "old":
                    monkey.operation = lambda x: operation_dict[split_line[3]](x, x)
                elif split_line[2] == "old":
                    monkey.operation = lambda x: operation_dict[split_line[3]](
                        x, int(split_line[4])
                    )
                elif split_line[4] == "old":
                    monkey.operation = lambda x: operation_dict[split_line[3]](
                        int(split_line[2], x)
                    )
                else:
                    raise ValueError("could not decode operation line")
            elif "Test:" in line:
                number = [int(n) for n in line.split() if n.isnumeric()][-1]
                monkey.test = lambda x: x % number == 0
                monkey.test_val = number
            elif "If true:" in line:
                monkey.test_true = [int(n) for n in line.split() if n.isnumeric()][-1]
            elif "If false:" in line:
                monkey.test_false = [int(n) for n in line.split() if n.isnumeric()][-1]

        return monkey


def part_1() -> int:
    n_rounds = 20
    with open("day_08.txt") as f:
        monkeys = [Monkey.from_text_block(chunk) for chunk in f.read().split("\n\n")]

    for _ in range(n_rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspection_count += 1
                item = monkey.operation(monkey.items.popleft())
                item = item // 3
                if monkey.test(item):
                    monkeys[monkey.test_true].items.append(item)
                else:
                    monkeys[monkey.test_false].items.append(item)

    return int(np.prod(sorted([m.inspection_count for m in monkeys], reverse=True)[:2]))


def part_2() -> int:
    n_rounds = 10000
    with open("day_08.txt") as f:
        monkeys = [Monkey.from_text_block(chunk) for chunk in f.read().split("\n\n")]

    common_factor = int(
        np.prod([m.test_val for m in monkeys])
    )  # be careful with the type returned by np.prod

    for _ in range(n_rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspection_count += 1
                item = monkey.operation(monkey.items.popleft())
                item = item % common_factor
                if monkey.test(item):
                    monkeys[monkey.test_true].items.append(item)
                else:
                    monkeys[monkey.test_false].items.append(item)

    return int(np.prod(sorted([m.inspection_count for m in monkeys], reverse=True)[:2]))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
