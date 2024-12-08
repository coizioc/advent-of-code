import functools
import itertools
import operator


with open("input/year2024/day07.txt", "r") as f:
    lines = f.read().splitlines()


def concat(x, y):
    return int(str(x) + str(y))

@functools.lru_cache
def evaluate_operands(operands, ops):
    curr = operands[0]
    for i, op in enumerate(ops):
        curr = op(curr, operands[i + 1])
    return curr


def is_valid(line, ops):
    target_value, operands = line.split(": ")
    target_value = int(target_value)
    operands = tuple([int(x) for x in operands.split(" ")])

    for curr_ops in itertools.product(*[tuple([*ops]) for _ in range(len(operands) - 1)]):
        total = evaluate_operands(operands, curr_ops)
        if target_value == total:
            return target_value

    return 0


part_1 = sum([is_valid(line, [operator.add, operator.mul]) for line in lines])
print(part_1)
part_2 = sum([is_valid(line, [operator.add, operator.mul, concat]) for line in lines])
print(part_2)
