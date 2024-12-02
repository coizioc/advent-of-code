with open("input/year2022/day25.txt", "r") as f:
    lines = f.read().splitlines()

snafu_to_decimal_digits = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}
decimal_to_snafu_digits = {v: k for k, v in snafu_to_decimal_digits.items()}


def from_snafu(snafu):
    return sum(
        (
            snafu_to_decimal_digits[digit] * 5 ** (len(snafu) - i - 1)
            for i, digit in enumerate(snafu)
        )
    )


def to_snafu(n):
    base_5 = []
    while n > 0:
        base_5.append(n % 5)
        n //= 5
    for i in range(len(base_5)):
        if base_5[i] > 2:
            base_5[i] -= 5
            if i + 1 < len(base_5):
                base_5[i + 1] += 1
            else:
                base_5.append(1)
    return "".join(decimal_to_snafu_digits[digit] for digit in reversed(base_5))


print(to_snafu(sum(from_snafu(x) for x in lines)))
