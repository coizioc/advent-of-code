with open(f"input/year2023/day14.txt", "r") as f:
    lines = f.read().splitlines()

lines = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

NUM_CYCLES = 1_000_000_000
cycle_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
rocks = []
walls = set(
    [(-1, i) for i in range(len(lines[0]))]
    + [(len(lines), i) for i in range(len(lines[0]))]
    + [(i, -1) for i in range(len(lines))]
    + [(i, len(lines[0])) for i in range(len(lines))]
)
max_height = len(lines)

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            walls.add((i, j))
        if c == "O":
            rocks.append((i, j))
rocks = sorted(rocks)

prev_rocks = {str(rocks): -1}
for i in range(4 * NUM_CYCLES):
    if i % 250_000 == 0:
        print(i)
    vx, vy = cycle_dirs[i % 4]
    rocks_to_check = set([*rocks])
    while True:
        # any_rocks_changed = False
        # for i, j in set(rocks):
        #     # print(rocks)
        #     for k in range(i, -1, -1):
        #         if (k, j) in walls or (k, j) in rocks:
        #             # print(i, j, k, rocks)
        #             rocks.remove((i, j))
        #             rocks.add((k + 1, j))
        #             any_rocks_changed = True
        #             break
        # if not any_rocks_changed:
        #     break

        new_rocks = sorted([(i + vx, j + vy) if (i + vx, j + vy) not in walls and (i + vx, j + vy) not in rocks else (i, j) for i, j in rocks_to_check])
        if rocks == new_rocks:
            break
        rocks = new_rocks
    if str(rocks) in prev_rocks:
        print(i, prev_rocks[str(rocks)])
    prev_rocks[str(rocks)] = i

load = 0
for i in range(len(lines)):
    # print(i, [rock for rock in rocks if rock[0] == i])
    load += (max_height - i) * len([rock for rock in rocks if rock[0] == i])

print(load)