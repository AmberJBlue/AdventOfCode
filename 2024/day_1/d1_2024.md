# Historian Hysteria: Day 1

## 🎄 Introduction
The Chief Historian of the North Pole has mysteriously disappeared, leaving a group of Senior Historians in disarray. As the big Christmas sleigh launch approaches, the Chief Historian’s presence is crucial, but nobody has seen him for months! 

Rumor has it he was visiting historically significant locations around the North Pole. The Senior Historians have tasked you with helping them search for him, starting with the first 50 places they believe he might have visited.

Your mission is to **collect 50 stars** by solving puzzles, ensuring Christmas is saved before Santa takes off on December 25th. Each day in the Advent calendar presents **two puzzles**, with the second puzzle unlocking after completing the first. Each puzzle earns you one star. Good luck!

---

## 🕵️ The Mystery Begins
The Historians have already encountered their first challenge: their list of locations to search is empty! After some deliberation, they decide to start by checking the **Chief Historian's office**.

Upon investigation, they confirm the Chief Historian is not in his office. However, they discover an assortment of notes and lists detailing historically significant locations, identified by **unique location IDs**. The Senior Historians divide into two groups to compile a complete list, but there’s a problem: 

**The two lists are not very similar!** 

You are tasked with reconciling these lists to determine the total distance between them.

---

## 📋 Problem Description

### Example Input:
Here are the two lists of location IDs:

| Left List | Right List |
|-----------|------------|
| 3         | 4          |
| 4         | 3          |
| 2         | 5          |
| 1         | 3          |
| 3         | 9          |
| 3         | 3          |

### Goal:
1. **Pair the numbers** from both lists such that the smallest number in the left list pairs with the smallest number in the right list, the second smallest with the second smallest, and so on.
2. **Calculate the distance** between each pair:
   - Distance = |Left Number - Right Number|
3. **Sum up all distances** to find the total distance.

---

## 🧮 Example Walkthrough
Using the example lists above:

| Pair         | Distance |
|--------------|----------|
| (1, 3)       | 2        |
| (2, 3)       | 1        |
| (3, 3)       | 0        |
| (3, 4)       | 1        |
| (3, 5)       | 2        |
| (4, 9)       | 5        |

### Total Distance:
\[ 2 + 1 + 0 + 1 + 2 + 5 = 11 \]

---

## 🛠️ Your Task
Given the actual left and right lists of location IDs (your puzzle input):

1. Sort both lists.
2. Pair the numbers from smallest to largest.
3. Calculate the total distance between the lists by summing the distances for each pair.

---

### Example Code Snippet (Python)
```python
def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate distances
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

# Example Input
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# Total Distance
print(calculate_total_distance(left_list, right_list))  # Output: 11
```

---

## 🔍 Your Challenge
Using the provided input data, determine the total distance between the two lists. Can you reconcile the lists and help save Christmas? 🎅✨