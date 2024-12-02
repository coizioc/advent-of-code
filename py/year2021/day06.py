with open("input/year2021/day06.txt", "r") as f:
    lines = f.read().splitlines()

def simulate_lanterfish(days):
    lanternfish = 10 * [0] # -1 to 8
    for age in lines[0].split(","):
        lanternfish[int(age) + 1] += 1
    for _ in range(days):
        for i in range(1, len(lanternfish)):
            lanternfish[i], lanternfish[i - 1] = lanternfish[i - 1], lanternfish[i]
        lanternfish[7] += lanternfish[0]
        lanternfish[9] += lanternfish[0]
        lanternfish[0] = 0
    return sum(lanternfish)

print(simulate_lanterfish(80))
print(simulate_lanterfish(256))