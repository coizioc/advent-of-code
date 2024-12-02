mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;

pub fn run(day: String) {
    match day.parse::<i32>() {
        Ok(1) => day01::run(),
        Ok(2) => day02::run(),
        Ok(3) => day03::run(),
        Ok(4) => day04::run(),
        Ok(5) => day05::run(),
        Ok(6) => day06::run(),
        Ok(n) => panic!("No program found for day {}.", n),
        Err(e) => panic!("Invalid argument for day: {}.", e),
    }
}
