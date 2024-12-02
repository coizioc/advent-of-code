from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Union

with open("./input/year2022/day07.txt", "r") as f:
    lines = f.read().splitlines()

@dataclass
class Directory:
    name: str
    parent: Directory
    children: Dict[Union[Directory, int]] = field(default_factory=dict)

    def __hash__(self):
        return hash(self.name)

def get_size(dir: Directory):
    subdir_size = 0
    for subdir in dir.children.values():
        if type(subdir) == int:
            subdir_size += subdir
        else:
            subdir_size += get_size(subdir)
    return subdir_size

def tree_to_set(dir: Directory):
    dir_set = set([(dir, dir.parent)])
    for child in dir.children.values():
        if type(child) == Directory:
            dir_set.update(tree_to_set(child))
    return dir_set

top_level_dir = Directory("/", None)
curr_dir = top_level_dir
line_idx = 1
while line_idx < len(lines):
    argv = lines[line_idx].split()
    if argv[1] == "cd":
        if argv[2] == "..":
            curr_dir = curr_dir.parent
        elif argv[2] not in curr_dir.children.keys():
            new_dir = Directory(argv[2], curr_dir)
        else:
            curr_dir = curr_dir.children[argv[2]]
        line_idx += 1
    elif argv[1] == "ls":
        line_idx += 1
        while line_idx < len(lines) and not lines[line_idx].startswith("$"):
            ls_argv = lines[line_idx].split()
            if ls_argv[0] == "dir":
                if ls_argv[1] not in curr_dir.children.keys():
                    new_dir = Directory(ls_argv[1], curr_dir)
                    curr_dir.children[ls_argv[1]] = new_dir
            else:
                curr_dir.children[ls_argv[1]] = int(ls_argv[0])
            line_idx += 1

all_dirs = tree_to_set(top_level_dir)
dir_sizes = sorted([get_size(dir) for dir, _ in all_dirs])

total_disk_space = 70_000_000
target_free_space = 30_000_000
current_free_space = total_disk_space - get_size(top_level_dir)
min_size_to_remove = target_free_space - current_free_space

print(sum(size for size in dir_sizes if size <= 100_000))
print([size for size in dir_sizes if size >= min_size_to_remove][0])