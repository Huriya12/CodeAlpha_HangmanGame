# CodeAlpha_HangmanGame
A simple text-based Hangman game built in Python as part of the CodeAlpha Programming Internship

## Description
A classic paper-and-pencil game turned text-based computer challenge, where a player must guess the letters of a hidden word one at a time. A word is randomly selected from a predefined list, and each incorrect guess brings the Hangman’s figure one step closer to completion. The player must guess all the correct letters to reveal the hidden word before running out of chances and completing the Hangman’s figure

## Features
- Randomly selects a word from a list of 5 predefined words
- Displays an ASCII Hangman drawing that updates with each incorrect guess
- Keeps track of guessed letters and prevents repeated attempts
- Validates input, accepting only a single letter at a time
- Show progress with dashes representing unguessed letters
- Detects wins and losses with a final reveal of the answer at the end
- Allows the player to replay the game as many times as they’d like

## Key Concepts
- Random module
- While Loops
- If-elif-else conditional statements
- Strings
- Lists
- Sets
- Functions

## Installation
1. Make sure Python 3 is installed on your machine. To check run:
```bash
python --version
```
2. Clone the repository:
```bash
git clone https://github.com/Huriya12/CodeAlpha_HangmanGame.git
```
3. Move into the project folder:
```bash
cd CodeAlpha_HangmanGame
```

## How to use:
1. Run the script in your terminal:
```bash
python hangman_game.py
```
2. Type ‘yes’ when asked if you’re ready to play
3. Guess letter one at a time
4. Win by guessing the full word, or lose if you run out of chances
5. Type ‘yes’ to play again, or ‘no’ if you wish to quit.

## Author
Huriya Zafar | https://github.com/Huriya12

