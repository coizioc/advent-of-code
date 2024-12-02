package com.aoc.util;

import java.util.ArrayList;
import java.util.List;

public class ListUtil {
    /**
     * Splits a list into multiple sublists based on a delimiter element.
     *
     * @param <T> The type of elements in the list.
     * @param list the list we want to split.
     * @param delimiter the element in the list by which we want to split.
     * @return a list of sublists containing elements that were separated by {@code delimiter}.
     */
    public static <T> List<List<T>> split(List<T> list, T delimiter) {
        List<List<T>> lists = new ArrayList<>();

        List<T> currList = new ArrayList<>();

        for (var t : list) {
            if (t.equals(delimiter)) {
                lists.add(new ArrayList<>(currList));
                currList.clear();
            } else {
                currList.add(t);
            }
        }

        return lists;
    }
}
