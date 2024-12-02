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


def make_request(year: str, day: str) -> str | None:
    headers = {"Cookie": f"session={session}"}
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{int(day)}/input", headers=headers
    )
    if resp.status_code == 200:
        return resp.text
    else:
        print(resp.text, file=sys.stderr)
        return None


def main():
    year, day = validate_args()

    input_path = os.path.join(".", "input", f"year{year}", f"day{day}.txt")
    if os.path.exists(input_path):
        with open(input_path, "r") as f:
            text = f.read()

        if len(text) > 0:
            print("Input already exists for that date.")
            exit(0)

    input_text = make_request(year, day)
    if input_text is not None:
        if not os.path.exists(os.path.join(".", "input")):
            os.mkdir(os.path.join(".", "input"))
        if not os.path.exists(os.path.join(".", "input", f"year{year}")):
            os.mkdir(os.path.join(".", "input", f"year{year}"))

        with open(input_path, "w+") as f:
            f.write(input_text)
            print("Wrote input to", input_path)

    exit(0)


if __name__ == "__main__":
    main()
