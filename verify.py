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
    if len(sys.argv) < 3:
        print("Usage: ./get_aoc <year> <day>")
        exit(1)

    year, day = sys.argv[1], sys.argv[2]
    if not year.isnumeric():
        print("Argument <year> is not numeric!")
        exit(1)
    if not day.isnumeric():
        print("Argument <day> is not numeric!")
        exit(1)
    if not re.match(r"\d{2}", day) or int(day) < 1 or int(day) > 25:
        print("Argument <day> must be a two digit number between 01 and 25!")
        exit(1)
    return year, day


def validate(part, expected, actual):
    if expected == actual:
        print(f"[O] {part} {expected} == {actual}")
    else:
        print(f"[X] {part} {expected} != {actual}")


def main():
    year, day = validate_args()
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

    if os.path.exists("log.out"):
        with open("log.out", "r") as f:
            lines = f.read().splitlines()

            if len(matches) > 0:
                validate("Part 1", matches[0], lines[0])

            if len(matches) == 2:
                validate("Part 2", matches[1], lines[1])

    exit(0)


if __name__ == "__main__":
    main()
