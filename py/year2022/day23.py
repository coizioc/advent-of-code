from collections import defaultdict
import itertools
from typing import List, Tuple

with open("input/year2022/day23.txt", "r") as f:
    lines = f.read().splitlines()

RULES = [
    ([(-1, -1), (0, -1), (1, -1)], (0, -1)),
    ([(-1, 1), (0, 1), (1, 1)], (0, 1)),
    ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
    ([(1, 1), (1, 0), (1, -1)], (1, 0)),
]


def get_neighbours(x: int, y: int):
    neighbours = set(
        [(x + i, y + j) for i, j in itertools.product(range(-1, 2), range(-1, 2))]
    )
    neighbours.remove((x, y))
    return neighbours


def simulate_elves(elves: List[Tuple[int, int]]):
    rules_idx = 0
    round_number = 1

    while True:
        new_elves = set()
        # A mapping from a new position to a list of elves who want to go to that posiiton.
        d_elves = defaultdict(list)

        for elf in elves:
            if len(elves & get_neighbours(*elf)) > 0:
                for x in range(4):
                    positions, velocity = RULES[(rules_idx + x) % len(RULES)]
                    if (
                        len(elves & set((elf[0] + i, elf[1] + j) for i, j in positions))
                        == 0
                    ):
                        d_elves[(elf[0] + velocity[0], elf[1] + velocity[1])].append(
                            elf
                        )
                        break
                else:
                    new_elves.add(elf)
            else:
                new_elves.add(elf)

        for new_pos, old_poses in d_elves.items():
            # If multiple elves want to go to the same position,
            # keep the elves in their old positions.
            if len(old_poses) > 1:
                new_elves |= set(old_poses)
            else:
                new_elves.add(new_pos)

        if elves == new_elves:
            return round_number

        elves = new_elves

        # Part 1
        if round_number == 10:
            min_x = min(x for x, _ in elves)
            max_x = max(x for x, _ in elves)
            min_y = min(y for _, y in elves)
            max_y = max(y for _, y in elves)

            num_empty = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
            print(num_empty)

        rules_idx += 1
        round_number += 1


elves = set()
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == "#":
            elves.add((i, j))

print(simulate_elves(elves))
