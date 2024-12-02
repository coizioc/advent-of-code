#!/usr/bin/env bash

if [ $# -lt 3 ]; then
    echo "Usage: ./run.sh <language> <year> <day>"
    exit 0;
fi

# Get input for <year> and <day> arguments.
./get_aoc.py $2 $3 || {
    exit 1;
}

# Check to see if <language> argument is valid.
if [ ! -f "./__run/$1.sh" ]; then
    echo "Unknown language $1"
    exit 1;
fi

# Run script for that language for the given year and day.
bash "./__run/$1.sh" $2 $3 || {
    exit 1;
}