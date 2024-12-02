package com.aoc.year2022;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Comparator;

import com.aoc.util.FileUtil;
import com.aoc.util.ListUtil;

public class Day01 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        var lines = FileUtil.readFile(2022, 1);

        var elves = ListUtil.split(lines, "");
        var rationsInDescendingOrder = elves.stream()
                .map(elf -> elf.stream().map(x -> Integer.parseInt(x)).reduce(Integer::sum).get())
                .sorted(Comparator.reverseOrder())
                .toList();

        var part1 = rationsInDescendingOrder.get(0);
        var part2 = rationsInDescendingOrder.subList(0, 3)
                .stream()
                .reduce(Integer::sum)
                .get();

        System.out.println(part1);
        System.out.println(part2);
    }
}