use regex::Regex;
use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day05.txt").unwrap();
    text = text.replace("\r\n", "\n");
    let lines = text.split("\n").filter(|line| line.len() > 0).collect();

    let part1 = move_stacks(&lines, false);
    let part2 = move_stacks(&lines, true);

    println!("{}", part1);
    println!("{}", part2);
}

fn parse_stacks(lines: &Vec<&str>, stack_start_idx: usize) -> Vec<Vec<char>> {
    let mut stacks: Vec<Vec<char>> = (0..(lines[stack_start_idx].len()))
        .skip(1)
        .step_by(4)
        .map(|_| Vec::new())
        .collect();

    for line in lines.iter().take(stack_start_idx).rev() {
        for (i, c) in line
            .chars()
            .skip(1)
            .step_by(4)
            .enumerate()
            .filter(|(_, c)| *c != ' ')
        {
            stacks[i].push(c);
        }
    }

    stacks
}

fn parse_instruction(line: &&str) -> (i32, usize, usize) {
    let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap();
    let matches: [&str; 3] = re.captures(line).map(|caps| caps.extract()).unwrap().1;

    let stack_number = matches[0].parse::<i32>().unwrap();
    let stack_from_idx = matches[1].parse::<usize>().unwrap();
    let stack_to_idx = matches[2].parse::<usize>().unwrap();

    (stack_number, stack_from_idx, stack_to_idx)
}

fn parse_instructions(lines: &Vec<&str>, stack_start_idx: usize) -> Vec<(i32, usize, usize)> {
    lines
        .iter()
        .skip(stack_start_idx + 1)
        .map(parse_instruction)
        .collect()
}

fn move_stacks(lines: &Vec<&str>, in_order: bool) -> String {
    let stack_start_idx = lines
        .iter()
        .position(|line| !line.starts_with("["))
        .unwrap();

    let mut stacks = parse_stacks(&lines, stack_start_idx);
    let instructions = parse_instructions(&lines, stack_start_idx);

    for (stack_number, stack_from_idx, stack_to_idx) in instructions {
        let mut stack_to_add: Vec<char> = Vec::new();
        for _ in 0..stack_number {
            let value = stacks[stack_from_idx - 1].pop().unwrap();
            stack_to_add.push(value);
        }

        if in_order {
            stack_to_add.reverse();
        }

        stacks[stack_to_idx - 1].append(&mut stack_to_add);
    }

    stacks
        .into_iter()
        .map(|stack| stack.into_iter().last().unwrap_or(' '))
        .collect::<String>()
}
