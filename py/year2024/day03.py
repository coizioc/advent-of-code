import re

with open("input/year2024/day03.txt", "r") as f:
    lines = f.read().splitlines()


def get_total_mul(code, handle_enable=False):
    total = 0
    enabled = True
    for line in code:
        matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", line)

        for match in matches:
            if match.startswith("do()"):
                enabled = True
            elif match.startswith("don't"):
                enabled = False
            elif not handle_enable or enabled:
                a, b = re.findall(r"mul\((\d+),(\d+)\)", match)[0]
                total += int(a) * int(b)

    return total


print(get_total_mul(lines, False))
print(get_total_mul(lines, True))
