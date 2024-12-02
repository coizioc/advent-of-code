with open(f"input/year2022/day06.txt", "r") as f:
    line = f.read()

def get_header(packet, n):
    for i, chars in enumerate(zip(*[packet[i:] for i in range(n)])):
        if len(set(chars)) == n:
            return i + n

print(get_header(line, 4))
print(get_header(line, 14))
