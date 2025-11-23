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
