# Resonant Collinearity: Day 8 🎄

## Part I

### 📜 Problem Description

You find yourself on the roof of a top-secret Easter Bunny installation where a network of antennas is broadcasting a signal tuned to specific frequencies. Each antenna's frequency is represented by a lowercase letter, uppercase letter, or digit. These antennas generate **antinodes**, which are points of signal interference that can influence behavior.

An **antinode** is created by two antennas with the same frequency under these conditions:

1. The antennas are perfectly **collinear** (aligned along a straight line).
2. One antenna is **twice as far away** from the antinode as the other.

Each pair of antennas with the same frequency generates **two antinodes**, one on each side of the pair. If there are multiple antennas of the same frequency, additional antinodes may overlap or extend beyond the map.

---

### 🔍 Example Walkthrough

#### Example Input:

```plaintext
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
```

#### How Antinodes Are Generated:

1. **Frequency Matching:**

   - Only antennas with the **same frequency** contribute to antinodes.
   - Antennas with different frequencies, such as `A` and `a`, do not interact.

2. **Collinear Antinodes:**
   - For antennas `a` and `a`, two antinodes are created:
     - One on the line extending outward past the farther antenna.
     - One on the line extending inward between the two antennas.

#### Example Output with Antinodes:

```plaintext
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
```

In this example:

- **Unique Antinode Locations:** 14 within the bounds of the map.

---

### 🛠️ Task

Write a program to calculate the total number of **unique locations within the bounds of the map** that contain an antinode.

---

### 🔢 Input Format

The input is a grid of characters:

- **`.`** represents empty space.
- Antennas are represented by their frequencies (`a-z`, `A-Z`, `0-9`).

#### Example Input:

```plaintext
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
```

---

### 🔢 Output Format

Output a single integer, the total number of **unique antinode locations**.

#### Example Output:

```plaintext
14
```

---

### 💡 Algorithm Overview

1. **Parse Input:**

   - Extract positions and frequencies of antennas from the map.

2. **Check Collinearity:**

   - For each pair of antennas with the same frequency:
     - Verify if they are collinear and satisfy the distance condition for an antinode.

3. **Calculate Antinodes:**

   - Generate the two potential antinode positions for each valid antenna pair.
   - Ensure positions are within the bounds of the map.

4. **Count Unique Antinodes:**
   - Store antinode positions in a set to count only unique locations.

---

### 🔍 Example Analysis

#### Input:

```plaintext
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
```

#### Output:

```plaintext
14
```

The example map produces **14 unique antinode locations**.

---

### 🎯 Your Challenge

Determine the total number of unique antinode locations within the bounds of the map caused by the network of antennas. Can you help mitigate the Easter Bunny's nefarious plans? 🐰✨
