from collections import deque
from typing import List, Tuple


with open("input/year2024/day09.txt", "r") as f:
    lines = f.read().splitlines()

disk_map = lines[0]


def get_first_gap(disk: List[Tuple[int, int, int]]) -> Tuple[int, int]:
    gaps = get_all_gaps(disk)
    if len(gaps) > 0:
        return gaps[0]
    else:
        return -1, None


def get_all_gaps(disk: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    previous_file_idx = -1
    curr_idx = 0
    gaps = []
    for i, (start_idx, _, length) in enumerate(disk):
        if curr_idx != start_idx:
            gaps.append((curr_idx, previous_file_idx))
            curr_idx = start_idx
        previous_file_idx = i
        curr_idx += length
    return gaps


def get_file_with_id(disk, n_to_find):
    for i, file in enumerate(disk):
        if file[1] == n_to_find:
            return i
    return -1


def compress_disk_bytewise(disk: List[Tuple[int, int, int]]):
    disk = disk.copy()
    while True:
        gap_idx, previous_file_idx = get_first_gap(disk)
        if gap_idx == -1:
            return disk

        last_file_idx, last_file_n, last_file_length = disk.pop()

        # If the file after the gap is the file we just removed,
        if previous_file_idx == len(disk) - 1:
            next_file_idx = last_file_idx
        else:
            next_file_idx, _, _ = disk[previous_file_idx + 1]
        gap_size = next_file_idx - gap_idx

        gap_file = (gap_idx, last_file_n, min(gap_size, last_file_length))
        if gap_size < last_file_length:
            disk.append((last_file_idx, last_file_n, last_file_length - gap_size))

        disk.insert(previous_file_idx + 1, gap_file)


def compress_disk_filewise(disk: List[Tuple[int, int, int]]):
    disk = disk.copy()
    max_n = disk[-1][1]
    for n_to_move in range(max_n, 0, -1):
        n_to_move_i = get_file_with_id(disk, n_to_move)
        n_file_start_idx, n_file_n, n_file_length = disk[n_to_move_i]

        gaps_to_check = [gap for gap in get_all_gaps(disk) if gap[0] < n_file_start_idx]
        for gap_idx, previous_file_idx in gaps_to_check:
            next_file_idx, _, _ = disk[previous_file_idx + 1]
            gap_size = next_file_idx - gap_idx

            if n_file_length <= gap_size:
                disk.remove((n_file_start_idx, n_file_n, n_file_length))
                gap_file = (gap_idx, n_to_move, n_file_length)
                disk.insert(previous_file_idx + 1, gap_file)
                break
    return disk


def get_checksum(disk: List[Tuple[int, int, int]]):
    checksum = 0
    for start_idx, n, length in disk:
        for i in range(start_idx, start_idx + length):
            checksum += i * n
    return checksum


n = 0
is_file = True
disk = deque()
curr_idx = 0
for c in disk_map:
    file_length = int(c)
    if is_file:
        disk.append((curr_idx, n, file_length))
        n += 1

    curr_idx += file_length
    is_file = not is_file

compressed_disk = compress_disk_bytewise(disk)
print(get_checksum(compressed_disk))

compressed_disk = compress_disk_filewise(disk)
print(get_checksum(compressed_disk))
