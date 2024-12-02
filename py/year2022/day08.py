import itertools

with open("input/year2022/day08.txt", "r") as f:
    lines = f.read().splitlines()

num_visible = 0
for i, j in itertools.product(range(len(lines)), range(len(lines[0]))):
    row = [int(tree) for tree in lines[i]]
    col = [int(line[j]) for line in lines]
    tree = int(lines[i][j])
    if (
        i in [0, len(lines) - 1]
        or j in [0, len(lines[i]) - 1]
        or all(left_tree < tree for left_tree in row[:j])
        or all(right_tree < tree for right_tree in row[j + 1 :])
        or all(up_tree < tree for up_tree in col[:i])
        or all(down_tree < tree for down_tree in col[i + 1 :])
    ):
        num_visible += 1


def get_scenic_score(trees, i, j):
    row = [int(tree) for tree in trees[i]]
    col = [int(line[j]) for line in trees]
    tree = int(trees[i][j])
    scenic_score = 1

    for dir_trees in [
        list(reversed(row[:j])),
        row[j + 1 :],
        list(reversed(col[:i])),
        col[i + 1 :],
    ]:
        view_dist = 0
        for dir_tree in dir_trees:
            view_dist += 1
            if dir_tree >= tree:
                break
        scenic_score *= view_dist

    return scenic_score


print(num_visible)
print(
    max(get_scenic_score(lines, i, j))
    for i, j in itertools.product(range(len(lines)), range(len(lines[0])))
)
