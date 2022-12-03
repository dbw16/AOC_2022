lower_scores = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}
upper_scores = {s.upper(): lower_scores[s] + 26 for s in lower_scores}
score_dict = lower_scores | upper_scores


def part_1():
    with open("day_03.txt") as f:
        lines = [[char for char in line.strip()] for line in f.readlines()]

    scores = []
    for line in lines:
        second_half_set = set(line[int(len(line)/2):])
        for char in line[:int(len(line)/2)]:
            if char in second_half_set:
                scores.append(score_dict[char])
                break

    print(sum(scores))


def part_2():
    def chunk(lst: list, n:int):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    with open("day_03.txt") as f:
        lines = [[char for char in line.strip()] for line in f.readlines()]

    common_letters = []
    for line_1, line_2, line_3 in chunk(lines, 3):
        common_letters.append(next(set(line_1).intersection(set(line_2)).intersection(line_3).__iter__()))

    print(sum((score_dict[c] for c in common_letters)))

if __name__ == '__main__':
    part_2()