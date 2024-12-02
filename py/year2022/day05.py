import re

with open(f"input/year2022/day05.txt", "r") as f:
    lines = f.read().splitlines()

stack_start_idx = 0
while lines[stack_start_idx].startswith("["):
    stack_start_idx += 1

def parse_stacks(lines, stack_start_idx):
    stacks = [[] for c in lines[stack_start_idx] if c != " "]
    for line in lines[stack_start_idx - 1 :: -1]:
        for i, value in enumerate(line[1::4]):
            if value != " ":
                stacks[i].append(value)
    return stacks

def move_stacks(lines, stack_start_idx, in_order=False):
    stacks = parse_stacks(lines, stack_start_idx)
    instructions = lines[stack_start_idx + 2:]

    for line in instructions:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        stack_number, stack_from_idx, stack_to_idx, = [int(group) for group in match.groups()]

        stack_to_add = []
        for _ in range(stack_number):
            value = stacks[stack_from_idx - 1].pop()
            stack_to_add.append(value)
        if in_order:
            stack_to_add.reverse()
        
        stacks[stack_to_idx - 1].extend(stack_to_add)
    return "".join(stack[-1] for stack in stacks)

print(move_stacks(lines, stack_start_idx))
print(move_stacks(lines, stack_start_idx, in_order=True))
