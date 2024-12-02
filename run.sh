#!/usr/bin/env bash

flag_verify='false'

print_usage() {
    echo "Usage: ./run.sh <language> <year> <day> (-v)"
}

if [ $# -lt 3 ]; then
    print_usage
    exit 1;
fi

language=$1
year=$2
day=$3

shift 3

while getopts 'v' flag; do
    case "${flag}" in
        v) flag_verify='true'; ;;
        *) print_usage
        exit 1 ;;
    esac
done

# Get input for <year> and <day> arguments.
./get_aoc.py $year $day || {
    exit 1;
}

# Check to see if <language> argument is valid.
if [ ! -f "./__run/$language.sh" ]; then
    echo "Unknown language $language"
    exit 1;
fi

# Run script for that language for the given year and day.
# Redirect otuput to temporary log file.
bash "./__run/$language.sh" $year $day > log.out || {
    exit 1;
}

# If user passes in verify flag, run verification script.
if [ "$flag_verify" = "true" ]; then
    ./verify.py $year $day
else
    # Log output from script.
    cat log.out
fi

# Delete temporary log file.
rm log.out;