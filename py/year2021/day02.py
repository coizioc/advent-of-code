
with open("input/year2021/day02.txt", 'r') as f:
    lines = f.read().splitlines()

depth = 0
xpos = 0
for line in lines:
    magnitude = int(line[-1])
    if line[0] == "f":
        xpos += magnitude
    elif line[0] == "u":
        depth -= magnitude
    elif line[0] == "d":
        depth += magnitude

print(depth * xpos)

aim = 0
depth = 0
xpos = 0
for line in lines:
    magnitude = int(line[-1])
    if line[0] == "f":
        xpos += magnitude
        depth += aim * magnitude
    elif line[0] == "u":
        aim -= magnitude
    elif line[0] == "d":
        aim += magnitude

print(depth * xpos)