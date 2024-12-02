use std::collections::HashSet;
use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day04.txt").unwrap();
    text = text.replace("\r\n", "\n");
    let lines = text.split("\n").filter(|line| line.len() > 0);

    let pairs: Vec<Vec<Vec<i32>>> = lines
        .map(|line| line.split(",").collect())
        .map(|pairs: Vec<&str>| {
            pairs
                .into_iter()
                .map(|pair| pair.split("-").map(|a| a.parse::<i32>().unwrap()).collect())
                .collect()
        }).collect();

    let part1 = pairs
        .clone()
        .into_iter()
        .filter(|pairs| contains(pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]))
        .count();

    let part2 = pairs
        .into_iter()
        .filter(|pairs| overlaps(pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]))
        .count();
    println!("{}", part1);
    println!("{}", part2);
}

fn contains(a_min: i32, a_max: i32, b_min: i32, b_max: i32) -> bool {
    a_min <= b_min && a_max >= b_max || a_min >= b_min && a_max <= b_max
}

fn overlaps(a_min: i32, a_max: i32, b_min: i32, b_max: i32) -> bool {
    let a: HashSet<i32> = HashSet::from_iter((a_min..(a_max + 1)).into_iter());
    let b: HashSet<i32> = HashSet::from_iter((b_min..(b_max + 1)).into_iter());

    a.intersection(&b).count() > 0
}
