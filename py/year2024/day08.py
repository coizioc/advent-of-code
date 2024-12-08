from collections import defaultdict
import itertools


with open("input/year2024/day08.txt", "r") as f:
    lines = f.read().splitlines()


def get_antinodes_from_pair(x, y, dx, dy, iterations=None):
    antinodes = []
    antinode = (x + dx, y + dy)
    num_iterations = 0
    while (
        0 <= antinode[0] < len(lines)
        and 0 <= antinode[1] < len(lines[0])
        and (iterations is None or num_iterations < iterations)
    ):
        # print(x, y, dx, dy, antinode, iterations, num_iterations)
        antinodes.append(antinode)
        antinode = (antinode[0] + dx, antinode[1] + dy)
        num_iterations += 1
    return antinodes


def get_antinodes(antenna_locations: dict, iterations=None):
    antinodes = set()
    for locations in antenna_locations.values():
        if len(locations) > 1:
            for (ax, ay), (bx, by) in itertools.combinations(locations, 2):
                dx = bx - ax
                dy = by - ay
                antinodes.update(
                    get_antinodes_from_pair(ax, ay, -dx, -dy, iterations)
                    + get_antinodes_from_pair(bx, by, dx, dy, iterations)
                )
    return antinodes


antinodes = set()
antenna_locations = defaultdict(list)

max_x = len(lines)
max_y = len(lines[0])
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] != ".":
            antenna_locations[c].append((i, j))

print(len(get_antinodes(antenna_locations, iterations=1)))
antinodes = get_antinodes(antenna_locations)
# Add all beacon locations where there are at least two beacons.
beacon_locations = set(
    itertools.chain(
        *[locations for locations in antenna_locations.values() if len(locations) > 1]
    )
)
print(len(antinodes | beacon_locations))
