use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day02.txt").unwrap();
    text = text.replace("\r\n", "\n");
    let lines = text.split("\n").filter(|line| line.len() > 0);

    let strategies = lines
        .map(|line| line.split(" ").collect::<Vec<&str>>())
        .map(|strategies| (strategies[0], strategies[1]));

    let part1: i32 = strategies
        .clone()
        .map(|(opponent, you)| rps(opponent, you))
        .sum();

    let part2: i32 = strategies
        .map(|(opponent, state)| choose_you_rps(opponent, state))
        .sum();

    println!("{}", part1);
    println!("{}", part2);
}

fn rps(opponent: &str, you: &str) -> i32 {
    let opponent_num = ord(opponent) - ord("A");
    let you_num = ord(you) - ord("X");

    if opponent_num == you_num {
        you_num + 1 + 3
    } else if opponent_num == (you_num + 1) % 3 {
        you_num + 1 + 0
    }
    // opponent_num == (you_num - 1) % 3
    else {
        you_num + 1 + 6
    }
}

fn choose_you_rps(opponent: &str, state: &str) -> i32 {
    let opponent_num = ord(opponent) - ord("A");

    match state {
        "X" => modulus(opponent_num - 1, 3) + 1,
        "Y" => opponent_num + 1 + 3,
        "Z" => (opponent_num + 1) % 3 + 1 + 6,
        _ => 0,
    }
}

fn ord(x: &str) -> i32 {
    x.chars().nth(0).unwrap() as i32
}

fn modulus(a: i32, b: i32) -> i32 {
    ((a % b) + b) % b
}