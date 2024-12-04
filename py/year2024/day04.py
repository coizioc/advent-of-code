import itertools


with open("input/year2024/day04.txt", "r") as f:
    lines = f.read().splitlines()

DIRECTION_VECTORS = [
    (i, j) for i, j in itertools.product(range(-1, 2), range(-1, 2)) if (i, j) != (0, 0)
]


def find_word(lines, i, j, word, directions):
    word_count = 0
    for dx, dy in directions:
        if dx == -1 and i < len(word) - 1:
            continue
        if dx == 1 and len(lines) - i < len(word):
            continue
        if dy == -1 and j < len(word) - 1:
            continue
        if dy == 1 and len(lines[i]) - j < len(word):
            continue

        for n in range(len(word)):
            if lines[i + n * dx][j + n * dy] != word[n]:
                break
        else:
            word_count += 1
    return word_count


found_xmases = 0
found_x_mases = 0
for i, j in itertools.product(range(len(lines)), range(len(lines[0]))):
    found_xmases += find_word(lines, i, j, "XMAS", DIRECTION_VECTORS)
    if 0 < i < len(lines) - 1 and 0 < j < len(lines[i]) - 1:
        backslash_matches = find_word(lines, i - 1, j - 1, "MAS", [(1, 1)]) + find_word(lines, i + 1, j + 1, "MAS", [(-1, -1)])
        forward_slash_matches = find_word(lines, i - 1, j + 1, "MAS", [(1, -1)]) + find_word(lines, i + 1, j - 1, "MAS", [(-1, 1)])
        if backslash_matches > 0 and forward_slash_matches > 0:
            found_x_mases += 1
        

print(found_xmases)
print(found_x_mases)
