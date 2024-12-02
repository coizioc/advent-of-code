use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day01.txt").unwrap();
    text = text.replace("\r\n", "\n");
    let elves = text.split("\n\n");

    let mut ration_amounts: Vec<i32> = elves
        .map(|elf| {
            elf.split("\n")
                .map(|ration| match ration.parse::<i32>() {
                    Ok(n) => n,
                    Err(_e) => 0,
                })
                .sum::<i32>()
        })
        .collect::<Vec<i32>>();

    ration_amounts.sort();

    println!("{}", ration_amounts.last().unwrap());
    println!("{}", ration_amounts.iter().rev().take(3).sum::<i32>());
}
