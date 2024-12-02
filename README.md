# Advent of Code

Repository for hosting my [Advent of Code](https://adventofcode.com) solutions.

Click [here](STATS.md) to see how well (or terrible) I'm doing!

## Usage

Make sure to set the AOC_SESSION environment variable with your AOC session cookie. This page describes how to get the session cookie: https://github.com/wimglenn/advent-of-code-wim/issues/1

Make sure to install pip requirements before running any scripts.

```bash
$ ./meta/run.sh <language> <year> <day>
```

Supported languages are in the [`meta/__run`](https://github.com/coizioc/advent-of-code/tree/main/meta/__run) folder.

Optionally, you can add the `-v` flag to the end of the `./meta/run.sh` arguments to validate the output of the script against the answers for your given input (assuming you have already solved the problem/part on AOC):

```bash
$ ./meta/run.sh <language> <year> <day> -v
```

To update the `STATS.md` file, run the `./meta/stats.sh` script.