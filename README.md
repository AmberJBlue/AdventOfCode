# Advent of Code Solutions 🎄

Welcome to my **Advent of Code 2024** solutions repository! This repository contains my solutions for the coding challenges from [Advent of Code](https://adventofcode.com/2024), a series of fun and challenging programming puzzles released daily in December.

---

## 📜 About Advent of Code

**Advent of Code (AoC)** is an annual event where programmers worldwide participate in solving creative puzzles that blend storytelling, logic, and programming. Each day from December 1st to 25th, a new two-part puzzle is unlocked at midnight EST.

These puzzles are designed to be:

- **Challenging:** A great way to hone your algorithmic and problem-solving skills.
- **Fun:** Each puzzle is wrapped in a festive holiday-themed story.
- **Accessible:** Suitable for beginners and experts alike, with increasing difficulty as the event progresses.

---

## 📂 Repository Structure

The repository is organized as follows:

```plaintext
/2024
├── day1/
│   ├── solution.py
│   ├── input.txt
│   ├── test_input.txt
│   └── README.md
├── day2/
│   ├── solution.py
│   ├── input.txt
│   ├── test_input.txt
│   └── README.md
...
├── utils/
│   ├── __init__.py
│   └── display_results.py
```

- Each day has its own directory containing:
  - **`solution.py`:** My solutions for each part of the puzzle.
  - **`input.txt`:** The puzzle input specific to my account.
  - **`test_input.txt`:** The test input for the given puzzle.
  - **`README.md`:** A description of the puzzle, solution explanation, and example walkthroughs.

---

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/AmberJBlue/AdventOfCode
   cd AdventOfCode
   ```
2. Navigate to a specific day's solution:
   ```bash
   cd 2024/day1
   ```
3. Run the solution script:
   - By default, the script runs for **Part 1** using `input.txt`:
     ```bash
     python solution.py
     ```
   - To specify **Part 2**, use the `--part` flag:
     ```bash
     python solution.py --part 2
     ```
   - To use the test input (`test_input.txt`), add the `--test` flag:
     ```bash
     python solution.py --test
     ```
   - Combine the `--part` and `--test` flags for testing Part 2:
     ```bash
     python solution.py --part 2 --test
     ```

---

## Fun Features & Easter Eggs

### ❄️ Let It Snow!

Activate a snowfall animation in the terminal with the `--snow` flag. You can also specify how long the snow lasts (in seconds):

```bash
python solution.py --snow 10
```

## 🎄 Join the Fun!

If you're interested in participating in **Advent of Code**, you can sign up for free at [adventofcode.com](https://adventofcode.com/2024). Whether you’re a seasoned programmer or just starting out, it’s a fantastic way to learn and grow.

Happy Coding and Happy Holidays! 🎅✨
