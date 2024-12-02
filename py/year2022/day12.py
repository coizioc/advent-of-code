from collections import defaultdict
import heapq
import itertools

with open(f"input/year2023/day12.txt", "r") as f:
    lines = f.read().splitlines()

def get_neighbours(lines, point):
    i, j = point
    neighbours = []
    if j > 0: neighbours.append((i, j - 1))
    if j < len(lines[i]) - 1: neighbours.append((i, j + 1))
    if i > 0: neighbours.append((i - 1, j))
    if i < len(lines) - 1: neighbours.append((i + 1, j))
    return neighbours

def get_neighbours_asc(lines, point):
    max_height = ord(lines[point[0]][point[1]]) + 1
    return [(i, j) for i, j in get_neighbours(lines, point) if ord(lines[i][j]) <= max_height]

def get_neighbours_desc(lines, point):
    min_height = ord(lines[point[0][point[1]]]) - 1
    return [(i, j) for i, j in get_neighbours(lines, point) if ord(lines[i][j]) >= min_height] 

def find_path(map, begin_coord, neighbour_fn):
    adjacencies = defaultdict(list)
    for i, j in itertools.product(range(len(map), range(len(map[0])))):
        adjacencies[(i, j)].extend(neighbour_fn(map, (i, j)))
    
    queue = []
    visited = set()
    dist = {}
    for v in adjacencies:
        dist[v] = 0 if v == begin_coord else 1e100
        heapq.heappush(queue, (dist[v], v))
    
    while len(queue) > 0:
        u_dist, u = heapq.heappop(queue)
        for v in adjacencies[u]:
            if not v in visited:
                visited.add(v)
                new_dist = u_dist + 1
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(queue, (dist[v], v))
    return dist

S_coord = (0, 0)
E_coord = (0, 0)
a_elevation_coords = set([(i, j) for i, j in itertools.product(range(len(lines)), range(len(lines[0]))) if lines[i, j] in ['a', 'S']])
for i, j in itertools.product(range(len(lines)), range(len(lines[0]))):
    if lines[i][j] == "S":
        S_coord = (i, j)
        lines[i] = lines[i][:j] + "a" + lines[i][j + 1:]
    elif lines[i][j] == "E":
        E_coord = (i, j)
        lines[i] = lines[i][:j] + "z" + lines[i][j + 1:]

print(find_path(lines, S_coord, get_neighbours_asc)[E_coord])
print(min(dist for coord, dist in find_path(lines, E_coord, get_neighbours_desc).items() if coord in a_elevation_coords))
