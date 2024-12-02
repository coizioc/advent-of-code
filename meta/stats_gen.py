#!/usr/bin/env python

from collections import defaultdict
import os
import re

stats = defaultdict(dict)

stats_log_files = [
    file
    for file in os.listdir(os.path.join("meta", "__temp"))
    if file.startswith("validation") and file.endswith(".log")
]

for stats_log_file in stats_log_files:
    groups = re.findall(r"validation_(.+?)_(\d{4})_(\d{2}).log", stats_log_file)
    language, year, day = groups[0]
    with open(os.path.join("meta", "__temp", stats_log_file), "r") as f:
        lines = f.read().splitlines()

    if len(lines) == 0:
        stats[language][(year, day)] = [False, False]
    if len(lines) == 1:
        stats[language][(year, day)] = [
            lines[0].startswith("[O]"),
            # Day 25 only has one coding solution.
            day == "25" and lines[0].startswith("[O]"),
        ]
    if len(lines) == 2:
        stats[language][(year, day)] = [
            lines[0].startswith("[O]"),
            lines[1].startswith("[O]"),
        ]

language_display_names_map = {
    "py": "Python",
}

out = """# Stats

"""

for language in sorted(stats.keys()):
    display_language = language_display_names_map.get(language, language.title())

    out += "## " + display_language + "\n\n"

    out += "|" + "|".join(["Year"] + ["Day " + str(i + 1) for i in range(25)]) + "|\n"
    out += "|" + "|".join(["---" for _ in range(26)]) + "|\n"

    for year in range(2015, 2025):
        year = str(year)
        out += f"|{year}|"

        for day in range(1, 26):
            day = f"0{day}" if day < 10 else str(day)
            try:
                stars = stats[language][(year, day)]
            except KeyError:
                stars = [False, False]

            num_stars = len([part for part in stars if part == True])

            out += num_stars * "⭐ " + "|" if num_stars > 0 else " |"

        out += "\n"
    out += "\n"

with open("STATS.md", "w+", encoding="utf-8") as f:
    f.write(out)
