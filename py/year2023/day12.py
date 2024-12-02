from functools import cache
import re
from typing import Tuple

with open(f"input/year2023/day12.txt", "r") as f:
    lines = f.read().splitlines()

def get_groups(pattern: str):
    return tuple([len(match) for match in re.findall(r"#+", pattern)])

@cache
def find_arrangements(pattern: str, group_lens: Tuple[int]):
    if len(pattern) < sum(group_lens):
        return 0
    if len(pattern) == 0:
        return len(group_lens) == 0
    if len(group_lens) == 0:
        return '#' not in pattern
    
    arrangements = 0
    idx = pattern.find("?")
    if idx == -1:
        return get_groups(pattern) == group_lens

    # Slice before and after the idx of "?":
    pattern_before = pattern[:idx]
    pattern_after = pattern[idx + 1:]

    # Treat missing idx as ".":
    groups_before = get_groups(pattern_before)
    actual_groups_before = group_lens[:len(groups_before)]
    if groups_before == actual_groups_before:
        arrangements += find_arrangements(pattern_after, group_lens[len(groups_before):])
    
    # Treat missing idx as "#":
    groups_before = get_groups(pattern_before + "#")
    actual_groups_before = group_lens[:len(groups_before)]
    if groups_before[:-1] == actual_groups_before[:-1]:
        if groups_before[-1] < actual_groups_before[-1]:
            arrangements += find_arrangements(pattern_before + "#" + pattern_after, group_lens)
        if groups_before[-1] == actual_groups_before[-1] and (not pattern_after or pattern_after[0] != "#"):
            arrangements += find_arrangements(pattern_after[1:], group_lens[len(groups_before):])
    return arrangements

def find_all_arrangements(line: str):
    pattern, group_lens = line.split(" ")
    group_lens = tuple([int(x) for x in group_lens.split(",")])

    return find_arrangements(pattern, group_lens)

p2_lines = []
for line in lines:
    pattern, lens = line.split(" ")
    p2_lines.append(" ".join(["?".join(5 * [pattern]), ",".join(5 * [lens])]))

print(sum([find_all_arrangements(line) for line in lines]))
print(sum([find_all_arrangements(line) for line in p2_lines]))