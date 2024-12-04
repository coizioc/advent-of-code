#!/usr/bin/env python

import os
import re
import sys
from typing import List, Tuple
from dotenv import load_dotenv
import requests


load_dotenv()

session = os.environ["AOC_SESSION"]
if session is None:
    print("AOC_SESSION env variable not defined!")
    exit(1)


def get_answers(year: str, day: str) -> List[str]:
    # Try to get answers from local file.
    answers_directory = os.path.join(".", "meta", "answers")
    answer_file_path = os.path.join(answers_directory, f"year{year}_day{day}.txt")
    if (os.path.exists(answer_file_path)):
        with open(answer_file_path, "r") as f:
            lines = f.read().splitlines()
        # Only consider local answer if we have answered both parts beforehand.
        if len(lines) == 2:
            return lines
    
    # Otherwise, make HTTP call to get answers.
    headers = {"Cookie": f"session={session}"}
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{int(day)}", headers=headers
    )
    matches = re.findall(
        r"<p>Your puzzle answer was <code>(?P<answer>.+)</code>.</p>",
        resp.text,
        re.MULTILINE,
    )

    if not os.path.exists(answers_directory):
        os.mkdir(answers_directory)

    with open(answer_file_path, "w+") as f:
        f.write("\n".join(matches))

    return matches

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
    
    answers = get_answers(year, day)

    if len(answers) == 0:
        print("No answers found for given date.")
        exit(0)

    out = []
    log_path = os.path.join("meta", "__temp", f"out_{language}_{year}_{day}.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            lines = f.read().splitlines()

            if len(lines) > 0:
                out.append(validate("Part 1", answers[0], lines[0]))

            if len(lines) > 1:
                # 2022-10 part 2's answer returns ASCII art of a sequence of letters and cannot be directly validated.
                if year == "2022" and day == "10":
                    out.append(validate("Part 2", answers[1], answers[1]))
                else:
                    out.append(validate("Part 2", answers[1], lines[1]))

    if len(out) > 0:
        out_path = os.path.join(
            "meta", "__temp", f"validation_{language}_{year}_{day}.log"
        )
        with open(out_path, "w+") as f:
            f.write("\n".join(out) + "\n")

    exit(0)


if __name__ == "__main__":
    main()
