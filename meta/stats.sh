#!/usr/bin/env bash

# Create temp dir if doesn't exist.
mkdir -p meta/__temp

current_year=$(date +%Y)
current_date=$(date +%-d)

pids=()
i=0
for language in meta/__run/*; do
    language=${language%*.sh}
    language=${language##*/}
    for year in $(seq 2015 $current_year); do
        for day in $(seq 1 25); do
            if [[ $day -gt $current_date ]] && [[ $year -eq $current_year ]]; then
                continue
            fi
            if [[ $day -lt 10 ]]; then
                day="0${day}"
            fi
            ./meta/run.sh $language $year $day -v &
            pids[${i}]=$!
            i=$((i+1))
        done
    done
done

for pid in ${pids[*]}; do
    wait $pid
done

./meta/stats_gen.py
