with open(f"input/year2022/day01.txt", "r") as f:
    lines = f.read().splitlines()

elves = []
elf = []
for line in lines:
    if line == "":
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

elves = sorted([sum(elf) for elf in elves])

print(elves[-1])
print(sum(elves[-3:]))
