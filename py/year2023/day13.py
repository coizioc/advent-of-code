from itertools import product

with open(f"input/year2023/day13.txt", "r") as f:
    groups = [group.splitlines() for group in f.read().split("\n\n")]

def find_mirror(cols, size, ignore_match=None):
    if size == 0:
        return 0, 0
    for i, curr in enumerate(zip(*[cols[i:] for i in range(2 * size)])):
        if i not in [0, len(cols) - 2 * size]:
            continue
        if all(curr[j] == curr[-j - 1] for j in range(len(curr))):
            if not ignore_match or ignore_match != [size, i + size]:
                return size, i + size
    return find_mirror(cols, size - 1, ignore_match)

def replace_smudge(group, i, j):
    new_group = [*group]
    new_group[i] = new_group[i][:j] + ("." if group[i][j] == "#" else "#") + new_group[i][j + 1:]

    cols = ["".join(col) for col in zip(*new_group)]

    new_col_mirror_size, new_col_mirror_idx = find_mirror(cols, len(cols) // 2, ignore_match=[col_mirror_size, col_mirror_idx])
    new_row_mirror_size, new_row_mirror_idx = find_mirror(new_group, len(new_group) // 2, ignore_match=[row_mirror_size, row_mirror_idx])

    return new_col_mirror_size, new_col_mirror_idx, new_row_mirror_size, new_row_mirror_idx

def get_score(col_mirror_size, col_mirror_idx, row_mirror_size, row_mirror_idx):
    return col_mirror_idx if col_mirror_size > row_mirror_size else 100 * row_mirror_idx

p1_total = 0
p2_total = 0
for group in groups:
    cols = ["".join(col) for col in zip(*group)]

    col_mirror_size, col_mirror_idx = find_mirror(cols, len(cols) // 2)
    row_mirror_size, row_mirror_idx = find_mirror(group, len(group) // 2)

    p1_total += get_score(col_mirror_size, col_mirror_idx, row_mirror_size, row_mirror_idx)

    for i, j in product(range(len(group)), range(len(group[0]))):
        new_col_mirror_size, new_col_mirror_idx, new_row_mirror_size, new_row_mirror_idx = replace_smudge(group, i, j)

        # If no reflections found,
        if [new_col_mirror_size, new_row_mirror_size] == [0, 0]:
            continue

        # If an old reflection was found,
        if [col_mirror_size, col_mirror_idx] == [new_col_mirror_size, new_col_mirror_idx] and [row_mirror_size, row_mirror_idx] == [new_row_mirror_size, new_row_mirror_idx]:
            continue

        if [col_mirror_size, col_mirror_idx] != [new_col_mirror_size, new_col_mirror_idx] and [new_col_mirror_size, new_col_mirror_idx] != [0, 0] :
            p2_total += new_col_mirror_idx
        else:
            p2_total += 100 * new_row_mirror_idx
        break

print(p1_total)
print(p2_total)
