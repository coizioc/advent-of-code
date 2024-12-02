from collections import defaultdict
import functools
import itertools

with open(f"input/year2023/day02.txt", "r") as f:
    lines = f.read().splitlines()

check_game = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

games = [itertools.chain(*[[dice.split(" ") for dice in round.split(", ")] for round in line.split(": ")[1].split("; ")]) for line in lines]

ids = []
powers = []
for i, game in enumerate(games):
    rolls = defaultdict(list)
    for number, color in game:
        rolls[color].append(int(number))
    if all(check_game[color] >= max(values) for color, values in rolls.items()):
        ids.append(i + 1)
    min_possible = { color: max(values) for color, values in rolls.items()}
    powers.append(functools.reduce(lambda x, y: x * y, min_possible.values(), 1))

print(sum(ids))
print(sum(powers))
