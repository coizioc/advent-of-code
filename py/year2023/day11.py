from itertools import product

with open(f"input/year2023/day11.txt", "r") as f:
    lines = f.read().splitlines()

no_galaxy_rows = set([i for i, row in enumerate(lines) if all(x == "." for x in row)])
no_galaxy_cols = set([i for i, col in enumerate(zip(*lines)) if all(x == "." for x in col)])
galaxies = [(i, j) for i, j in product(range(len(lines)), range(len(lines[0]))) if lines[i][j] == "#"]

def dist(no_galaxy_rows, no_galaxy_cols, expand_dist, galaxy_1, galaxy_2):
    g1_x, g1_y = galaxy_1
    g2_x, g2_y = galaxy_2

    if g1_x == g2_x and g1_y == g2_y: return 0
    if g1_x > g2_x: g1_x, g2_x = g2_x, g1_x
    if g1_y > g2_y: g1_y, g2_y = g2_y, g1_y

    expand_x = sum(expand_dist - 1 for x in range(g1_x + 1, g2_x) if x in no_galaxy_rows)
    expand_y = sum(expand_dist - 1 for y in range(g1_y + 1, g2_y) if y in no_galaxy_cols)

    return (g2_x - g1_x) + expand_x + (g2_y - g1_y) + expand_y

def get_min_dists_all_pairs(no_galaxy_rows, no_galaxy_cols, galaxies, expand_dist):
    return [dist(no_galaxy_rows, no_galaxy_cols, expand_dist, galaxy_1, galaxy_2) for galaxy_1, galaxy_2 in product(galaxies, galaxies) if galaxy_1 != galaxy_2]

print(sum(get_min_dists_all_pairs(no_galaxy_rows, no_galaxy_cols, galaxies, 2)) // 2)
print(sum(get_min_dists_all_pairs(no_galaxy_rows, no_galaxy_cols, galaxies, 1_000_000)) // 2)
