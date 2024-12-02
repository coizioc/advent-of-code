#!/usr/bin/env bash

# Create temp dir if doesn't exist.
mkdir -p meta/__temp

flag_verify='false'

print_usage() {
    >&2 echo "Usage: ./run.sh <language> <year> <day> (-v)"
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
./meta/get_aoc.py $year $day || {
    exit 1;
}

# Check to see if <language> argument is valid.
if [ ! -f "./meta/__run/$language.sh" ]; then
    >&2 echo "Unknown language $language"
    exit 1;
fi

# Run script for that language for the given year and day.
# Redirect otuput to temporary log file.
bash "./meta/__run/$language.sh" $year $day > meta/__temp/out_${language}_${year}_${day}.log || {
    exit 1;
}

# If user passes in verify flag, run verification script.
if [[ $flag_verify = "true" ]]; then
    ./meta/verify.py $language $year $day
    cat meta/__temp/validation_${language}_${year}_${day}.log
else
    # Log output from script.
    cat meta/__temp/out_${language}_${year}_${day}.log
fi