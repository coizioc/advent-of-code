import functools
import operator
import re

with open(f"input/year2023/day06.txt", "r") as f:
    lines = f.read().splitlines()

times = [int(x) for x in re.split(r" +", lines[0])[1:]]
distances = [int(x) for x in re.split(r" +", lines[1])[1:]]

new_time = int("".join([str(x) for x in times]))
new_distance = int("".join(str(x) for x in distances))

def get_ways_to_win(times, distances):
    ways_to_win= []
    
    for time, record in zip(times, distances):
        num_ways_to_win = 0
        for i in range(time):
            if i * (time - i) > record:
                num_ways_to_win += 1
        ways_to_win.append(num_ways_to_win)

    return functools.reduce(operator.mul, ways_to_win)

print(get_ways_to_win(times, distances))
print(get_ways_to_win([new_time], [new_distance]))
