# Mull It Over: Day 3

## Part I
### 🎄 Introduction
At the **North Pole Toboggan Rental Shop**, the shopkeeper is having computer troubles. The Historians are busy searching the warehouse for any sign of the Chief Historian, leaving you to figure out why the computer is malfunctioning.

The computer's memory (your puzzle input) is corrupted, with valid instructions mixed in with junk data. Your task is to **scan the corrupted memory, identify valid multiplication instructions, and sum up the results of their calculations**.

---

### 🖥️ Problem Overview

#### Valid Instructions:
A valid instruction follows the format:

```plaintext
mul(X,Y)
```
Where:
- `mul` is the command.
- `X` and `Y` are integers (1 to 3 digits each).
- Parentheses and commas must be properly formatted without extra spaces.

#### Invalid Instructions:
Corrupted data contains invalid characters or malformed instructions, such as:
- **Extra characters**: `xmul(2,4)%&`
- **Missing commas**: `mul(32,64]`
- **Invalid parentheses**: `mul(6,9!`
- **Spaces within the instruction**: `mul ( 2 , 4 )`

#### Example Input:
```plaintext
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```

#### Example Analysis:
From the input above:
- Valid `mul` instructions:
  - `mul(2,4)` → Result: `2 * 4 = 8`
  - `mul(3,7)` → Result: `3 * 7 = 21`
  - `mul(11,8)` → Result: `11 * 8 = 88`
  - `mul(8,5)` → Result: `8 * 5 = 40`
- Sum of results: `8 + 21 + 88 + 40 = 161`

---

### 🛠️ Your Task

#### Input:
- A single string of corrupted memory data.

#### Output:
- The sum of the results of all valid `mul` instructions.

---

### 🔍 Steps to Solve
1. **Extract Valid `mul` Instructions**:
   - Use a regular expression to identify instructions matching the format `mul(X,Y)`.
   - Ensure `X` and `Y` are integers with 1 to 3 digits.

2. **Calculate Results**:
   - For each valid instruction, parse the integers `X` and `Y` and calculate `X * Y`.

3. **Sum the Results**:
   - Add up the results of all valid `mul` instructions.

---

#### Example Code (Python)
```python
import re

def sum_valid_muls(corrupted_memory):
    # Regular expression for valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate and sum results
    total = sum(int(x) * int(y) for x, y in matches)
    
    return total

# Example Input
corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Total Sum of Valid Multiplications
print(sum_valid_muls(corrupted_memory))  # Output: 161
```

---

### 🎯 Your Challenge
Given the corrupted memory data, implement the solution to extract valid `mul` instructions and calculate their total sum. Can you restore the computer's functionality and save the day? 🎅✨

## Part II

### 📜 Problem Description

As you continue scanning the corrupted memory, you notice that the program contains conditional instructions that modify whether `mul` operations are enabled. These new instructions can enable or disable `mul` commands, affecting the results. Here's what they do:

1. **`do()` Instruction**: Enables future `mul` instructions.
2. **`don't()` Instruction**: Disables future `mul` instructions.

At the start of the program, all `mul` instructions are enabled by default. However, only the most recent `do()` or `don't()` instruction applies, and any `mul` operations affected by a `don't()` instruction are ignored.

---

### 🔍 Example Walkthrough

Input:
```plaintext
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```

#### Explanation:
1. The program starts with `mul` enabled:
   - `mul(2,4)` is valid: \( 2 \times 4 = 8 \).
   - `mul(3,7)` is valid: \( 3 \times 7 = 21 \).
2. The `don't()` instruction disables future `mul` commands:
   - `mul(5,5)` is skipped.
   - `mul(32,64)` is skipped.
3. The `do()` instruction re-enables `mul` commands:
   - `mul(11,8)` is valid: \( 11 \times 8 = 88 \).
   - `mul(8,5)` is valid: \( 8 \times 5 = 40 \).

Final sum of results:  
\[ 8 + 21 + 40 = 48 \]

---

### 🛠️ Your Task

Modify the analysis to:
1. Identify and handle `do()` and `don't()` instructions.
2. Enable or disable future `mul` instructions based on the most recent conditional statement.
3. Calculate the total sum of results for only the enabled `mul` instructions.

---

### 🔢 Input Format

The input consists of a single line of corrupted memory, containing a mix of `mul(X,Y)` operations and `do()`/`don't()` instructions.

---

### 🔢 Output Format

The output should be the sum of all results for `mul` operations that were enabled.