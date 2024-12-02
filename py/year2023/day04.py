with open(f"input/year2023/day04.txt", "r") as f:
    lines = f.read().splitlines()

total_score = 0
copies = len(lines) * [1]
scores = len(lines) * [0]
for j, line in enumerate(lines):
    winning_nums, card_nums = line[line.find(": ") + 2:].split("| ")
    winning_nums = [int(winning_nums[i: i + 3]) for i in range(0, len(winning_nums), 3)]
    card_nums = [int(card_nums[i: i + 3]) for i in range(0, len(card_nums), 3)]
    num_winning_nums_in_card = sum([1 if num in winning_nums else 0 for num in card_nums])
    for k in range(num_winning_nums_in_card):
        copies[j + k + 1] += copies[j]
    scores[j] = 2 ** (num_winning_nums_in_card - 1) if num_winning_nums_in_card > 0 else 0

print(sum(scores))
print(sum(copies))
