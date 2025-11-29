# 6 - Product of Array Except Self

**Jira Ticket:** [LND-37](https://rohitroy007.atlassian.net/browse/LND-37)  
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self  
**Pattern:** Array Manipulation / Prefix-Suffix Products  
**Difficulty:** Medium  
**Status:** To Do  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-08-22

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/product-of-array-except-self
Problem Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm running in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem

- What are we asked to find/compute?
- What are the inputs and outputs?
- What are the edge cases?

### Pattern Recognition

**Why Array Manipulation / Prefix-Suffix Products?**

- Need to compute products from both left and right directions
- Cannot use division operator (eliminates simple total/current approach)
- Requires O(n) time complexity

**What clues in the problem point to this pattern?**

- "Product of all elements EXCEPT self" → need left × right products
- "Without division" constraint → must use prefix/suffix approach
- "O(n) time" requirement → single or double pass solution

---

## 💡 Approach

### Brute Force (if applicable)

**Idea:**

-

**Time Complexity:** O(?)  
**Space Complexity:** O(?)

### Optimized Approach

**Idea:**

-

**Algorithm Steps:**

1.
2.
3.

**Time Complexity:** O(?)  
**Space Complexity:** O(?)

---

## 🎨 Visual Explanation

```
Example:

Step 1:
Step 2:
Step 3:
```

---

## 💻 Implementation

```python
# Your solution here
def solution():
    pass
```

### Code Explanation

-

---

## 🧪 Test Cases

### Test Case 1: Basic Example

```
Input:
Expected Output:
Actual Output:
Status: ⏳ Not Tested
```

### Test Case 2: Edge Case - Empty Input

```
Input:
Expected Output:
Actual Output:
Status: ⏳ Not Tested
```

### Test Case 3: Edge Case - Single Element

```
Input:
Expected Output:
Actual Output:
Status: ⏳ Not Tested
```

---

## 📊 Complexity Analysis

### Time Complexity: O(?)

**Breakdown:**

-

### Space Complexity: O(?)

**Breakdown:**

-

---

## 🎓 Key Learnings

### What I Learned

1.
2.
3.

### Mistakes I Made

1.
2.

### Pattern Insights

- When to use prefix-suffix products: When you need information from both directions (before and after each element) without nested loops
- When NOT to use this pattern: When division is allowed and no zeros exist (simpler total product / current element approach works)

---

## 🔗 Similar Problems

1.
2.
3.

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#array-manipulation)
- LeetCode Discussion: https://leetcode.com/problems/product-of-array-except-self/discuss/

---

## ✅ Progress Checklist

- [ ] Problem understood
- [ ] Pattern identified
- [ ] Brute force solution
- [ ] Optimized solution
- [ ] All test cases pass
- [ ] Complexity analyzed
- [ ] Code reviewed
- [ ] Learnings documented
- [ ] Jira ticket updated

---

**Status:** 🔴 Not Started  
**Last Updated:** 2025-08-22
