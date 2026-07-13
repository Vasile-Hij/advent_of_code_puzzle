# Advent of Code Solver

A Python framework for solving Advent of Code puzzles with automatic project structure generation and file management. This repo may inherit some functions from my previous [Advent of Code](https://github.com/Vasile-Hij/advent_of_code).

## Features

- Improved automatic directory and file creation
- Organized structure by year and day
- Simple command-line interface
- Sample input support for testing
- Pre-configured solution templates

## Installation

Clone and initialize:

```bash
git clone https://github.com/Vasile-Hij/advent_of_code_puzzle
cd advent_of_code_puzzle
just init
```

This project uses [`just`](https://github.com/casey/just) as its command runner.
Install it with `cargo install just`, `brew install just`, or `apt install just`.

## Usage

Basic commands:

```bash
just up
python main.py -id 2501 -p a        # 2501 -> YYDD, a -> part a
python main.py -id 2501 -p b        # 2501 -> YYDD, a -> part b
python main.py -id 2501 -p a -s s   # 2501 -> YYDD, a -> part a with sample input
python main.py -id 2501 -r 1        # auto run both parts and dump results to JSON
just down
```

## Just Commands

```bash
just               # Show all commands (same as `just help`)
just --list        # Show all commands
just install-uv    # Install uv package manager
just setup         # Initialize project
just up            # Activate virtual environment
just down          # Deactivate virtual environment
just lock          # Update dependencies
just init          # Full initialization
just lint          # Highlights semantic and stylistic issue
just test          # Run the test suite
just check         # Run lint + test at once
```
## Workflow

Running `python main.py -id 2501 -p a -s s ` it will create and populate a script file in `25` directory 
with script file `1.py`. Also it will create a sample file in `input` directory named `1_sample_a.txt`. 
If running without a sample will also create a new input file named `1.txt`


## License

[MIT License](LICENSE)
