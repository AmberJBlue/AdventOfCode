# Guard Gallivant: Day 6 🎄

## Part I

### 📜 Problem Description

The search for the Chief Historian takes you to the **North Pole prototype suit manufacturing lab** in the year **1518**. The Historians are using their time-traveling device to access history directly, but they must avoid anyone from 1518 while searching. Unfortunately, a **single guard** is patrolling the area, so you must predict their movements to ensure the Historians' safety.

You are given a **map** of the lab, where:

- The guard's current position and facing direction are marked with `^` (facing up), `>`, `<`, or `v`.
- Obstructions like crates and desks are marked with `#`.
- Empty spaces are represented by `.`.

The guard follows a strict patrol protocol:

1. **If there is an obstruction directly ahead**, the guard will turn **90 degrees right**.
2. **Otherwise, the guard will take a step forward**.

Your task is to predict the guard's patrol path and determine how many distinct positions they will visit before leaving the mapped area. The guard's starting position counts as a visited position.

---

### 🔍 Example Walkthrough

#### Input Map:

```plaintext
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

#### Step-by-Step Guard Movements:

1. Starting at `^` (facing up), the guard moves upward until encountering an obstacle:
   ```plaintext
   ....#.....
   ....^....#
   ..........
   ..#.......
   .......#..
   ..........
   .#........
   ........#.
   #.........
   ......#...
   ```
2. The guard turns **90 degrees right** and moves to the right:
   ```plaintext
   ....#.....
   ........>#
   ..........
   ..#.......
   .......#..
   ..........
   .#........
   ........#.
   #.........
   ......#...
   ```
3. The guard encounters another obstacle, turns **90 degrees right** again, and moves downward:
   ```plaintext
   ....#.....
   .........#
   ..........
   ..#.......
   .......#..
   ..........
   .#......v.
   ........#.
   #.........
   ......#...
   ```
4. This process continues until the guard leaves the mapped area.

#### Final Map with Patrol Path Marked (`X` for visited positions):

```plaintext
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

In this example, the guard visits **41 distinct positions** before leaving the map.

---

### 🔢 Input Format

The input consists of a rectangular grid of characters:

- `#`: Obstructions
- `.`: Empty spaces
- `^`, `>`, `<`, `v`: The guard's starting position and direction

---

### 🔢 Output Format

Output a single integer, representing the total number of distinct positions the guard visits, including the starting position.

#### Example Output:

```plaintext
41
```

---

### 💡 Algorithm Overview

1. **Input Parsing**:

   - Read the grid and identify the guard's initial position and direction.
   - Store the map dimensions for boundary checking.

2. **Simulate Patrol**:

   - Repeat the patrol protocol until the guard leaves the grid:
     1. Check the cell in front of the guard based on their current direction.
     2. Turn **90 degrees right** if there’s an obstruction or boundary ahead; otherwise, move forward.

3. **Track Visited Positions**:

   - Keep a set of all distinct positions the guard visits.

4. **Output Result**:
   - Return the total number of positions in the visited set.

---

### 🔍 Example Analysis

#### Input:

```plaintext
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

#### Output:

```plaintext
41
```

The guard visits **41 distinct positions** before leaving the grid.

---

### 🎯 Your Challenge

Predict the path of the guard and calculate how many distinct positions they visit before leaving the mapped area. Can you navigate the guard safely through history? 🎅✨

---

## Part II

### 📜 Problem Description

While The Historians begin working around the guard's patrol route, you decide to step outside the lab and use their time-traveling device to gather data. After recording the nightly status of the lab's guard post over several months, you return to The Historians with a new idea: to place a **single new obstruction** in the lab.

This obstruction must be positioned to cause the guard to get stuck in a **loop**, ensuring the rest of the lab is safe to search. The obstruction cannot be placed at the guard's starting position, as the guard would immediately notice.

Your task is to determine **how many different positions** could be used for the new obstruction while ensuring:

1. The guard gets stuck in a loop.
2. The obstruction placement avoids creating a time paradox.

---

### 🔍 Example Walkthrough

Using the previous example map, there are **6 different positions** where a new obstruction would cause the guard to get stuck in a loop. Here are diagrams for these six positions, with:

- `O` marking the obstruction,
- `|` showing positions where the guard moves up/down,
- `-` showing positions where the guard moves left/right,
- `+` showing positions where the guard moves both up/down and left/right.

#### Example Obstruction Positions:

1. Place an obstruction next to the guard's starting position:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ....|..#|.
   ....|...|.
   .#.O^---+.
   ........#.
   #.........
   ......#...
   ```
2. Place an obstruction in the bottom right quadrant:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ......O.#.
   #.........
   ......#...
   ```
3. Place an obstruction next to the standing desk in the bottom right quadrant:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   .+----+O#.
   #+----+...
   ......#...
   ```
4. Place an obstruction near the bottom left corner:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ..|...|.#.
   #O+---+...
   ......#...
   ```
5. Place an obstruction slightly to the right of the bottom left corner:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ....|.|.#.
   #..O+-+...
   ......#...
   ```
6. Place an obstruction next to the tank of universal solvent:
   ```plaintext
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   .+----++#.
   #+----++..
   ......#O..
   ```

---

### 🔢 Output Format

Output a single integer, representing the **number of possible obstruction positions** that will trap the guard in a loop.

#### Example Output:

```plaintext
6
```

---

### 🎯 Your Challenge

Determine all the valid positions for a single new obstruction that traps the guard in a loop. How many options do you have? 🕵️‍♂️🎄
