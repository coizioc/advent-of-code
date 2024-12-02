use std::env;

mod year2022;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Usage: <year> <day>");
    } else {
        let year = args[1].parse::<i32>();
        match year {
            Ok(2022) => year2022::run(args[2].clone()),
            Ok(n) => println!("No program found for year {}.", n),
            Err(e) => println!("Invalid argument for year: {}.", e),
        }
    }
}
