# Bridge Repair: Day 7 🎄

## Part I

### 📜 Problem Description

The Historians arrive at a familiar rope bridge in the jungle, but it’s in disrepair! A group of engineers is trying to fix the bridge but is stuck because the calibration equations for the repair are missing operators. The engineers need your help to figure out which test values in the calibration equations can be made valid by inserting operators.

Each equation has the following format:

```plaintext
<test_value>: <number_1> <number_2> ... <number_n>
```

The goal is to determine whether it is possible to insert the operators `+` (addition) and `*` (multiplication) between the numbers such that the result equals the `test_value`.

### Rules:

- Operators are evaluated **left-to-right** (not by standard operator precedence).
- Numbers in the equations **cannot be rearranged**.
- Only two operators are available: `+` and `*`.

---

### 🔍 Example Walkthrough

#### Input:

```plaintext
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

#### Analysis:

1. **190: 10 19**

   - Operators can only be placed between `10` and `19`.
   - `10 + 19 = 29` (not valid).
   - `10 * 19 = 190` (valid).

2. **3267: 81 40 27**

   - Operators can be placed between `81`, `40`, and `27`.
   - Valid configurations:
     - `81 + 40 * 27 = 3267`.
     - `81 * 40 + 27 = 3267`.

3. **292: 11 6 16 20**
   - Operators can be placed between `11`, `6`, `16`, and `20`.
   - Valid configuration:
     - `11 + 6 * 16 + 20 = 292`.

---

### 🛠️ Task

1. **Input:** A list of calibration equations.
2. **Output:** The total sum of the test values that can be made valid by inserting operators.

#### Example Input:

```plaintext
190: 10 19
3267: 81 40 27
292: 11 6 16 20
```

#### Example Output:

```plaintext
3749
```

---

### 🔢 Input Format

Each line of the input represents a calibration equation in the format:

```plaintext
<test_value>: <number_1> <number_2> ... <number_n>
```

---

### 💡 Algorithm Overview

1. **Parse Input:**

   - Extract the `test_value` and the sequence of numbers for each equation.

2. **Simulate Operator Insertion:**

   - Generate all possible combinations of `+` and `*` operators for the given numbers.
   - Evaluate each combination **left-to-right** to see if it equals the `test_value`.

3. **Sum Valid Test Values:**
   - If a combination produces the `test_value`, add it to the total calibration result.

---

### 🎯 Output Format

The program should output the sum of all `test_values` from valid equations.

---

### 🔍 Example Analysis

#### Input:

```plaintext
190: 10 19
3267: 81 40 27
292: 11 6 16 20
```

#### Output:

```plaintext
3749
```

The valid equations are:

- `190: 10 * 19`
- `3267: 81 + 40 * 27` or `81 * 40 + 27`
- `292: 11 + 6 * 16 + 20`

---

### 🎄 Your Challenge

Help the engineers determine which calibration equations are valid and calculate the total calibration result. Can you restore the bridge and continue the search for the Chief Historian? 🚧✨
