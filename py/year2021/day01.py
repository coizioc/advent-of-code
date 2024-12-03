with open("input/year2021/day01.txt", 'r') as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines]

num_increases = 0
for i, b in zip(lines, lines[1:]):
    if b - i > 0:
        num_increases += 1

print(num_increases)

num_increases = 0
for i in range(0, len(lines) - 3):
    aaa = lines[i] + lines[i + 1] + lines[i + 2]
    bbb = lines[i + 1] + lines[i + 2] + lines[i + 3]
    if bbb - aaa > 0:
        num_increases += 1

print(num_increases)