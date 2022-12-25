from collections import defaultdict
from numpy import base_repr


SNAFU_DIGITS_TO_INT: dict[str, int] = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
BASE_5_TO_SNAFU_DIGITS: dict[str, tuple[str, str]] = {
    "-2": ("0", "="),
    "-1": ("0", "-"),
    "0": ("0", "0"),
    "1": ("0", "1"),
    "2": ("0", "2"),
    "3": ("1", "="),
    "4": ("1", "-"),
    "5": ("1", "0"),
}


def snafu_sum(vals: list[str]) -> tuple[str, str]:
    return BASE_5_TO_SNAFU_DIGITS[str(sum((SNAFU_DIGITS_TO_INT[s] for s in vals)))]


def int_to_snafu(base_10: int) -> str:
    base_5: str = base_repr(base_10, 5)
    # 124030
    # convert base 5 to snafu left to right 0->0, 3-> 5-2 -> 1=, 0->0, 4->5-1 -> 1-, 2 -> 2, 1->1 and smash em together
    place_to_vals: dict[int, list[str]] = defaultdict(list)

    for n_th, i in enumerate(reversed(base_5)):
        n_plus_1, n = BASE_5_TO_SNAFU_DIGITS[i]
        place_to_vals[n_th].append(n)
        if n_plus_1:
            place_to_vals[n_th + 1].append(n_plus_1)

    result = []
    for i in list(place_to_vals):
        n_plus_1, n = snafu_sum(place_to_vals[i])
        result.append(n)
        if n_plus_1:
            place_to_vals[i + 1].append(n_plus_1)

    return "".join(reversed(result)).lstrip("0")


def snafu_to_int(s: str) -> int:
    return sum((SNAFU_DIGITS_TO_INT[c] * 5**i for i, c in enumerate(reversed(s))))


def main():
    with open("day_25.txt") as f:
        snafu_vals = [vals.strip() for vals in f.readlines()]

    total_fuel: int = sum((snafu_to_int(s) for s in snafu_vals))
    print(int_to_snafu(total_fuel))


if __name__ == "__main__":
    main()
