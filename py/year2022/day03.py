import functools

with open(f"input/year2022/day03.txt", "r") as f:
    lines = f.read().splitlines()

def get_priority(x: str): return ord(x.lower()) - ord("a") + 1 + (26 if x.isupper() else 0)

def get_priority_line(line):
    compartment1, compartment2 = set(line[:len(line) // 2]), set(line[len(line) // 2:])
    both_item = list(compartment1 & compartment2)[0]
    return get_priority(both_item)

def get_priority_group(group):
    all_item = list(functools.reduce(lambda curr, new : curr & set(new), group, set(group[0])))[0]
    return get_priority(all_item)

print(sum([get_priority_line(line) for line in lines]))
print(sum([get_priority_group(group) for group in zip(lines[::3], lines[1::3], lines[2::3])]))
