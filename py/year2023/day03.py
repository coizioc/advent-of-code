import re
from collections import defaultdict
import itertools

with open(f"input/year2023/day03.txt", "r") as f:
    lines = f.read().splitlines()

def get_symbols(lines, i, j):
    neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    return [(x, y) for x, y in neighbors if x in range(len(lines)) and y in range(len(lines[x])) and lines[x][y] not in "0123456789."]

part_nums = []
for i, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    part_nums.extend([(match.group(), i, match.start()) for match in matches])

part_sum = 0
gears = defaultdict(set)
for part_id, row, col in part_nums:
    symbols_in_part = [get_symbols(lines, row, col + i) for i in range(len(part_id))]
    if any(len(symbols) > 0 for symbols in symbols_in_part):
        part_sum += int(part_id)
    
    for x, y in itertools.chain(*symbols_in_part):
        if lines[x][y] == "*":
            gears[(x, y)].add(part_id)

gear_sum = 0
for gear in gears:
    if len(gears[gear]) == 2:
        part_1, part_2 = [int(n) for n in gears[gear]]
        gear_sum += part_1 * part_2

print(part_sum)
print(gear_sum)
