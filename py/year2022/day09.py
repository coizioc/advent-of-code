import itertools


with open("input/year2022/day09.txt", "r") as f:
    lines = f.read().splitlines()

def get_neighbours(cube):
    return itertools.product(*[[cube[i] - 1, cube[i], cube[i] + 1] for i in range(len(cube))])

sign = lambda x : 0 if x == 0 else int(x / abs(x))

def rope(directions, n_knots):
    knots = n_knots * [(0, 0)]
    tail_visited = set([(knots[0])])

    for line in directions:
        direction, n_times = line.split(" ")
        v_head = (0, 0)
        if direction == "R":
            v_head = (0, 1)
        if direction == "L":
            v_head = (0, -1)
        if direction == "U":
            v_head = (-1, 0)
        if direction == "D":
            v_head = (1, 0)
        for _ in range(int(n_times)):
            knots[-1] = (knots[-1][0] + v_head[0], knots[-1][1] + v_head[1])
            for i in range(len(knots) - 1, 0, -1):
                if not knots[i - 1] in get_neighbours(knots[i]):
                    dist_vec = (knots[i][0] - knots[i - 1][0], knots[i][1] - knots[i - 1][1])
                    knots[i - 1] = (knots[i - 1][0] + sign(dist_vec[0]), knots[i - 1][1] + sign(dist_vec[1]))
            tail_visited.add(knots[0])
    return tail_visited

print(len(rope(lines, 2)))
print(len(rope(lines, 10)))