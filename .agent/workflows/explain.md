---
description: Explain and clarify problem statement only
---

# Explain Problem Workflow

## Purpose

Provide a comprehensive explanation of what the problem is asking for, WITHOUT revealing solutions, approaches, or patterns. This workflow is for when you need to deeply understand the problem requirements before attempting to solve it.

## When to Use

- 📖 First time reading a problem and need clarification
- 🤔 Problem statement seems confusing or ambiguous
- ✅ Want to verify your understanding before coding
- 🎯 Need to identify all edge cases and constraints
- 📝 Want to break down a complex problem into simpler parts

## What This Workflow Does

✅ **DOES:**

- Explain what the problem is asking in simple terms
- Break down inputs, outputs, and constraints
- Walk through examples step-by-step
- Identify edge cases and boundary conditions
- Clarify any ambiguous wording
- Rephrase the problem in different ways

❌ **DOES NOT:**

- Reveal solution approaches or patterns
- Discuss algorithms or data structures
- Show code implementations
- Analyze time/space complexity
- Give hints about how to solve it

## Workflow Steps

### 1. Read Problem File

- Extract the problem statement
- Note the difficulty and pattern (but don't discuss the pattern yet)
- Identify the source (LeetCode, NeetCode, etc.)

### 2. What Are We Given? (Inputs)

Break down the inputs:

- **Data types:** What types of data are we working with?
- **Format:** How is the data structured?
- **Size/Range:** What are the constraints on input size?
- **Special properties:** Is it sorted? Can it have duplicates? Empty?

**Example:**

```
Input: nums = [100,4,200,1,3,2], target = 5

What we're given:
- Array of integers called 'nums'
- Can contain positive, negative, or zero
- May have duplicates (not specified, so assume yes)
- Length can be from 0 to 10^4 (check constraints)
- Array is NOT sorted
- Separate integer 'target'
```

### 3. What Are We Asked to Find? (Output)

Clarify the expected output:

- **Return type:** What exactly should we return?
- **Format:** Single value? Array? Boolean? Object?
- **Specific requirements:** All solutions? First solution? Count?
- **Return value constraints:** Any limits on the output?

**Example:**

```
Output: Return the LENGTH of the longest consecutive sequence

What we need to return:
- An integer (not the sequence itself, just its length!)
- If no consecutive sequence exists, return... (check edge cases)
- If array is empty, return 0
```

### 4. What Does This Problem Really Mean?

Rephrase the problem in the simplest possible terms:

**Template:**

```
In everyday language:
"We have [input description]. We need to find/return [output description]."

More specifically:
"[Detailed explanation of what 'consecutive sequence' or key term means]"

Important distinction:
"We are NOT asked to [common misconception]"
```

### 5. Understand Constraints

List ALL constraints and what they mean:

```
Constraints:
1. 0 <= nums.length <= 10^4
   → Means: Can be empty! Array can be very large (10,000 elements)

2. -10^9 <= nums[i] <= 10^9
   → Means: Numbers can be negative, zero, or positive
   → Means: Very large range, cannot use array indexing

3. Must work in O(n) time
   → Means: Can only loop through array a constant number of times
   → Means: Cannot use nested loops
```

### 6. Walk Through Examples

Take EACH example and trace through it step-by-step:

**Example 1:**

```
Input: nums = [100, 4, 200, 1, 3, 2]

Step 1: What consecutive sequences exist?
  - 1, 2, 3, 4 (length 4)
  - 100 (length 1)
  - 200 (length 1)

Step 2: Which is longest?
  - 1, 2, 3, 4 has length 4

Output: 4 ✓

Why this works:
- 1, 2, 3, 4 are consecutive (differ by 1)
- Order in array doesn't matter [100, 4, 200, 1, 3, 2]
- We found them by recognizing the pattern
```

**Example 2:**

```
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Step 1: Identify all numbers present
  - 0, 1, 2, 3, 4, 5, 6, 7, 8
  - Note: 0 appears twice

Step 2: Find consecutive sequences
  - 0, 1, 2, 3, 4, 5, 6, 7, 8 (length 9!)

Output: 9 ✓

Key insight from this example:
- Duplicates don't break the sequence
- The sequence can include the entire array
```

### 7. Identify Edge Cases

List ALL edge cases and what should happen:

```
Edge Case 1: Empty Array
  Input: []
  Expected: 0 (no elements = no sequence)

Edge Case 2: Single Element
  Input: [5]
  Expected: 1 (one element = sequence of length 1)

Edge Case 3: No Consecutive Numbers
  Input: [10, 20, 30]
  Expected: 1 (each number is its own sequence)

Edge Case 4: All Same Number
  Input: [5, 5, 5, 5]
  Expected: 1 (duplicates don't extend sequence)

Edge Case 5: Negative Numbers
  Input: [-2, -1, 0, 1]
  Expected: 4 (consecutive works with negatives)

Edge Case 6: All Consecutive
  Input: [1, 2, 3, 4, 5]
  Expected: 5 (entire array is one sequence)
```

### 8. Common Misconceptions

Clarify what the problem is NOT asking:

```
❌ MISCONCEPTION 1: "The elements must be in consecutive positions in the array"
✅ REALITY: Order in the array doesn't matter. [1, 5, 2, 3] contains sequence [1,2,3]

❌ MISCONCEPTION 2: "We need to return the actual sequence"
✅ REALITY: We only return the LENGTH, not the numbers themselves

❌ MISCONCEPTION 3: "Duplicates create longer sequences"
✅ REALITY: [1, 1, 2, 3] has a sequence 1→2→3 (length 3), not 1→1→2→3

❌ MISCONCEPTION 4: "We need to sort the array"
✅ REALITY: Problem says O(n), sorting would be O(n log n) - not allowed!

❌ MISCONCEPTION 5: "Consecutive means next to each other in the array"
✅ REALITY: Consecutive means differing by 1 in VALUE (continuous numbers)
```

### 9. Clarifying Questions

Ask questions that help understand requirements:

```
Q1: If the array is empty, what should we return?
A: 0 (specified in constraints or implied)

Q2: Can numbers be negative?
A: Yes, constraints show -10^9 to 10^9

Q3: Can there be duplicates?
A: Not explicitly forbidden, so yes

Q4: Do we need to return the actual sequence or just the length?
A: Just the length (check output specification)

Q5: If there are multiple sequences of the same max length, does it matter which?
A: No, we only return the length, not the sequence itself

Q6: Must the solution be optimal?
A: Yes, O(n) time constraint means we need an efficient solution
```

### 10. Summary of Understanding

Provide a concise summary:

```
📋 PROBLEM SUMMARY:

Given: An unsorted array of integers (possibly with duplicates)
Find: Length of longest sequence of consecutive integers
Consecutive means: Numbers that differ by exactly 1 (e.g., 5→6→7)

Key points:
1. Order in array doesn't matter
2. Only return LENGTH, not the sequence
3. Must be O(n) time (stated in constraints)
4. Duplicates are allowed but don't extend sequences
5. Empty array → return 0
6. Single element → return 1

Example mental model:
If you have [5, 1, 3, 2, 10], you can form:
- 1→2→3 (length 3)
- 5 (length 1)
- 10 (length 1)
Longest is 3, so return 3.
```

## Output Format

Present the explanation as:

```markdown
# 🔍 Problem Explanation: [Problem Name]

## 📥 What Are We Given? (Inputs)

[Detailed breakdown of inputs]

## 📤 What Are We Asked to Find? (Output)

[Clear explanation of expected output]

## 🎯 What Does This Mean in Simple Terms?

[Rephrase problem in everyday language]

## 📏 Constraints & What They Mean

[List constraints with implications]

## 📚 Example Walkthroughs

### Example 1: [Description]

[Step-by-step trace]

### Example 2: [Description]

[Step-by-step trace]

## ⚠️ Edge Cases to Consider

[Comprehensive list of edge cases]

## ❌ Common Misconceptions

[What the problem is NOT asking]

## ❓ Clarifying Questions

[Important questions and answers]

## 📋 Summary

[Concise summary of understanding]

---

**Next Steps:**

- ✅ If you understand the problem: Try solving on your own or use `/learn` for hints
- 🤔 If still confused: Ask specific questions about what's unclear
- 📝 If ready to see solutions: Use `/learn` for guided learning
```

## Success Criteria

User should be able to:

- ✅ Explain the problem to someone else in their own words
- ✅ Identify all edge cases
- ✅ Understand what the output should be for any given input
- ✅ Recognize common mistakes/misconceptions
- ✅ Feel confident they understand WHAT the problem is asking (not HOW to solve it)

## Important Notes

**DO:**

- Be extremely thorough with examples
- Use multiple rephrasing approaches
- Point out subtle wording
- Identify ambiguities and clarify them
- Use visual representations if helpful
- Compare to similar but different problems

**DON'T:**

- Mention algorithms or data structures
- Discuss approaches or patterns (that's for `/learn`)
- Give hints about the solution
- Show code
- Discuss complexity analysis
- Suggest optimizations

**Remember:** This workflow is ONLY about understanding the problem, not solving it!
