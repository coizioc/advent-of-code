from typing import Tuple


with open("input/year2024/day06.txt", "r") as f:
    lines = f.read().splitlines()

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_loop(lines, guard) -> Tuple[int, bool]:
    original_guard = tuple([*guard])

    dir_idx = 0
    v_guard = DIRECTIONS[0]

    i = 0
    tiles_travelled = set()
    escapes = False

    def is_in_bounds(pos):
        return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0])

    # Iterate until the guard theoretically has walked every square in the grid.
    while i < len(lines) * len(lines[0]):
        tiles_travelled.add(guard)

        # Try moving forward.
        next_pos = (guard[0] + v_guard[0], guard[1] + v_guard[1])

        if is_in_bounds(next_pos):
            # If we encounter a wall,
            # Try turning right until we can move foward in a direction.
            while lines[next_pos[0]][next_pos[1]] == "#":
                dir_idx += 1
                v_guard = DIRECTIONS[dir_idx % 4]
                next_pos = (guard[0] + v_guard[0], guard[1] + v_guard[1])

            # If the next position is now not in bounds, the guard escapes.
            if not is_in_bounds(next_pos):
                escapes = True
                break

            guard = next_pos
            # If the guard returns to the beginning, stop iterating.
            if guard == original_guard and v_guard == DIRECTIONS[0]:
                break
        else:
            escapes = True
            break
        i += 1
    else:
        # If guard gets stuck in a loop that doesn't pass
        # through his original position, consider this an escape.
        escapes = False
    return tiles_travelled, escapes


guard = None
for i, line in enumerate(lines):
    try:
        j = line.index("^")
        guard = (i, j)
        break
    except ValueError:
        pass


tiles_travelled, _ = is_loop(lines, guard)

print(len(tiles_travelled))

num_loops = 0
for i, j in tiles_travelled:
    if lines[i][j] != ".":
        continue

    new_lines = [line for line in lines]
    new_lines[i] = new_lines[i][:j] + "#" + new_lines[i][j + 1 :]

    _, escaped = is_loop(new_lines, guard)

    if not escaped:
        num_loops += 1

print(num_loops)
