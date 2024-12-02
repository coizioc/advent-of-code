use std::fs;

pub fn run() {
    let mut text = fs::read_to_string("../input/year2022/day06.txt").unwrap();
    text = text.split("\r\n").take(1).collect::<String>();

    let part1 = get_packet_marker_idx(&text, 4);
    let part2 = get_packet_marker_idx(&text, 14);
    println!("{}", part1);
    println!("{}", part2);
}

fn get_packet_marker_idx(text: &String, size: usize) -> i32 {
    for i in 0..(text.len() - size) {
        let chars: u32 = (0..size)
            .map(|j| 1 << text.as_bytes()[i + j] - "a".as_bytes()[0])
            .sum();
        if u32::count_ones(chars) == size as u32 {
            return (i + size) as i32;
        }
    }
    -1
}
