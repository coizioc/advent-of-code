package com.aoc.util;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileUtil {
    public static List<String> readFile(int year, int day) throws FileNotFoundException, IOException {
        var strDay = day > 9 ? Integer.toString(day) : "0%d".formatted(day);
        List<String> lines = new ArrayList<>();
        try (var br = new BufferedReader(new FileReader("input/year%d/day%s.txt".formatted(year, strDay)));) {
            String line = br.readLine();
            while (line != null) {
                lines.add(line);
                line = br.readLine();
            }
        }

        return lines;
    }
}
