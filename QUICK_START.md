# Quick Start Guide

## 🚀 Getting Started with Your L&D Workspace

### What's Been Set Up

Your Learning & Development workspace is now ready! Here's what you have:

1. **📚 PATTERNS_GUIDE.md** - Complete guide to 16 coding patterns
2. **📋 README.md** - Full documentation of this workspace
3. **⚙️ .windsurf/workflows/study-helper.md** - Automated workflow for studying
4. **📁 Organized directories** - Problems sorted by pattern type
5. **🔧 jira-config.json** - Configuration for your Jira board

### Your Jira Board
[LND Project Board](https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35)

---

## 🎯 How to Use This Workspace

### Step 1: Fetch Your Work Items
To get started, tell me:
```
"Fetch my Jira work items"
```

I'll retrieve all items assigned to you from your LND board.

### Step 2: Pick a Problem
Once you see your work items, choose one:
```
"Let's work on [problem name or ID]"
```

### Step 3: Get Guidance
I'll help you by:
- ✅ Asking clarifying questions about the problem
- ✅ Suggesting which of the 16 patterns to use
- ✅ Providing hints when you're stuck
- ✅ Validating your approach
- ✅ Discussing time/space complexity
- ❌ **NOT giving you the complete solution**

---

## 💡 Example Conversation Flow

**You:** "Let's work on finding the maximum sum subarray of size K"

**Me:** "Great! Let me help you think through this. First, let's understand:
1. What are the inputs? (array of numbers, integer K)
2. What's the output? (maximum sum)
3. Any constraints? (array size, K value)

This looks like a **Sliding Window** problem. Why? Because we're looking at contiguous elements of a fixed size.

Can you think about how a sliding window would work here?"

**You:** "I think I slide a window of size K through the array?"

**Me:** "Exactly! Now, what would you track as the window slides?"

**You:** "The sum of elements in the current window?"

**Me:** "Perfect! And how would you optimize this? Do you need to recalculate the entire sum each time?"

---

## 📊 The 16 Patterns (Quick Reference)

| Pattern | Use When | Example |
|---------|----------|---------|
| 1. Sliding Window | Contiguous subarrays/substrings | Max sum subarray |
| 2. Two Pointers | Sorted arrays, pairs | Two sum in sorted array |
| 3. Fast & Slow Pointers | Cycle detection | LinkedList cycle |
| 4. Merge Intervals | Overlapping intervals | Merge intervals |
| 5. Cyclic Sort | Numbers in range [1..n] | Find missing number |
| 6. LinkedList Reversal | Reverse linked list parts | Reverse sub-list |
| 7. Tree BFS | Level-order traversal | Level order traversal |
| 8. Tree DFS | Path problems | All root-to-leaf paths |
| 9. Two Heaps | Median, top/bottom K | Find median |
| 10. Subsets | Combinations/permutations | Generate subsets |
| 11. Binary Search | Sorted data with twist | Search rotated array |
| 12. Bitwise XOR | Find unique elements | Single number |
| 13. Top K Elements | Top/smallest K items | Top K frequent |
| 14. K-way Merge | Merge sorted lists | Merge K sorted lists |
| 15. 0/1 Knapsack | Optimization with DP | Subset sum |
| 16. Topological Sort | Dependency ordering | Course schedule |

---

## 🎓 Study Tips

### Before Starting a Problem
1. Read the problem 2-3 times
2. Draw examples with small inputs
3. Identify the pattern
4. Think about edge cases

### While Solving
1. Start with brute force approach
2. Think about optimization
3. Consider time/space tradeoffs
4. Write clean, readable code

### After Solving
1. Analyze complexity
2. Test edge cases
3. Document learnings
4. Update Jira ticket

---

## 📝 Useful Commands

| What You Want | What to Say |
|---------------|-------------|
| See your Jira items | "Fetch my Jira work items" |
| Start a problem | "Let's work on [problem]" |
| Get a hint | "I'm stuck on [specific part]" |
| Pattern suggestion | "What pattern should I use?" |
| Validate approach | "Is this approach correct?" |
| Check complexity | "What's the time complexity?" |
| Find similar problems | "Show me similar problems" |

---

## 🗂️ Directory Structure

```
LnD/
├── README.md                    # Full documentation
├── QUICK_START.md              # This file
├── PATTERNS_GUIDE.md           # Detailed pattern guide
├── jira-config.json            # Jira configuration
├── .windsurf/
│   └── workflows/
│       └── study-helper.md     # Workflow automation
├── problems/                   # Your solutions by pattern
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
│   ├── weekly-reviews/         # Weekly progress reviews
│   └── key-learnings/          # Important takeaways
└── jira-sync/                  # Synced work items
```

---

## 🎯 Your Learning Goals

1. **Master the 16 patterns** - Recognize which pattern fits each problem
2. **Build problem-solving intuition** - Think before coding
3. **Understand complexity** - Analyze time and space
4. **Practice consistently** - Regular practice builds skill
5. **Learn from mistakes** - Review and reflect

---

## 🤝 How I'll Help You

### I WILL:
- ✅ Guide you with hints and questions
- ✅ Suggest relevant patterns
- ✅ Help you understand the "why"
- ✅ Validate your thinking
- ✅ Discuss complexity analysis
- ✅ Provide similar examples

### I WON'T:
- ❌ Give you complete solutions
- ❌ Write the code for you
- ❌ Skip the learning process
- ❌ Let you copy without understanding

---

## 🚦 Ready to Start?

Tell me: **"Fetch my Jira work items"** and let's begin your learning journey! 🚀

---

## 📚 Additional Resources

- [Coding Patterns GitHub Repo](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)
- [Your Jira Board](https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35)
- See `PATTERNS_GUIDE.md` for detailed pattern explanations
