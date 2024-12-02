use std::collections::HashSet;
use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day03.txt").unwrap();
    text = text.replace("\r\n", "\n");
    let lines = text
        .split("\n")
        .filter(|line| line.len() > 0)
        .collect::<Vec<&str>>();

    let part1: i32 = lines
        .clone()
        .into_iter()
        .map(|line| get_priority_line(line))
        .sum();

    let part2: i32 = (0..lines.len())
        .step_by(3)
        .map(|i| get_priority_group(vec![lines[i], lines[i + 1], lines[i + 2]]))
        .sum();

    println!("{}", part1);
    println!("{}", part2);
}

fn get_priority_line(line: &str) -> i32 {
    let divider = line.len() / 2;
    let compartment1 = &line[0..divider];
    let compartment2 = &line[divider..line.len()];

    get_priority_group(vec![compartment1, compartment2])
}

fn get_priority_group(group: Vec<&str>) -> i32 {
    let shared_items = group
        .into_iter()
        .map(|compartment| HashSet::from_iter(compartment.chars()))
        .reduce(|curr: HashSet<char>, new: HashSet<char>| {
            curr.intersection(&new).cloned().collect::<HashSet<char>>()
        })
        .unwrap()
        .into_iter()
        .collect::<String>();

    get_priority(shared_items.as_str())
}

fn get_priority(x: &str) -> i32 {
    let value = if x.to_ascii_uppercase() == x.to_string() {
        26
    } else {
        0
    };
    ord(x.to_ascii_lowercase().as_str()) - ord("a") + 1 + value
}

fn ord(x: &str) -> i32 {
    x.chars().nth(0).unwrap() as i32
}
