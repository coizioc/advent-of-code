use std::env;

mod year2022;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        panic!("Usage: <year> <day>");
    } else {
        let year = args[1].parse::<i32>();
        match year {
            Ok(2022) => year2022::run(args[2].clone()),
            Ok(n) => panic!("No program found for year {}.", n),
            Err(e) => panic!("Invalid argument for year: {}.", e),
        }
    }
}
