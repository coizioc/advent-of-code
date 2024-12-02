# Advent of Code

Repository for hosting my [Advent of Code](https://adventofcode.com) solutions.

## Usage

Make sure to set the AOC_SESSION environment variable with your AOC session cookie. This page describes how to get the session cookie: https://github.com/wimglenn/advent-of-code-wim/issues/1

Make sure to install pip requirements before running any scripts.

```bash
$ ./run.sh <language> <year> <day>
```

Supported languages are in the [`__run`](https://github.com/coizioc/advent-of-code/tree/main/__run) folder.

Optionally, you can add the `-v` flag to the end of the `./run.sh` arguments to validate the output of the script against the answers for your given input (assuming you have already solved the problem/part on AOC):

```bash
$ ./run.sh <language> <year> <day> -v
```
