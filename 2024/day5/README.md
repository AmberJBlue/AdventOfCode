# Print Queue: Day 5 🎄

## Part I

### 📜 Problem Description

The search for the Chief Historian leads to **sub-basement 17**, where the North Pole's printing department is in full swing. While The Historians scour the stationery stacks, an Elf asks for your help fixing a malfunctioning printer tasked with producing safety manual updates.

The printer needs to ensure that pages are printed in a specific order, based on a set of rules. Each rule is written in the format **X|Y**, meaning **page X must be printed before page Y** if both pages are part of the update.

The Elf provides:

1. **Page ordering rules**: A list of constraints specifying the required order between pairs of pages.
2. **Updates**: Lists of pages that need to be printed, with varying page numbers in each update.

Your job is to determine which updates are **already in the correct order** based on the rules.

---

### 🔍 Example Walkthrough

#### Input Rules:

```plaintext
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
```

#### Updates:

```plaintext
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

#### Example Analysis:

1. **First Update: `75,47,61,53,29`**

   - **Valid**:
     - 75 comes before 47, 61, 53, and 29 as required.
     - 47 comes before 61, 53, and 29.
     - All other rules are satisfied.

2. **Fourth Update: `75,97,47,61,53`**

   - **Invalid**:
     - 97 must come before 75, but 75 is printed first (violates rule `97|75`).

3. **Correctly Ordered Updates:**
   - `75,47,61,53,29`
   - `97,61,53,29,13`
   - `75,29,13`

---

### 🛠️ Task

1. Validate each update against the page ordering rules:

   - Only consider rules that apply to the pages in the update.
   - Ensure all applicable rules are satisfied.

2. Find the **middle page number** of each correctly-ordered update:

   - For an odd-length update, this is the middle element.
   - For an even-length update, the middle page is the lower of the two middle values.

3. Add the middle page numbers together.

---

### 🔢 Input Format

1. The first section lists **page ordering rules** in the format `X|Y`.
2. The second section lists **updates**, with each update on a new line.

#### Example Input:

```plaintext
47|53
97|13
97|61
75,47,61,53,29
97,61,53,29,13
```

---

### 🔢 Output Format

A single integer: the sum of the middle page numbers from all correctly-ordered updates.

#### Example Output:

```plaintext
143
```

---

### 💡 Algorithm Overview

1. **Parse Input**:

   - Split the input into rules and updates.

2. **Validate Updates**:

   - For each update:
     - Filter the rules to include only those relevant to the pages in the update.
     - Check if the update satisfies all applicable rules.

3. **Find Middle Pages**:

   - For each valid update, determine the middle page number.

4. **Sum Middle Pages**:
   - Add up the middle page numbers of all valid updates.

---

### 🔍 Example Analysis

#### Valid Updates:

```plaintext
75,47,61,53,29 -> Middle: 61
97,61,53,29,13 -> Middle: 53
75,29,13       -> Middle: 29
```

#### Total:

```plaintext
61 + 53 + 29 = 143
```

---

### 🎯 Your Challenge

Help the Elf identify which updates are in the correct order, calculate the middle page numbers of those updates, and find their sum. Can you ensure the safety manuals are printed on time? 🎅✨

## Part II

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

```plaintext
75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
```

After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
