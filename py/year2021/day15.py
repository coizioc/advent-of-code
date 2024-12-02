from collections import defaultdict
import heapq
import itertools
from typing import List, Tuple

with open("input/year2021/day15.txt", "r") as f:
    lines = f.read().splitlines()


def add_to_map(val, n):
    for _ in range(n):
        val += 1
        if val == 10:
            val = 1
    return val


def get_neighbours(
    risk_map: List[List[int]], point: Tuple[int, int]
) -> List[Tuple[int, int]]:
    i, j = point
    neighbours = []
    if j > 0:
        neighbours.append((i, j - 1))
    if j < len(risk_map[i]) - 1:
        neighbours.append((i, j + 1))
    if i > 0:
        neighbours.append((i - 1, j))
    if i < len(risk_map) - 1:
        neighbours.append((i + 1, j))
    return neighbours


def get_smallest_risk(risk_map: List[List[int]]):
    adjacencies = defaultdict(list)
    for i, j in itertools.product(range(len(risk_map)), range(len(risk_map[0]))):
        for n in get_neighbours(risk_map, (i, j)):
            adjacencies[(i, j)].append(n)

    queue = []
    visited = set()
    dist = {}
    for v in adjacencies:
        dist[v] = 0 if v == (0, 0) else 1e100
        heapq.heappush(queue, (dist[v], v))
    while len(queue) > 0:
        u_dist, u = heapq.heappop(queue)
        for v in adjacencies[u]:
            if not v in visited:
                visited.add(v)
                new_dist = u_dist + risk_map[v[0]][v[1]]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(queue, (dist[v], v))
    return dist[(len(risk_map) - 1, len(risk_map[0]) - 1)]


map1 = [[int(i) for i in row] for row in lines]
map2 = []
for _ in range(5):
    map2.extend([5 * [int(i) for i in row] for row in lines])

for x, y in itertools.product(range(5), range(5)):
    for i, j in itertools.product(range(len(map1)), range(len(map1[0]))):
        current_value = map2[i + x * len(map1)][j + y * len(map1[i])]
        map2[i + x * len(map1)][j + y * len(map1[i])] = add_to_map(current_value, x + y)

print(get_smallest_risk(map1))
print(get_smallest_risk(map2))
