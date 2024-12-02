from collections import Counter


with open("input/year2024/day01.txt", "r") as f:
    lines = f.read().splitlines()

left_nums = []
right_nums = []

for line in lines:
    left, right = line.split("   ")
    left_nums.append(int(left))
    right_nums.append(int(right))

distance = 0
for left, right in zip(sorted(left_nums), sorted(right_nums)):
    distance += abs(left - right)

print(distance)

right_set = Counter(right_nums)

similarity_score = 0
for left in left_nums:
    similarity_score += left * right_set[left]

print(similarity_score)
