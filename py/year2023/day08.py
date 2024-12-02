import math
from typing import Callable, Dict, List, Tuple

with open(f"input/year2023/day08.txt", "r") as f:
    lines = f.read().splitlines()

directions = lines[0]
get_direction = lambda step: 0 if directions[step % len(directions)] == "L" else 1

nodes: Dict[str, Tuple[str, str]] = {}
for line in lines[2:]:
    from_node, to_nodes = line.split(" = ")
    nodes[(from_node, 0)], nodes[(from_node, 1)] = to_nodes[1:-1].split(", ")

def get_cycle_lens(nodes: Dict[str, Tuple[str, str]], start_nodes: List[str], end_condition: Callable[[str], bool]):
    cycle_lens = len(start_nodes) * [0]
    for i, start_node in enumerate(start_nodes):
        step = 0
        curr_node = start_node
        while not end_condition(curr_node):
            curr_node = nodes[(curr_node, get_direction(step))]
            step += 1
        cycle_lens[i] = step
    return cycle_lens

print(get_cycle_lens(nodes, ["AAA"], lambda node: node == "ZZZ")[0])
print(math.lcm(*get_cycle_lens(nodes, [node for node, _ in nodes if node.endswith("A")], lambda node: node.endswith("Z"))))
