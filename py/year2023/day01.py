with open(f"input/year2023/day01.txt", "r") as f:
    lines = f.read().splitlines()

real_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}
numeric_digits = {str(i): i for i in range(10)}
real_digits.update(numeric_digits)

def get_digits(line: str, digits: dict):
    idxs = [(digit, line.find(digit), line.rindex(digit)) for digit in digits if line.find(digit) > -1]
    min_digit = digits[min(idxs, key=lambda x: x[1])[0]]
    max_digit = digits[max(idxs, key=lambda x: x[2])[0]]
    return 10 * min_digit + max_digit

print(sum([get_digits(line, numeric_digits) for line in lines]))
print(sum([get_digits(line, real_digits) for line in lines]))
