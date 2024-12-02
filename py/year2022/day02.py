with open(f"input/year2022/day02.txt", "r") as f:
    lines = f.read().splitlines()

def rps(opponent, you):
    opponent_num = ord(opponent) - ord("A")
    you_num = ord(you) - ord("X")

    if you_num == opponent_num: return 3
    if (you_num + 1) % 3 == opponent_num: return 0
    if (you_num - 1) % 3 == opponent_num: return 6

def choose_you_rps(opponent, state):
    opponent_num = ord(opponent) - ord("A")

    if state == "X": return (opponent_num - 1) % 3 + 1
    if state == "Y": return opponent_num + 1 + 3
    if state == "Z": return (opponent_num + 1) % 3 + 1 + 6

strategies = [line.split(" ") for line in lines]

print(sum([ord(you) - ord("X") + 1 + rps(opponent, you) for opponent, you in strategies]))
print(sum([choose_you_rps(opponent, state) for opponent, state in strategies]))
