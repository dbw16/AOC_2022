from enum import IntEnum
from dataclasses import dataclass

LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6


class Result(IntEnum):
    loss = 0
    draw = 3
    win = 6

    @classmethod
    def from_letter(cls, letter: str) -> "Result":
        if letter in {"x", "X"}:
            return cls.loss
        elif letter in {"Y", "y"}:
            return cls.draw
        elif letter in {"Z", "z"}:
            return cls.win
        else:
            raise ValueError


# maybe should have made a circle linked list
class Move(IntEnum):
    rock = 1
    paper = 2
    scissors = 3

    @classmethod
    def from_letter(cls, letter: str) -> "Move":
        if letter in {"A", "a", "x", "X"}:
            return cls.rock
        elif letter in {"b", "B", "Y", "y"}:
            return cls.paper
        elif letter in {"c", "C", "Z", "z"}:
            return cls.scissors
        else:
            raise ValueError

    def next(self) -> "Move":
        if self == self.rock:
            return self.paper
        elif self == self.paper:
            return self.scissors
        elif self == self.scissors:
            return self.rock

    def last(self) -> "Move":
        if self == self.rock:
            return self.scissors
        elif self == self.paper:
            return self.rock
        elif self == self.scissors:
            return self.paper

    def __gt__(self, move: "Move"):
        if self == self.rock and move == self.scissors:
            return True
        if self == self.scissors and move == self.rock:
            return False
        return self.value > move.value

    def __eq__(self, move: "Move"):
        return self.value == move.value


@dataclass
class Round_2:
    op_move: Move
    result: Result

    def score(self) -> int:
        score = 0
        score += self.result.value
        # now we need to calculate our move base on op_move
        if self.result == Result.draw:
            score += self.op_move.value
        elif self.result == Result.loss:
            score += self.op_move.last().value
        elif self.result == Result.win:
            score += self.op_move.next().value
        return score


@dataclass
class Round_1:
    op_move: Move
    response: Move

    def score(self) -> int:
        score = 0
        if self.op_move == self.response:
            score += DRAW_SCORE
            score += self.response.value
        elif self.op_move > self.response:
            score += LOSS_SCORE
            score += self.response.value
        else:
            score += WIN_SCORE
            score += self.response.value
        return score


def part_1():
    with open("day2.txt") as f:
        rounds = [
            Round_1(Move.from_letter(a), Move.from_letter(b))
            for a, b in map(str.split, f.readlines())
        ]
    return sum(map(Round_1.score, rounds))


def part_2():
    with open("day2.txt") as f:
        rounds = [
            Round_2(Move.from_letter(a), Result.from_letter(b))
            for a, b in map(str.split, f.readlines())
        ]
    return sum(map(Round_2.score, rounds))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
