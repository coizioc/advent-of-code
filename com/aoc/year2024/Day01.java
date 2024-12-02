package com.aoc.year2024;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.aoc.util.FileUtil;

public class Day01 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        var lines = FileUtil.readFile(2024, 1);

        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (var line : lines) {
            var parts = line.split("   ");
            left.add(Integer.parseInt(parts[0]));
            right.add(Integer.parseInt(parts[1]));
        }

        left.sort(Comparable::compareTo);
        right.sort(Comparable::compareTo);

        var distance = 0;
        for (var i = 0; i < left.size(); i++) {
            distance += Math.abs(left.get(i) - right.get(i));
        }
        System.out.println(distance);

        Map<Integer, Integer> rightCounts = new HashMap<>();
        for (var i = 0; i < right.size(); i++) {
            rightCounts.put(right.get(i), rightCounts.getOrDefault(right.get(i), 0) + 1);
        }

        var similarityScore = 0;
        for (var i = 0; i < left.size(); i++) {
            similarityScore += left.get(i) * rightCounts.getOrDefault(left.get(i), 0);
        }
        System.out.println(similarityScore);
    }
}
