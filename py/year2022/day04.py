with open(f"input/year2022/day04.txt", "r") as f:
    lines = f.read().splitlines()

def contains(a_min, a_max, b_min, b_max):
    return a_min <= b_min and a_max >= b_max or a_min >= b_min and a_max <= b_max

def overlaps(a_min, a_max, b_min, b_max):
    return len(set(range(a_min, a_max + 1)) & set(range(b_min, b_max + 1))) > 0

assignment_pairs_str = [
    ([int(x) for x in a.split("-")], [int(x) for x in b.split("-")])
    for a,b in [line.split(",") for line in lines]
]

print(len([1 for a, b in assignment_pairs_str if contains(*a, *b)]))
print(len([1 for a, b in assignment_pairs_str if overlaps(*a, *b)]))