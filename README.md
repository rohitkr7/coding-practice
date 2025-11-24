# Learning & Development Tracker

Welcome to your personalized Learning & Development workspace! This repository helps you track and solve coding problems systematically using proven algorithmic patterns.

## 🎯 Purpose

This workspace integrates with your Jira board to:
- Track coding problems assigned to you
- Provide pattern-based hints and guidance
- Help you learn problem-solving approaches without giving away solutions
- Monitor your progress and identify areas for improvement

## 📋 Jira Board

Your Jira Board: [LND Project](https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35)

## 📚 Resources

### 1. Patterns Guide
See [`PATTERNS_GUIDE.md`](./PATTERNS_GUIDE.md) for a comprehensive guide to 16 coding patterns that solve most interview problems.

### 2. Windsurf Workflow
The `.windsurf/workflows/study-helper.md` file contains the automated workflow for:
- Fetching Jira work items
- Analyzing problems
- Providing pattern-based hints
- Tracking progress

### 3. Problem Tracking
Create a `problems/` directory to store:
- Your solutions
- Notes and learnings
- Pattern mappings
- Complexity analysis

## 🚀 Getting Started

### Step 1: Fetch Your Work Items
Ask the AI assistant:
```
"Fetch my current Jira work items"
```

### Step 2: Select a Problem
```
"Let's work on [problem name/ID]"
```

### Step 3: Get Guidance
The AI will:
- Help you understand the problem
- Suggest relevant patterns
- Provide hints when you're stuck
- Validate your approach
- Discuss time/space complexity

## 💡 How to Use the AI Assistant

### ✅ DO:
- Ask for hints when stuck
- Request pattern suggestions
- Discuss your approach before coding
- Ask about time/space complexity
- Request similar example problems

