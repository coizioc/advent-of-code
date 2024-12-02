package com.aoc.year2022;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;

import com.aoc.util.FileUtil;

public class Day21 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        var lines = FileUtil.readFile(2022, 21);
        var variables = getVariables(lines);
        var part1 = evalRoot(variables);
        printDoubleAsInt(part1);

        var root = variables.get("root");
        if (root instanceof BinaryOp rootOp) {
            variables.put("root", new BinaryOp(rootOp.left, "-", rootOp.right));
        } else {
            throw new RuntimeException("Root is not BinaryOp!");
        }

        double part2 = part1;
        // Use Newton's method to find value of root such that
        // root.left - root.right == 0.
        for (int i = 0; i < Integer.MAX_VALUE; i++) {
            variables.put("humn", new Value(part2));
            var answer = evalRoot(variables);
            if (Math.abs(answer) < 1e-5) {
                printDoubleAsInt(part2);
                return;
            } else {
                variables.put("humn", new Value(part2 + 1));
                var dx = evalRoot(variables) - answer;
                part2 = part2 - answer / dx;
            }
        }

        System.err.println("Unable to determine part 2!");
    }

    public static Map<String, Node> getVariables(List<String> lines) {
        Map<String, Node> variables = new HashMap<>();
        for (var line : lines) {
            var parts = Arrays.asList(line.split(" "));

            // Remove trailing :
            var monkey = parts.get(0)
                    .substring(0, parts.get(0).length() - 1);
            var valueParts = parts.subList(1, parts.size());
            Node valueNode;
            if (valueParts.size() == 1) {
                valueNode = new Value(Double.parseDouble(valueParts.get(0)));
            } else {
                valueNode = new BinaryOp(
                        new Variable(valueParts.get(0)),
                        valueParts.get(1),
                        new Variable(valueParts.get(2)));
            }

            variables.put(monkey, valueNode);
        }

        return variables;
    }

    public static double evalRoot(Map<String, Node> variables) {
        return variables.get("root").eval(new Ctx(variables));
    }

    public static void printDoubleAsInt(double x) {
        System.out.println((long) Math.floor(x));
    }

    public static record Ctx(Map<String, Node> variables) {
    };

    public static interface Node {
        public double eval(Ctx ctx);
    }

    public static record Variable(String name) implements Node {
        @Override
        public double eval(Ctx ctx) {
            return ctx.variables.get(name).eval(ctx);
        }
    }

    public static record Value(double value) implements Node {
        @Override
        public double eval(Ctx ctx) {
            return value;
        }
    }

    public static record BinaryOp(Node left, String op, Node right) implements Node {

        static Map<String, BiFunction<Double, Double, Double>> SUPPORTED_OPERATIONS = Map.of(
                "+", ((a, b) -> a + b),
                "-", ((a, b) -> a - b),
                "*", ((a, b) -> a * b),
                "/", ((a, b) -> a / b));

        @Override
        public double eval(Ctx ctx) {
            return BinaryOp.SUPPORTED_OPERATIONS.get(this.op)
                    .apply(this.left.eval(ctx), this.right.eval(ctx));
        }
    }
}
