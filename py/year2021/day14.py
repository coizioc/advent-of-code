from collections import Counter
import math

with open("./input/year2021/day14.txt", "r") as f:
    lines = f.read().splitlines()

insertion_rules = {}
for rule in lines[2:]:
    pair, insert_element = rule.split(" -> ")
    insertion_rules[pair] = insert_element


def apply_insertions(iterations):
    polymer_template_pairs = Counter()
    for a, b in zip(lines[0], lines[0][1:]):
        polymer_template_pairs[a + b] += 1
    for _ in range(iterations):
        new_polymer_template_pairs = Counter()
        for pair in polymer_template_pairs:
            a, b = pair[0], pair[1]
            new_polymer_template_pairs[
                a + insertion_rules[pair]
            ] += polymer_template_pairs[pair]
            new_polymer_template_pairs[
                insertion_rules[pair] + b
            ] += polymer_template_pairs[pair]
        polymer_template_pairs = new_polymer_template_pairs

    number_of_elements = Counter()
    for pair, count in polymer_template_pairs.items():
        a, b = pair[0], pair[1]
        number_of_elements[a] += count / 2
        number_of_elements[b] += count / 2
    return math.ceil(
        number_of_elements.most_common()[0][1] - number_of_elements.most_common()[-1][1]
    )


print(apply_insertions(10))
print(apply_insertions(40))
