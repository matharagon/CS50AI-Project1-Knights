# Knights and Knaves Puzzle Solver
This is a Python implementation of the classic Knights and Knaves puzzles, developed as part of CS50AI's Project1.

# Problem Description
In the Knights and Knaves puzzles, there are two types of characters: knights, who always tell the truth, and knaves, who always lie. The puzzles involve a group of these characters making statements about themselves and others, and the goal is to determine which characters are knights and which are knaves.

This implementation provides a solver for four different puzzles of varying difficulty, each with a different set of statements made by the characters:

* A says "I am both a knight and a knave."
* A says "We are both knaves." B says nothing.
* A says "We are the same kind." B says "We are of different kinds."
* A says either "I am a knight." or "I am a knave.", but you don't know which. B says "A said 'I am a knave'." B says "C is a knave." C says "A is a knight."

# Solution Strategy

This implementation uses propositional logic to represent the statements made by the characters, and a logical reasoning algorithm based on knowledge levels to determine the type of each character. The knowledge levels range from 0 to 3, where:

* Knowledge level 0: a character knows nothing about the truthfulness of any statement.
* Knowledge level 1: a character knows the truthfulness of a statement made by another character.
* Knowledge level 2: a character knows the truthfulness of a statement made by another character who knows the truthfulness of another statement made by a third character.
* Knowledge level 3: a character knows the truthfulness of a statement made by another character who knows the truthfulness of a statement made by a third character who knows the truthfulness of a statement made by the first character.
By applying the logical reasoning algorithm based on knowledge levels, the solver is able to determine the type of each character in each puzzle.

How to Use
To run the solver for a specific puzzle, execute the following command:

```python puzzle.py```
The solver will then output the solution, which consists of a list of the characters and their types (knight or knave).

# Project Structure
The repository contains the following files:

* `puzzle.py`: the main file that runs the solver
* `knights.py`: the implementation of the Knights and Knaves puzzle logic and sentence representation
* `README.md`: this file

# Contributing
Contributions to the solver are welcome! If you have any suggestions or find any bugs, feel free to open an issue or submit a pull request.
