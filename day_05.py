def part_2():
    with open("day05.txt") as f:
        pic_lines = []
        instruction_lines = []
        in_instruction = False
        for line in f.readlines():
            if not in_instruction:
                if "1" in line:
                    in_instruction = True
                    continue
                pic_lines.append(line.replace(" ", "-").strip())

            else:
                instruction_lines.append(line.strip())

    cols = [[] for _ in pic_lines[-1]]

    for line in pic_lines[::-1]:
        for i, col in enumerate([x for i, x in enumerate(line) if i % 4 == 1]):
            if col != "-":
                cols[i].append(col)

    instructions = []

    for line in instruction_lines[::-1]:
        if line:
            instructions.append([int(i) for i in line.split() if i.isnumeric()])

    while instructions:
        number, _from, to = instructions.pop()
        cols[_from - 1], stack = cols[_from - 1][:-number], cols[_from - 1][-number:]
        cols[to - 1].extend(stack)

    print("".join(col[-1] for col in cols if col))


def part_1():
    with open("day05.txt") as f:
        pic_lines = []
        instruction_lines = []
        in_instruction = False
        for line in f.readlines():
            if not in_instruction:
                if "1" in line:
                    in_instruction = True
                    continue
                pic_lines.append(line.replace(" ", "-").strip())

            else:
                instruction_lines.append(line.strip())

    cols = [[] for _ in pic_lines[-1]]

    for line in pic_lines[::-1]:
        for i, col in enumerate([x for i, x in enumerate(line) if i % 4 == 1]):
            if col != "-":
                cols[i].append(col)

    instructions = []

    for line in instruction_lines[::-1]:
        if line:
            instructions.append([int(i) for i in line.split() if i.isnumeric()])

    while instructions:
        number, _from, to = instructions.pop()
        for _ in range(number):
            cols[to - 1].append(cols[_from - 1].pop())

    print("".join(col[-1] for col in cols if col))


if __name__ == '__main__':
    # part_1()
    part_2()
