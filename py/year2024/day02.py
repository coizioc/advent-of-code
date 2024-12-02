with open("input/year2024/day02.txt", "r") as f:
    lines = f.read().splitlines()


def is_safe(report):
    num_increases = 0
    for prev, curr in zip(report, report[1:]):
        diff = curr - prev
        if diff > 0:
            num_increases += 1
        if not (0 < abs(diff) < 4):
            return False
    return num_increases in [0, len(report) - 1]


def is_safe_with_at_most_one_error(report):
    if is_safe(report):
        return True
    for j in range(len(report)):
        report_without_jth_level = report[:j] + report[j + 1 :]
        if is_safe(report_without_jth_level):
            return True
    return False


reports = [[int(level) for level in line.split(" ")] for line in lines]

print(len([report for report in reports if is_safe(report)]))
print(len([report for report in reports if is_safe_with_at_most_one_error(report)]))