### ❌ DON'T:
- Ask for complete solutions (the AI won't provide them)
- Skip thinking and jump to hints
- Ignore the suggested patterns

## 📊 Progress Tracking

### Problem Status
- 🔴 **Not Started** - Problem identified but not attempted
- 🟡 **In Progress** - Currently working on it
- 🟠 **Stuck** - Need hints or guidance
- 🟢 **Completed** - Solved and understood

### Weekly Review
Every week, review:
1. Problems solved
2. Patterns used
3. Weak areas identified
4. Time spent on each problem

## 🎓 Learning Approach

### 1. Understand the Problem
- Read carefully
- Identify inputs and outputs
- Consider edge cases
- Draw examples

### 2. Identify the Pattern
- What type of problem is this?
- Which pattern fits best?
- Why does this pattern work here?

### 3. Design the Approach
- Start with brute force
- Think about optimization
- Consider trade-offs

### 4. Implement
- Write clean, readable code
- Add comments for complex logic
- Test with examples

### 5. Analyze
- Time complexity
- Space complexity
- Can it be optimized further?

### 6. Reflect
- What did you learn?
- What would you do differently?
- What similar problems can you solve now?

## 📁 Recommended Structure

```
LnD/
├── README.md (this file)
├── PATTERNS_GUIDE.md
├── .windsurf/
│   └── workflows/
│       └── study-helper.md
├── problems/
│   ├── sliding-window/
│   ├── two-pointers/
│   ├── fast-slow-pointers/
│   ├── merge-intervals/
│   ├── cyclic-sort/
│   ├── linkedlist-reversal/
│   ├── tree-bfs/
│   ├── tree-dfs/
│   ├── two-heaps/
│   ├── subsets/
│   ├── binary-search/
│   ├── bitwise-xor/
│   ├── top-k-elements/
│   ├── k-way-merge/
│   ├── knapsack-dp/
│   └── topological-sort/
├── notes/
│   ├── weekly-reviews/
│   └── key-learnings/
└── jira-sync/
    └── work-items.json
```

## 🔗 External Resources

- [Coding Patterns Repository](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)
- Your Jira Board: [LND Project](https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35)

## 🤝 Working with the AI

The AI assistant is configured to:
1. **Guide, not solve** - You'll get hints and direction, not complete solutions
2. **Teach patterns** - Learn reusable problem-solving approaches
3. **Validate thinking** - Confirm if you're on the right track
4. **Encourage exploration** - Ask "what if" questions to deepen understanding

## 📝 Commands Reference

| Command | Purpose |
|---------|---------|
| "Fetch my Jira items" | Get current work items assigned to you |
| "Let's work on [problem]" | Start working on a specific problem |
| "What pattern should I use?" | Get pattern suggestions |
| "I'm stuck on [part]" | Get a hint for specific part |
| "Is my approach correct?" | Validate your solution approach |
| "What's the complexity?" | Discuss time/space complexity |
| "Show similar problems" | Find related problems for practice |
| "Review my progress" | See weekly progress summary |

## 🎯 Goals

- Build strong problem-solving fundamentals
- Master the 16 essential coding patterns
- Develop pattern recognition skills
- Improve time and space complexity analysis
- Build confidence in technical interviews

---

**Remember:** The goal is not just to solve problems, but to understand the patterns and approaches that make you a better problem solver!

Happy Learning! 🚀


<!-- PROBLEM_TRACKER_START -->
## 📊 Problem Tracker

**Progress:** 3/77 problems completed (3%)

---

### Binary Search
**Progress:** 0/4 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [22 - Search a 2D Matrix](problems/binary-search/LND-133-22-search-a-2d-matrix.md) | 🟡 Medium | LND-133 | [LC](https://leetcode.com/problems/search-a-2d-matrix) |
| ⏳ | [23 - Find Minimum in Rotated Sorted Array](problems/binary-search/LND-134-23-find-minimum-in-rotated-sorted-array.md) | 🟡 Medium | LND-134 | [LC](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) |
| ⏳ | [21 - Binary Search](problems/binary-search/LND-139-21-binary-search.md) | 🟢 Easy | LND-139 | [LC](https://leetcode.com/problems/binary-search) |
| ⏳ | [24 - Search in Rotated Sorted Array](problems/binary-search/LND-143-24-search-in-rotated-sorted-array.md) | 🟡 Medium | LND-143 | [LC](https://leetcode.com/problems/search-in-rotated-sorted-array) |

### Bitwise Xor
**Progress:** 0/5 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [6 - Product of Array Except Self](problems/bitwise-xor/LND-37-6-product-of-array-except-self.md) | 🟡 Medium | LND-37 | [LC](https://leetcode.com/problems/product-of-array-except-self) |
| ⏳ | [75 - Missing Number](problems/bitwise-xor/LND-85-75-missing-number.md) | 🟢 Easy | LND-85 | [LC](https://leetcode.com/problems/missing-number) |
| ⏳ | [73 - Counting Bits](problems/bitwise-xor/LND-91-73-counting-bits.md) | 🟢 Easy | LND-91 | [LC](https://leetcode.com/problems/counting-bits) |
| ⏳ | [74 - Reverse Bits](problems/bitwise-xor/LND-93-74-reverse-bits.md) | 🟢 Easy | LND-93 | [LC](https://leetcode.com/problems/reverse-bits) |
| ⏳ | [72 - Number of 1 Bits](problems/bitwise-xor/LND-96-72-number-of-1-bits.md) | 🟢 Easy | LND-96 | [LC](https://leetcode.com/problems/number-of-1-bits) |

### Fast Slow Pointers
**Progress:** 0/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [29 - Linked List Cycle](problems/fast-slow-pointers/LND-14-29-linked-list-cycle.md) | 🟢 Easy | LND-14 | [LC](https://leetcode.com/problems/linked-list-cycle) |

### Hash Table / Frequency Counter
**Progress:** 1/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ✅ | [3 - Valid Anagram](problems/two-pointers/LND-27-3-valid-anagram.md) | 🟢 Easy | LND-27 | [LC](https://leetcode.com/problems/valid-anagram) |

### K Way Merge
**Progress:** 0/2 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [26 - Merge Two Sorted Lists](problems/k-way-merge/LND-140-26-merge-two-sorted-lists.md) | 🟢 Easy | LND-140 | [LC](https://leetcode.com/problems/merge-two-sorted-lists) |
| ⏳ | [30 - Merge k Sorted Lists](problems/k-way-merge/LND-16-30-merge-k-sorted-lists.md) | 🔴 Hard | LND-16 | [LC](https://leetcode.com/problems/merge-k-sorted-lists) |

### Knapsack Dp
**Progress:** 0/2 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [57 - Coin Change](problems/knapsack-dp/LND-50-57-coin-change.md) | 🟡 Medium | LND-50 | [LC](https://leetcode.com/problems/coin-change) |
| ⏳ | [51 - Climbing Stairs](problems/knapsack-dp/LND-55-51-climbing-stairs.md) | 🟢 Easy | LND-55 | [LC](https://leetcode.com/problems/climbing-stairs) |

### Linkedlist Reversal
**Progress:** 0/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [25 - Reverse Linked List](problems/linkedlist-reversal/LND-145-25-reverse-linked-list.md) | 🟢 Easy | LND-145 | [LC](https://leetcode.com/problems/reverse-linked-list) |

### Merge Intervals
**Progress:** 0/5 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [66 - Non-overlapping Intervals](problems/merge-intervals/LND-62-66-non-overlapping-intervals.md) | 🟡 Medium | LND-62 | [LC](https://leetcode.com/problems/non-overlapping-intervals) |
| ⏳ | [67 - Meeting Rooms](problems/merge-intervals/LND-63-67-meeting-rooms.md) | 🟢 Easy | LND-63 | [LC](https://leetcode.com/problems/meeting-rooms) |
| ⏳ | [64 - Insert Interval](problems/merge-intervals/LND-65-64-insert-interval.md) | 🟡 Medium | LND-65 | [LC](https://leetcode.com/problems/insert-interval) |
| ⏳ | [65 - Merge Intervals](problems/merge-intervals/LND-67-65-merge-intervals.md) | 🟡 Medium | LND-67 | [LC](https://leetcode.com/problems/merge-intervals) |
| ⏳ | [68 - Meeting Rooms II](problems/merge-intervals/LND-69-68-meeting-rooms-ii.md) | 🟡 Medium | LND-69 | [LC](https://leetcode.com/problems/meeting-rooms-ii) |

### Sliding Window
**Progress:** 0/6 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [15 - Minimum Window Substring](problems/sliding-window/LND-122-15-minimum-window-substring.md) | 🔴 Hard | LND-122 | [LC](https://leetcode.com/problems/minimum-window-substring) |
| ⏳ | [13 - Longest Substring Without Repeating Characters](problems/sliding-window/LND-126-13-longest-substring-without-repeating-characters.md) | 🟡 Medium | LND-126 | [LC](https://leetcode.com/problems/longest-substring-without-repeating-characters) |
| ⏳ | [14 - Longest Repeating Character Replacement](problems/sliding-window/LND-127-14-longest-repeating-character-replacement.md) | 🟡 Medium | LND-127 | [LC](https://leetcode.com/problems/longest-repeating-character-replacement) |
| ⏳ | [55 - Palindromic Substrings](problems/sliding-window/LND-43-55-palindromic-substrings.md) | 🟡 Medium | LND-43 | [LC](https://leetcode.com/problems/palindromic-substrings) |
| ⏳ | [54 - Longest Palindromic Substring](problems/sliding-window/LND-48-54-longest-palindromic-substring.md) | 🟡 Medium | LND-48 | [LC](https://leetcode.com/problems/longest-palindromic-substring) |
| ⏳ | [58 - Maximum Product Subarray](problems/sliding-window/LND-52-58-maximum-product-subarray.md) | 🟡 Medium | LND-52 | [LC](https://leetcode.com/problems/maximum-product-subarray) |

### Subsets
**Progress:** 0/2 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [44 - Combination Sum](problems/subsets/LND-17-44-combination-sum.md) | 🟡 Medium | LND-17 | [LC](https://leetcode.com/problems/combination-sum) |
| ⏳ | [45 - Word Search](problems/subsets/LND-19-45-word-search.md) | 🟡 Medium | LND-19 | [LC](https://leetcode.com/problems/word-search) |

### Top K Elements
**Progress:** 0/3 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| 🟡 | [Blind75-NeetCode](problems/top-k-elements/LND-152-blind75-neetcode.md) | 🟡 Medium | LND-152 | - |
| ⏳ | [5 - Top K Frequent Elements](problems/top-k-elements/LND-36-5-top-k-frequent-elements.md) | 🟡 Medium | LND-36 | [LC](https://leetcode.com/problems/top-k-frequent-elements) |
| ⏳ | [63 - Jump Game](problems/top-k-elements/LND-74-63-jump-game.md) | 🟡 Medium | LND-74 | [LC](https://leetcode.com/problems/jump-game) |

### Topological Sort
**Progress:** 0/5 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [48 - Pacific Atlantic Water Flow](problems/topological-sort/LND-23-48-pacific-atlantic-water-flow.md) | 🟡 Medium | LND-23 | [LC](https://leetcode.com/problems/pacific-atlantic-water-flow) |
| ⏳ | [46 - Number of Islands](problems/topological-sort/LND-24-46-number-of-islands.md) | 🟡 Medium | LND-24 | [LC](https://leetcode.com/problems/number-of-islands) |
| ⏳ | [47 - Clone Graph](problems/topological-sort/LND-25-47-clone-graph.md) | 🟡 Medium | LND-25 | [LC](https://leetcode.com/problems/clone-graph) |
| ⏳ | [49 - Course Schedule](problems/topological-sort/LND-58-49-course-schedule.md) | 🟡 Medium | LND-58 | [LC](https://leetcode.com/problems/course-schedule) |
| ⏳ | [50 - Number of Connected Components In An Undirected Graph](problems/topological-sort/LND-59-50-number-of-connected-components-in-an-undirected-graph.md) | 🟡 Medium | LND-59 | [LC](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) |

### Tree Bfs
**Progress:** 0/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [36 - Binary Tree Level Order Traversal](problems/tree-bfs/LND-13-36-binary-tree-level-order-traversal.md) | 🟡 Medium | LND-13 | [LC](https://leetcode.com/problems/binary-tree-level-order-traversal) |

### Tree Dfs
**Progress:** 0/14 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [38 - Kth Smallest Element in a BST](problems/tree-dfs/LND-10-38-kth-smallest-element-in-a-bst.md) | 🟡 Medium | LND-10 | [LC](https://leetcode.com/problems/kth-smallest-element-in-a-bst) |
| ⏳ | [17 - Min Stack](problems/tree-dfs/LND-112-17-min-stack.md) | 🟡 Medium | LND-112 | [LC](https://leetcode.com/problems/min-stack) |
| ⏳ | [18 - Evaluate Reverse Polish Notation](problems/tree-dfs/LND-114-18-evaluate-reverse-polish-notation.md) | 🟡 Medium | LND-114 | [LC](https://leetcode.com/problems/evaluate-reverse-polish-notation) |
| ⏳ | [35 - Lowest Common Ancestor of a Binary Search Tree](problems/tree-dfs/LND-12-35-lowest-common-ancestor-of-a-binary-search-tree.md) | 🟢 Easy | LND-12 | [LC](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) |
| ⏳ | [16 - Valid Parentheses](problems/tree-dfs/LND-124-16-valid-parentheses.md) | 🟢 Easy | LND-124 | [LC](https://leetcode.com/problems/valid-parentheses) |
| ⏳ | [20 - Daily Temperatures](problems/tree-dfs/LND-136-20-daily-temperatures.md) | 🟡 Medium | LND-136 | [LC](https://leetcode.com/problems/daily-temperatures) |
| ⏳ | [19 - Generate Parentheses](problems/tree-dfs/LND-150-19-generate-parentheses.md) | 🟡 Medium | LND-150 | [LC](https://leetcode.com/problems/generate-parentheses) |
| ⏳ | [33 - Same Tree](problems/tree-dfs/LND-3-33-same-tree.md) | 🟢 Easy | LND-3 | [LC](https://leetcode.com/problems/same-tree) |
| ⏳ | [40 - Implement Trie (Prefix Tree)](problems/tree-dfs/LND-31-40-implement-trie-prefix-tree.md) | 🟡 Medium | LND-31 | [LC](https://leetcode.com/problems/implement-trie-prefix-tree) |
| ⏳ | [39 - Binary Tree Maximum Path Sum](problems/tree-dfs/LND-39-39-binary-tree-maximum-path-sum.md) | 🔴 Hard | LND-39 | [LC](https://leetcode.com/problems/binary-tree-maximum-path-sum) |
| ⏳ | [34 - Subtree of Another Tree](problems/tree-dfs/LND-4-34-subtree-of-another-tree.md) | 🟢 Easy | LND-4 | [LC](https://leetcode.com/problems/subtree-of-another-tree) |
| ⏳ | [31 - Invert Binary Tree](problems/tree-dfs/LND-6-31-invert-binary-tree.md) | 🟢 Easy | LND-6 | [LC](https://leetcode.com/problems/invert-binary-tree) |
| ⏳ | [32 - Maximum Depth of Binary Tree](problems/tree-dfs/LND-7-32-maximum-depth-of-binary-tree.md) | 🟢 Easy | LND-7 | [LC](https://leetcode.com/problems/maximum-depth-of-binary-tree) |
| ⏳ | [37 - Validate Binary Search Tree](problems/tree-dfs/LND-9-37-validate-binary-search-tree.md) | 🟡 Medium | LND-9 | [LC](https://leetcode.com/problems/validate-binary-search-tree) |

### Two Heaps
**Progress:** 0/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [43 - Find Median from Data Stream](problems/two-heaps/LND-22-43-find-median-from-data-stream.md) | 🔴 Hard | LND-22 | [LC](https://leetcode.com/problems/find-median-from-data-stream) |

### Two Pointers
**Progress:** 2/24 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ✅ | [First Task](problems/two-pointers/LND-1-first-task.md) | 🟡 Medium | LND-1 | - |
| ⏳ | [11 - Container With Most Water](problems/two-pointers/LND-116-11-container-with-most-water.md) | 🟡 Medium | LND-116 | [LC](https://leetcode.com/problems/container-with-most-water) |
| ⏳ | [12 - Best Time to Buy and Sell Stock](problems/two-pointers/LND-117-12-best-time-to-buy-and-sell-stock.md) | 🟢 Easy | LND-117 | [LC](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) |
| ⏳ | [9 - Valid Palindrome](problems/two-pointers/LND-119-9-valid-palindrome.md) | 🟢 Easy | LND-119 | [LC](https://leetcode.com/problems/valid-palindrome) |
| ⏳ | [10 - 3Sum](problems/two-pointers/LND-121-10-3sum.md) | 🟡 Medium | LND-121 | [LC](https://leetcode.com/problems/3sum) |
| ⏳ | [28 - Remove Nth Node From End of List](problems/two-pointers/LND-132-28-remove-nth-node-from-end-of-list.md) | 🟡 Medium | LND-132 | [LC](https://leetcode.com/problems/remove-nth-node-from-end-of-list) |
| ⏳ | [27 - Reorder List](problems/two-pointers/LND-141-27-reorder-list.md) | 🟡 Medium | LND-141 | [LC](https://leetcode.com/problems/reorder-list) |
| ⏳ | [42 - Word Search II](problems/two-pointers/LND-20-42-word-search-ii.md) | 🔴 Hard | LND-20 | [LC](https://leetcode.com/problems/word-search-ii) |
| ⏳ | [4 - Group Anagrams](problems/two-pointers/LND-28-4-group-anagrams.md) | 🟡 Medium | LND-28 | [LC](https://leetcode.com/problems/group-anagrams) |
| ✅ | [1 - Two Sum](problems/two-pointers/LND-29-1-two-sum.md) | 🟢 Easy | LND-29 | [LC](https://leetcode.com/problems/two-sum) |
| ✅ | [2 - Contains Duplicate](problems/two-pointers/LND-30-2-contains-duplicate.md) | 🟢 Easy | LND-30 | [LC](https://leetcode.com/problems/contains-duplicate) |
| ⏳ | [7 - Encode and Decode Strings](problems/two-pointers/LND-32-7-encode-and-decode-strings.md) | 🟡 Medium | LND-32 | [LC](https://leetcode.com/problems/encode-and-decode-strings) |
| ⏳ | [41 - Design Add and Search Words Data Structure](problems/two-pointers/LND-34-41-design-add-and-search-words-data-structure.md) | 🟡 Medium | LND-34 | [LC](https://leetcode.com/problems/design-add-and-search-words-data-structure) |
| ⏳ | [8 - Longest Consecutive Sequence](problems/two-pointers/LND-35-8-longest-consecutive-sequence.md) | 🟡 Medium | LND-35 | [LC](https://leetcode.com/problems/longest-consecutive-sequence) |
| ⏳ | [56 - Decode Ways](problems/two-pointers/LND-45-56-decode-ways.md) | 🟡 Medium | LND-45 | [LC](https://leetcode.com/problems/decode-ways) |
| ⏳ | [53 - House Robber II](problems/two-pointers/LND-47-53-house-robber-ii.md) | 🟡 Medium | LND-47 | [LC](https://leetcode.com/problems/house-robber-ii) |
| ⏳ | [52 - House Robber](problems/two-pointers/LND-56-52-house-robber.md) | 🟡 Medium | LND-56 | [LC](https://leetcode.com/problems/house-robber) |
| ⏳ | [59 - Word Break](problems/two-pointers/LND-72-59-word-break.md) | 🟡 Medium | LND-72 | [LC](https://leetcode.com/problems/word-break) |
| ⏳ | [62 - Longest Common Subsequence](problems/two-pointers/LND-73-62-longest-common-subsequence.md) | 🟡 Medium | LND-73 | [LC](https://leetcode.com/problems/longest-common-subsequence) |
| ⏳ | [60 - Longest Increasing Subsequence](problems/two-pointers/LND-76-60-longest-increasing-subsequence.md) | 🟡 Medium | LND-76 | [LC](https://leetcode.com/problems/longest-increasing-subsequence) |
| ⏳ | [61 - Unique Paths](problems/two-pointers/LND-78-61-unique-paths.md) | 🟡 Medium | LND-78 | [LC](https://leetcode.com/problems/unique-paths) |
| ⏳ | [69 - Rotate Image](problems/two-pointers/LND-89-69-rotate-image.md) | 🟡 Medium | LND-89 | [LC](https://leetcode.com/problems/rotate-image) |
| ⏳ | [70 - Spiral Matrix](problems/two-pointers/LND-90-70-spiral-matrix.md) | 🟡 Medium | LND-90 | [LC](https://leetcode.com/problems/spiral-matrix) |
| ⏳ | [71 - Set Matrix Zeroes](problems/two-pointers/LND-94-71-set-matrix-zeroes.md) | 🟡 Medium | LND-94 | [LC](https://leetcode.com/problems/set-matrix-zeroes) |

<!-- PROBLEM_TRACKER_END -->
