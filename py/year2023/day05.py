from collections import defaultdict

with open(f"input/year2023/day05.txt", "r") as f:
    lines = f.read().splitlines()

seeds = [int(x) for x in lines[0][7:].split(" ")]

range_mappings = defaultdict(list)
curr_mapping = None
for line in lines[2:]:
    if curr_mapping is None:
        curr_mapping = line[:-5]
    elif line == "":
        curr_mapping = None
    else:
        range_mappings[curr_mapping].append([int(x) for x in line.split(" ")])

mappings = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

def transform_ranges(seed_ranges):
    for mapping in mappings:
        seed_ranges = convert_ranges(seed_ranges, mapping)
    return min(seed_ranges)[0]

def get_new_start_and_step(seed_min, size, ranges):
    # If seed_min is in range,
    for dest_begin, source_begin, range_len in ranges:
        if 0 <= seed_min - source_begin < range_len:
            return seed_min + dest_begin - source_begin, min(source_begin + range_len - seed_min, size)
    else:
        # seed_min is not in a range mapping, create maping from seed_min to next highest
        # range min, or an arbitrarily high number if seed_min is higher than all ranges.
        step = int(1e10)
        for dest_begin, source_begin, range_len in sorted(ranges):
            if source_begin > seed_min:
                step = min(source_begin - seed_min, size)
                break
        return seed_min, step

def convert_ranges(ranges, mapping):
    new_ranges = []
    for seed_min, seed_max in ranges:
        size = seed_max - seed_min
        while size > 0:
            new_start, step = get_new_start_and_step(seed_min, size, range_mappings[mapping])
            new_ranges.append((new_start, new_start + step))
            size -= step
            seed_min += step
    return new_ranges

print(transform_ranges([(seed, seed + 1) for seed in seeds]))
print(transform_ranges([(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]))
