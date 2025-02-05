# Rock-Paper-Scissors Game

## Description
This is a simple command-line Rock-Paper-Scissors game implemented in Python. The user plays against the computer, which randomly selects one of the three choices: Rock, Paper, or Scissors. The game determines the winner based on the standard rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both choices are the same, it's a tie.

## Features
- User inputs their choice (Rock, Paper, or Scissors) using numbers 1, 2, or 3.
- The computer randomly selects a choice.
- The program determines the winner and displays the result.
- If an invalid input is provided, the program exits with an error message.

## Installation
Ensure you have Python installed on your system. This script does not require any additional libraries apart from Python's built-in modules.

## Usage
1. Run the script using Python:
   ```bash
   python rps_game.py
   ```
2. Enter your choice:
   - 1 for Rock
   - 2 for Paper
   - 3 for Scissors
3. The game will compare your choice with the computer's and display the result.

## Code Breakdown
- The `RPS` Enum defines the choices.
- The player is prompted to enter a number (1, 2, or 3).
- The computer randomly selects a choice.
- The choices are compared to determine the winner.
- The result is displayed to the user.

## Example Output
```
Enter...
1 for rock
2 for paper, or
3 for Scissors:

2

you choose PAPER.
python choose ROCK.

you win!
```

## Improvements
- Add a loop to allow multiple rounds of play.
- Implement score tracking.
- Enhance input validation and error handling.

## Author
Ayşe Türk

