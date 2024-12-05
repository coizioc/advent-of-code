import functools


with open("input/year2024/day05.txt", "r") as f:
    lines = f.read()

rules, patterns = [x.splitlines() for x in lines.split("\n\n")]

part_1 = 0
part_2 = 0
for pattern in patterns:
    nums = pattern.split(",")
    valid = True
    sorted_nums = sorted(
        nums,
        # x|y rules implies x < y => -1 in the comparator.
        key=functools.cmp_to_key(lambda x, y: -1 if f"{x}|{y}" in rules else 1),
    )
    if nums == sorted_nums:
        part_1 += int(nums[len(nums) // 2])
    else:
        part_2 += int(sorted_nums[len(nums) // 2])

print(part_1)
print(part_2)
