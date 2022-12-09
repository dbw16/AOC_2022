from numpy import sign
from itertools import chain, accumulate
import typing as t

move_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def pair_add(t_1: t.Sequence[int], t_2: t.Sequence[int]) -> t.Sequence[int]:
    return tuple(map(sum, zip(t_1, t_2)))


def pair_sub(t_1: t.Sequence[int], t_2: t.Sequence[int]) -> t.Sequence[int]:
    return tuple(h - t for h, t in zip(t_1, t_2))


def move(pos, movement) -> t.Sequence[int]:
    return pair_add(pos, move_dict[movement])


def knot_move(head_cord, knot_cord):
    relative_head_cord = pair_sub(head_cord, knot_cord)
    ((low_idx, low_coord), (high_idx, high_coord)) = sorted(enumerate(relative_head_cord), key=lambda x: abs(x[1]))
    movement = [0, 0]
    if abs(high_coord) == 2:
        if abs(low_coord) >= 1:
            movement[low_idx] = sign(low_coord)
        movement[high_idx] = sign(high_coord)
        knot_cord = pair_add(knot_cord, movement)

    return knot_cord


def knot_follow_head(head_cords):
    knot_cord = (0, 0)  # each knot starts at 0, 0
    knot_positions = list()
    for head_cord in head_cords:
        knot_cord = knot_move(head_cord, knot_cord)
        knot_positions.append(knot_cord)
    return knot_positions


def part_n(k_notes: int):
    with open('day09.txt', 'r') as file:
        movements = chain.from_iterable(((line.split()[0]) * int(line.split()[1]) for line in file.readlines()))
    previous_knots_cords = list(accumulate(movements, func=move, initial=(0, 0)))

    # we are going to do one knot at a time following the full path that that knot travels
    for _ in range(k_notes):
        previous_knots_cords = knot_follow_head(previous_knots_cords)

    return len(set(previous_knots_cords))


if __name__ == '__main__':
    print(part_n(k_notes=1))
    print(part_n(k_notes=9))
