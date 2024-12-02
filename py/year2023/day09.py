import functools
from typing import List

with open(f"input/year2023/day09.txt", "r") as f:
    lines = f.read().splitlines()

histories = [[int(x) for x in line.split(" ")] for line in lines]

def get_diffs(history: List[int]):
    return [b - a for a, b in zip(history, history[1:])]

def next_value(history: List[int], idx=-1, reduce_func=lambda x, y : y + x):
    diffs = [history, get_diffs(history)]
    while not all([x == 0 for x in diffs[-1]]):
        diffs.append(get_diffs(diffs[-1]))
    return functools.reduce(reduce_func, [diff[idx] for diff in list(reversed(diffs))])

print(sum(next_value(history) for history in histories))
print(sum(next_value(history, 0, reduce_func=lambda x, y : y - x) for history in histories))
