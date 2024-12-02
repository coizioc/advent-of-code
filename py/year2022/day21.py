import re

with open("./input/year2022/day21.txt", "r") as f:
    lines = f.read().splitlines()

def reduce_root(monkeys):
    while type(monkeys["root"]) == str:
        values = monkeys["root"].split(" ")
        for value in values:
            if value in monkeys:
                monkeys["root"] = monkeys["root"].replace(value, "( " + str(monkeys[value]) + " )")
        if re.match(r"^[\(\) 0-9\-\+\/\*\=X]+$", monkeys["root"]):
            break
    return monkeys

monkeys = {}
monkeys_v2 = {}
for line in lines:
    monkey, value = line.split(": ")
    monkeys[monkey] = monkeys_v2[monkey] = int(value) if value.isnumeric() else value
    if monkey == "humn":
        monkeys_v2["humn"] = "X"
    if monkey == "root":
        root_values = monkeys_v2["root"].split(" ")
        monkeys_v2["root"] = root_values[0] + " == " + root_values[-1]

monkeys = reduce_root(monkeys)
monkeys["root"] = int(eval(monkeys["root"]))
print(monkeys["root"])

monkeys_v2 = reduce_root(monkeys_v2)
left, right = monkeys_v2["root"].split(" == ")
if re.match(r"^[^X]+$", left):
    left = eval(left)
    equation = right + " - " + str(left)
else:
    right = eval(right)
    equation = left + " - " + str(right)

guess = monkeys["root"]
for i in range(1_000_000):
    answer = eval(equation.replace("X", str(int(guess))))
    if answer == 0:
        print(int(guess))
        break
    else:
        dx = eval(equation.replace("X", str(int(guess + 1)))) - answer
        guess = guess - (answer / dx)
else:
    print("Can't solve oopsie woopsie")