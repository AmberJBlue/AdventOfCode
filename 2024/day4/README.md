# Ceres Search: Day 4 🎄

## Part I

### 📜 Problem Description

The search for the Chief Historian takes you to the **Ceres monitoring station**, where a small Elf asks for your help with a word search puzzle. She needs to find every instance of the word **XMAS** in her puzzle. The word can appear in any direction:

- **Horizontal** (left-to-right or right-to-left)
- **Vertical** (top-to-bottom or bottom-to-top)
- **Diagonal** (in any direction)
- Words may **overlap**.

Your goal is to count all instances of **XMAS** in the Elf's word search.

---

### 🔍 Example Walkthrough

#### Input Word Search:

```plaintext
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

#### How to Identify XMAS:

In the word search:

- Words may overlap.
- Words can be found in **any direction**.

The word **XMAS** occurs **18 times** in total. Below is a representation of the word search with irrelevant characters replaced by `.`:

```plaintext
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

---

### 🛠️ Task

1. Write a program to identify all instances of **XMAS** in a grid.
2. Consider all possible directions for the word:

   - Horizontal (left-to-right and right-to-left)
   - Vertical (top-to-bottom and bottom-to-top)
   - Diagonal (all four possible diagonals)

3. Return the total number of times **XMAS** appears.

---

### 🔢 Input Format

The input is a square or rectangular grid of letters, where each line represents one row of the grid.

### Example Input:

```plaintext
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

---

### 🔢 Output Format

Output a single integer, representing the total number of times **XMAS** appears in the grid.

#### Example Output:

```plaintext
18
```

---

### 💡 Algorithm Overview

1. **Directions to Search:**

   - Define all possible directions as coordinate pairs for moving through the grid.
   - Horizontal: (0, 1), (0, -1)
   - Vertical: (1, 0), (-1, 0)
   - Diagonal: (1, 1), (1, -1), (-1, 1), (-1, -1)

2. **Iterate Through Grid:**

   - Start at each cell in the grid and search in all directions for **XMAS**.

3. **Count Matches:**

   - Keep a running total of all matches found.

4. **Edge Handling:**
   - Ensure no out-of-bounds errors when searching near the grid's edges.

---

### 🔍 Example Analysis

#### Input:

```plaintext
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

#### Output:

```plaintext
18
```

The word **XMAS** is found 18 times in various directions.

---

### 🎯 Your Challenge

Analyze the Elf's word search and count how many times **XMAS** appears. Can you solve the puzzle and help her finish her task? 🎅✨

## Part II

### 📜 Problem Description

The Elf looks at you quizzically—did you misunderstand the assignment?

Looking for further instructions, you flip over the word search and discover that this isn’t an **XMAS** puzzle but an **X-MAS** puzzle! You’re supposed to find **two MAS patterns in the shape of an X**. Each **MAS** can be written forwards or backwards. For example:

```
M.S
.A.
M.S
```

Irrelevant characters have been replaced with `.` in the diagram above.

---

### 🔍 Example Walkthrough

Here’s the same example word search from before, but this time all of the **X-MAS** patterns have been kept:

```
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```

In this example, an **X-MAS** pattern appears **9 times**.

---

### 🎯 Task

Flip the word search back over and try again. **How many times does an X-MAS pattern appear in the grid?**
