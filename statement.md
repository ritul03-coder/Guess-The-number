# Guess The Number Game

## Project Statement

The **Guess The Number Game** is an interactive command-line application developed in Python. The objective of the project is to create a simple and engaging game in which the computer generates a random number between **1 and 100**, and the player attempts to guess the generated number.

After each valid guess, the program provides feedback to the player by indicating whether the guessed number is **too high** or **too low**. The game continues until the player successfully identifies the correct number.

The project demonstrates the practical implementation of several foundational programming concepts, including:

- Control Flow
- Loops
- User Input
- Data Type Conversion
- Exception Handling
- Random Number Generation
- State Management

---

## Problem Statement

Many beginner programmers understand individual programming concepts but may find it difficult to combine them into a complete interactive application.

This project addresses this challenge by developing a simple number-guessing game that integrates multiple Python concepts into one functional program.

The program should:

- Generate a random number between 1 and 100.
- Accept user guesses through the command line.
- Validate user input and handle invalid entries.
- Compare the guess with the generated number.
- Inform the user whether the guess is too high or too low.
- Count the number of valid attempts.
- Display a success message when the correct number is guessed.
- Evaluate the player's performance based on the number of attempts.

---

## Objectives

1. Develop an interactive command-line game using Python.
2. Implement loops and conditional statements.
3. Handle user input and data type conversion.
4. Use Python's `random` library.
5. Implement exception handling.
6. Track the number of attempts.
7. Provide immediate feedback to the player.
8. Combine multiple programming concepts into one application.

---

## Technologies Used

- **Programming Language:** Python
- **Library:** `random`
- **IDE:** Visual Studio Code
- **Interface:** Command-Line Interface (CLI)

---

## Key Programming Concepts

### Random Number Generation

```python
secret_number = random.randint(1, 100)