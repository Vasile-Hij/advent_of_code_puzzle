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
cd advent-of-code-solver
make init
```

## Usage

Basic commands:

```bash
make up
python main.py -id 2501 -p a        # 2501 -> YYDD, a -> part a
python main.py -id 2501 -p b        # part b
python main.py -id 2501 -p a -s s   # with sample input
make down
```



## Make Commands

```bash
make help          # Show all commands
make install-uv    # Install uv package manager
make setup         # Initialize project
make up            # Activate virtual environment
make down          # Deactivate virtual environment
make lock          # Update dependencies
make init          # Full initialization
```
## Workflow

Running `python main.py -id 2501 -p a -s s ` it will create and populate a script file in `25` directory 
with script file `1.py`. Also it will create a sample file in `input` directory named `1_sample_a.txt`. 
If running without a sample will also create a new input file named `1.txt`


## License

[MIT License](LICENSE)