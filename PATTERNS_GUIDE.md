# Coding Patterns Guide

This guide is based on the repository: [Several Coding Patterns for Solving Data Structures and Algorithms Problems](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)

## 16 Essential Coding Patterns

### Pattern 1: Sliding Window
**When to use:** Problems involving contiguous subarrays or substrings
**Key concept:** Maintain a window that slides through the data
**Common problems:** 
- Maximum sum subarray of size K
- Longest substring with K distinct characters
- Fruits into baskets

---

### Pattern 2: Two Pointers
**When to use:** Sorted arrays, linked lists, or when you need to find pairs
**Key concept:** Use two pointers moving toward each other or in the same direction
**Common problems:**
- Pair with target sum
- Remove duplicates
- Squaring a sorted array

---

### Pattern 3: Fast & Slow Pointers
**When to use:** Cycle detection in linked lists or arrays
**Key concept:** Two pointers moving at different speeds
**Common problems:**
- LinkedList cycle detection
- Find middle of LinkedList
- Happy number

---

### Pattern 4: Merge Intervals
**When to use:** Overlapping intervals problems
**Key concept:** Sort intervals and merge overlapping ones
**Common problems:**
- Merge overlapping intervals
- Insert interval
- Intervals intersection

---

### Pattern 5: Cyclic Sort
**When to use:** Arrays containing numbers in a given range
**Key concept:** Place each number at its correct index
**Common problems:**
- Find missing number
- Find all duplicates
- Find corrupt pair

---

### Pattern 6: In-place Reversal of LinkedList
**When to use:** Reversing parts of a linked list
**Key concept:** Reverse pointers in-place without extra space
**Common problems:**
- Reverse a LinkedList
- Reverse a sub-list
- Reverse every K-element sub-list

---

### Pattern 7: Tree Breadth First Search (BFS)
**When to use:** Level-order traversal of trees
**Key concept:** Use a queue to traverse level by level
**Common problems:**
- Binary tree level order traversal
- Zigzag traversal
- Level averages

---

### Pattern 8: Tree Depth First Search (DFS)
**When to use:** Path-based problems in trees
**Key concept:** Use recursion or stack to explore paths
**Common problems:**
- Sum of path numbers
- All paths for a sum
- Path with given sequence

---

### Pattern 9: Two Heaps
**When to use:** Finding median or dealing with smallest and largest elements
**Key concept:** Use min-heap and max-heap together
**Common problems:**
- Find median of number stream
- Sliding window median
- Maximize capital

---

### Pattern 10: Subsets
**When to use:** Permutations, combinations, or subsets
**Key concept:** Use BFS or backtracking
**Common problems:**
- Generate subsets
- Permutations
- String permutations by changing case

---

### Pattern 11: Modified Binary Search
**When to use:** Sorted data with a twist
**Key concept:** Adapt binary search for rotated or modified arrays
**Common problems:**
- Order-agnostic binary search
- Search in rotated array
- Search in infinite sorted array

---

### Pattern 12: Bitwise XOR
**When to use:** Finding unique elements or missing numbers
**Key concept:** XOR properties (a^a=0, a^0=a)
**Common problems:**
- Single number
- Two single numbers
- Complement of base 10 number

---

### Pattern 13: Top K Elements
**When to use:** Finding top/smallest/frequent K elements
**Key concept:** Use heap to maintain K elements
**Common problems:**
- Top K numbers
- Kth smallest number
- K closest points to origin

---

### Pattern 14: K-way Merge
**When to use:** Merging multiple sorted arrays or lists
**Key concept:** Use heap to merge efficiently
**Common problems:**
- Merge K sorted lists
- Kth smallest in M sorted arrays
- Smallest number range

---

### Pattern 15: 0/1 Knapsack (Dynamic Programming)
**When to use:** Optimization problems with constraints
**Key concept:** Build solution using memoization or bottom-up DP
**Common problems:**
- 0/1 Knapsack
- Equal subset sum partition
- Minimum subset sum difference

---

### Pattern 16: Topological Sort (Graph)
**When to use:** Dependency ordering problems
**Key concept:** Use in-degree and queue for ordering
**Common problems:**
- Task scheduling
- Course schedule
- Alien dictionary

---

## How to Use This Guide

1. **Identify the problem type** - Read the problem carefully
2. **Match with a pattern** - Which pattern fits best?
3. **Understand the approach** - Why does this pattern work?
4. **Implement step by step** - Start with brute force, then optimize
5. **Analyze complexity** - What's the time and space complexity?
6. **Practice variations** - Solve similar problems using the same pattern

## Pattern Selection Flowchart

```
Is it about contiguous elements? → Sliding Window
Is the array sorted? → Two Pointers or Binary Search
Does it involve cycles? → Fast & Slow Pointers
Are there intervals? → Merge Intervals
Numbers in a range [1..n]? → Cyclic Sort
LinkedList reversal? → In-place Reversal
Tree level-by-level? → BFS
Tree path problems? → DFS
Need median/top-bottom elements? → Two Heaps
Combinations/Permutations? → Subsets
Finding top K? → Top K Elements (Heap)
Merging sorted lists? → K-way Merge
Unique elements with XOR? → Bitwise XOR
Optimization with choices? → 0/1 Knapsack (DP)
Dependency ordering? → Topological Sort
```

## Tips for Success

1. **Don't jump to code immediately** - Think about the pattern first
2. **Draw examples** - Visualize the problem with small inputs
3. **Start simple** - Solve a simpler version first
4. **Think out loud** - Explain your approach before coding
5. **Test edge cases** - Empty input, single element, duplicates, etc.
6. **Optimize iteratively** - Brute force → Better → Optimal
7. **Learn from mistakes** - Review wrong approaches to understand why they failed

## Resources

- [Original GitHub Repository](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)
- Each pattern has detailed explanations with JavaScript implementations
- Practice problems are categorized by pattern
