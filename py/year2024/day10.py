import itertools


with open("input/year2024/day10.txt", "r") as f:
    lines = f.read().splitlines()


def get_neighbours(lines, i, j):
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < len(lines) - 1:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < len(lines[i]) - 1:
        neighbours.append((i, j + 1))
    return [
        neighbour
        for neighbour in neighbours
        if int(lines[neighbour[0]][neighbour[1]]) == int(lines[i][j]) + 1
    ]


def get_trailhead_score(lines, start_i, start_j, count_distinct=False):
    visited = set()
    stack = [(start_i, start_j)]
    trailhead_score = 0
    while len(stack) > 0:
        i, j = stack.pop()
        if count_distinct or (i, j) not in visited:
            visited.add((i, j))
            if lines[i][j] == "9":
                trailhead_score += 1
            else:
                stack.extend(get_neighbours(lines, i, j))
    return trailhead_score


sum_trailhead_scores = 0
sum_trailhead_ratings = 0
for i, j in itertools.product(range(len(lines)), range(len(lines[0]))):
    if lines[i][j] == "0":
        sum_trailhead_scores += get_trailhead_score(lines, i, j)
        sum_trailhead_ratings += get_trailhead_score(lines, i, j, count_distinct=True)

print(sum_trailhead_scores)
print(sum_trailhead_ratings)
