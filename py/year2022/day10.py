with open("input/year2022/day10.txt", "r") as f:
    lines = f.read().splitlines()

cycles = 0
events = {}
for line in lines:
    if line.startswith("noop"):
        cycles += 1
    if line.startswith("addx"):
        cycles += 2
        events[cycles] = int(line.split(" ")[1])

def signal_strengh(events, n):
    reg_x = 1 + sum(val for cycle, val in events.items() if cycle < n)
    return n * reg_x

print(sum(signal_strengh(events, cycle) for cycle in range(20, 241, 40)))

x_pos = 1
image = ""
for i in range(cycles):
    if i % 40 == 0 and i != 0:
        image += "\n"
    image += "#" if i % 40 in [x_pos - 1, x_pos, x_pos + 1] else "."

    if i + 1 in events:
        x_pos += events[i + 1]

print(image)