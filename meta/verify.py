#!/usr/bin/env python

import os
import re
import sys
from typing import Tuple
from dotenv import load_dotenv
import requests


load_dotenv()

session = os.environ["AOC_SESSION"]
if session is None:
    print("AOC_SESSION env variable not defined!")
    exit(1)


def validate_args() -> Tuple[str, str]:
    if len(sys.argv) < 4:
        print("Usage: ./verify <language> <year> <day>")
        exit(1)

    language, year, day = sys.argv[1], sys.argv[2], sys.argv[3]
    if not year.isnumeric():
        print("Argument <year> is not numeric!")
        exit(1)
    if not day.isnumeric():
        print("Argument <day> is not numeric!")
        exit(1)
    if not re.match(r"\d{2}", day) or int(day) < 1 or int(day) > 25:
        print("Argument <day> must be a two digit number between 01 and 25!")
        exit(1)
    return language, year, day


def validate(part, expected, actual):
    if expected == actual:
        return f"[O] {part} {expected} == {actual}"
    else:
        return f"[X] {part} {expected} != {actual}"


def main():
    language, year, day = validate_args()
    headers = {"Cookie": f"session={session}"}
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{int(day)}", headers=headers
    )
    matches = re.findall(
        r"<p>Your puzzle answer was <code>(?P<answer>.+)</code>.</p>",
        resp.text,
        re.MULTILINE,
    )

    if len(matches) == 0:
        print("No answers found for given date.")
        exit(0)

    out = []
    log_path = os.path.join("meta", "__temp", f"out_{language}_{year}_{day}.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            lines = f.read().splitlines()

            if len(lines) > 0:
                out.append(validate("Part 1", matches[0], lines[0]))

            if len(lines) == 2:
                out.append(validate("Part 2", matches[1], lines[1]))

    if len(out) > 0:
        out_path = os.path.join(
            "meta", "__temp", f"validation_{language}_{year}_{day}.log"
        )
        with open(out_path, "w+") as f:
            f.write("\n".join(out) + "\n")

    exit(0)


if __name__ == "__main__":
    main()
