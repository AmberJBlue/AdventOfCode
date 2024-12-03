# Red-Nosed Reports: Day 2

## Part I 
### 🎄 Introduction
After leaving the Chief Historian's office, The Historians’ next search brings them to the **Red-Nosed Reindeer nuclear fusion/fission plant**. While there’s no sign of the Chief Historian here, the engineers at the plant are in need of assistance analyzing some **unusual data** from the reactor.

You step in to help while The Historians explore the facility.

---

### 🕵️ Problem Overview

#### The Data:
The unusual data (your puzzle input) consists of multiple **reports**, where each report is a list of **levels** represented as numbers separated by spaces. For example:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

#### Safety Rules:
A report is **safe** if **both** of the following rules are true:
1. **Monotonicity**: The levels must either be:
   - All **increasing** (each number is greater than the one before), or
   - All **decreasing** (each number is less than the one before).
2. **Adjacent Differences**: The difference between any two adjacent levels must be **at least 1 and at most 3**.

---

### 🧮 Example Analysis
Using the sample input provided:

#### Reports:
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

#### Results:
- **2 reports** are safe (`7 6 4 2 1` and `1 3 6 7 9`).

---

### 🛠️ Your Task

#### Input:
- A list of reports, where each report is a space-separated list of numbers.

#### Output:
- The total number of **safe reports**.

---

#### Example Code (Python)
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

### 🎯 Your Challenge
Analyze the unusual data from the engineers and determine how many reports are **safe** based on the given rules. Can you ensure the reactor's safety before Christmas? 🎅✨

## Part II 

### 📜 Problem Description
The engineers were surprised by the low number of safe reports until they remembered the **Problem Dampener**, a reactor-mounted module that allows the safety systems to tolerate a **single bad level** in an otherwise unsafe report. This means that **removing one bad level** can make an unsafe report safe.

#### Updated Rules:
1. The levels must still follow the original rules:
   - Either **all increasing** or **all decreasing**.
   - Any two adjacent levels must differ by at least 1 and at most 3.
2. If removing **one level** from an unsafe report would make it safe, the report is now considered safe.

---

### 🔍 Example Walkthrough

Here are the same example reports:

| Report            | Status                              |
|--------------------|-------------------------------------|
| `7 6 4 2 1`       | Safe without removing any level.   |
| `1 2 7 8 9`       | Unsafe regardless of removal.      |
| `9 7 6 2 1`       | Unsafe regardless of removal.      |
| `1 3 2 4 5`       | Safe by removing the second level, `3`. |
| `8 6 4 4 1`       | Safe by removing the third level, `4`. |
| `1 3 6 7 9`       | Safe without removing any level.   |

#### Updated Safe Reports:
With the Problem Dampener, **4 reports** are considered safe:
1. `7 6 4 2 1` (already safe)
2. `1 3 2 4 5` (made safe by removing `3`)
3. `8 6 4 4 1` (made safe by removing `4`)
4. `1 3 6 7 9` (already safe)

---

### 🛠️ Your Task
1. Analyze the reports to identify **safe** and **unsafe** ones based on the original rules.
2. For each unsafe report, determine if removing a single level would make it safe.
3. Update the count of safe reports to include those fixed by the Problem Dampener.

---

### 💡 Input Format
The input consists of multiple reports, one per line, where each report is a sequence of space-separated integers.

Example:
```plaintext
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

---

### 🔢 Output Format
The output should be the total number of **safe reports**, including those fixed by the Problem Dampener.

Example Output:
```plaintext
4
```

---

### 🧮 Algorithm Overview
1. **Check Original Rules:**
   - Identify reports that are already safe using the original criteria.
2. **Simulate Level Removal:**
   - For each unsafe report, remove one level at a time and recheck if the modified report is safe.
3. **Count Safe Reports:**
   - Include both originally safe reports and those fixed by the Problem Dampener.

---

### 🔍 Example Analysis

Input:
```plaintext
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

Output:
```plaintext
4
```

Explanation:
- Reports `7 6 4 2 1` and `1 3 6 7 9` are already safe.
- Reports `1 3 2 4 5` and `8 6 4 4 1` are made safe by removing one level.
- Reports `1 2 7 8 9` and `9 7 6 2 1` remain unsafe regardless of removal.

---

### 🎯 Your Challenge
Update your analysis to include the **Problem Dampener** logic and determine the total number of safe reports. Can you solve it and ensure reactor safety? 🎅✨