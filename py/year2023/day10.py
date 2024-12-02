from collections import defaultdict
import heapq
from itertools import product
from typing import Callable, Dict, List, Tuple

with open(f"input/year2023/day10.txt", "r") as f:
    lines = f.read().splitlines()

adjacencies_map: Dict[str, Callable[[int, int], List[Tuple[int, int]]]] = {
    "|": lambda i, j: [(i - 1, j), (i + 1, j)],
    "-": lambda i, j: [(i, j - 1), (i, j + 1)],
    "L": lambda i, j: [(i - 1, j), (i, j + 1)],
    "J": lambda i, j: [(i - 1, j), (i, j - 1)],
    "7": lambda i, j: [(i + 1, j), (i, j - 1)],
    "F": lambda i, j: [(i + 1, j), (i, j + 1)],
    ".": lambda i, j: [],
}

big_pipe_map = {
    "|": [".|.", ".|.", ".|."],
    "-": ["...", "---", "..."],
    "L": [".|.", ".L-", "..."],
    "J": [".|.", "-J.", "..."],
    "7": ["...", "-7.", ".|."],
    "F": ["...", ".F-", ".|."],
    ".": ["...", "...", "..."],
}

def replace_in_str(s: str, replacement: str, idx: int): return s[:idx] + replacement + s[idx + len(replacement):]

def create_big_map(map):
    big_map = 3 * [line + line + line for line in map]
    for i, j in product(range(len(map)), range(len(map[0]))):
        for n, replacement in enumerate(big_pipe_map[map[i][j]]):
            big_map[3 * i + n] = replace_in_str(big_map[3 * i + n], replacement, 3 * j)
    return big_map

def get_inside(map, loop_coords):
    all_visited = set()
    loop_coords_set = set(loop_coords)
    min_pipe_x, min_pipe_y = (
        min(loop_coords)[0],
        min(loop_coords, key=lambda x: x[1])[1],
    )
    max_pipe_x, max_pipe_y = (
        max(loop_coords)[0],
        max(loop_coords, key=lambda x: x[1])[1],
    )
    for i, j in product(
        range(min_pipe_x + 1, max_pipe_x), range(min_pipe_y + 1, max_pipe_y)
    ):
        if (i, j) not in all_visited and (i, j) not in loop_coords_set:
            visited = set(all_visited)
            queue = [(i, j)]
            while len(queue) > 0:
                u = queue.pop()
                x, y = u
                if not (-1 < x < len(map) and -1 < y < len(map[0])):
                    break
                if u not in visited:
                    queue.extend(
                        [
                            neighbour
                            for neighbour in [
                                (x - 1, y),
                                (x + 1, y),
                                (x, y - 1),
                                (x, y + 1),
                            ]
                            if neighbour not in loop_coords_set
                        ]
                    )
                    visited.add(u)
            if len(queue) == 0:
                return visited
            all_visited |= visited
    return set()

def get_pipe_from_adjacencies(lines, i, j):
    connections = set([(a, b) for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if (i, j) in set(adjacencies_map[lines[a][b]](a, b))])
    for adj, pipe in [[set(adj_fn(i, j)), pipe] for pipe, adj_fn in adjacencies_map.items()]:
        if adj == connections:
            return pipe
    else:
        raise ValueError(i, j)

def find_path(map, begin_coord, adjacencies_map: Dict[str, Callable[[int, int], List[Tuple[int, int]]]]):
    adjacencies = defaultdict(list)
    for i, j in product(range(len(map)), range(len(map[0]))):
        adjacencies[(i, j)].extend(adjacencies_map[map[i][j]](i, j))

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
                if v in dist and new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(queue, (dist[v], v))
    return dist

def get_s_coord(map):
    for i, j in product(range(len(map)), range(len(map[0]))):
        if map[i][j] == "S":
            map[i] = replace_in_str(map[i], get_pipe_from_adjacencies(map, i, j), j)
            return (i, j)
    raise ValueError("No S coord in input")

def get_pipe_coords(map, S_coord):
    dists = find_path(map, S_coord, adjacencies_map)
    return [(loc, dist) for loc, dist in dists.items() if dist != 1e100]

S_coord = get_s_coord(lines)
loop_coords_and_dists = get_pipe_coords(lines, S_coord)
loop_coords = [loc for loc in loop_coords_and_dists]
print(max(loop_coords_and_dists, key=lambda x: x[1])[1])

big_map = create_big_map(lines)
big_loop_coords = [loc[0] for loc in get_pipe_coords(big_map, (3 * S_coord[0] + 1, 3 * S_coord[1] + 1))]
inside_coords = get_inside(big_map, big_loop_coords)
print(len([1 for i, j in product(range(len(lines)), range(len(lines[0]))) if (3 * i + 1, 3 * j + 1) in inside_coords]))
