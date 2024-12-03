# Red-Nosed Reports: Day 2

## 🎄 Introduction
After leaving the Chief Historian's office, The Historians’ next search brings them to the **Red-Nosed Reindeer nuclear fusion/fission plant**. While there’s no sign of the Chief Historian here, the engineers at the plant are in need of assistance analyzing some **unusual data** from the reactor.

You step in to help while The Historians explore the facility.

---

## 🕵️ Problem Overview

### The Data:
The unusual data (your puzzle input) consists of multiple **reports**, where each report is a list of **levels** represented as numbers separated by spaces. For example:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

### Safety Rules:
A report is **safe** if **both** of the following rules are true:
1. **Monotonicity**: The levels must either be:
   - All **increasing** (each number is greater than the one before), or
   - All **decreasing** (each number is less than the one before).
2. **Adjacent Differences**: The difference between any two adjacent levels must be **at least 1 and at most 3**.

---

## 🧮 Example Analysis
Using the sample input provided:

### Reports:
1. `7 6 4 2 1`: **Safe**
   - Monotonicity: All levels are **decreasing**.
   - Differences: `|7 - 6| = 1`, `|6 - 4| = 2`, `|4 - 2| = 2`, `|2 - 1| = 1` (all between 1 and 3).

2. `1 2 7 8 9`: **Unsafe**
   - Monotonicity: Levels are **increasing**.
   - Differences: `|1 - 2| = 1`, `|2 - 7| = 5` (violates the difference rule).

3. `9 7 6 2 1`: **Unsafe**
   - Monotonicity: Levels are **decreasing**.
   - Differences: `|9 - 7| = 2`, `|7 - 6| = 1`, `|6 - 2| = 4` (violates the difference rule).

4. `1 3 2 4 5`: **Unsafe**
   - Monotonicity: Levels are neither all increasing nor all decreasing.

5. `8 6 4 4 1`: **Unsafe**
   - Differences: `|4 - 4| = 0` (violates the difference rule).

6. `1 3 6 7 9`: **Safe**
   - Monotonicity: All levels are **increasing**.
   - Differences: `|1 - 3| = 2`, `|3 - 6| = 3`, `|6 - 7| = 1`, `|7 - 9| = 2` (all between 1 and 3).

### Results:
- **2 reports** are safe (`7 6 4 2 1` and `1 3 6 7 9`).

---

## 🛠️ Your Task

### Input:
- A list of reports, where each report is a space-separated list of numbers.

### Output:
- The total number of **safe reports**.

---

### Example Code (Python)
```python
def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]
    
    # Check adjacent differences rule
    if any(diff < 1 or diff > 3 for diff in differences):
        return False
    
    # Check monotonicity
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    return increasing or decreasing

def count_safe_reports(data):
    return sum(1 for report in data if is_safe(report))

# Example Input
data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9"
]

# Count Safe Reports
print(count_safe_reports(data))  # Output: 2
```

---

## 🎯 Your Challenge
Analyze the unusual data from the engineers and determine how many reports are **safe** based on the given rules. Can you ensure the reactor's safety before Christmas? 🎅✨