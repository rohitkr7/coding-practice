---
description: Track and solve problems from Jira board
---

# Learning & Development Study Helper Workflow

## Purpose
This workflow helps track and solve coding problems from your Jira board using proven algorithmic patterns.

## Workflow Steps

### 1. Fetch Current Work Items
- Connect to Jira board: https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35
- Filter for items assigned to Rohit
- Display current sprint items and backlog

### 2. Problem Analysis
When you select a problem:
- Identify the problem type
- Suggest relevant coding patterns from the 16 patterns
- Provide hints without giving away the solution
- Guide you through the thought process

### 3. Pattern-Based Hints
Based on the problem, I'll suggest one or more of these patterns:
1. **Sliding Window** - For contiguous subarrays/substrings
2. **Two Pointers** - For sorted arrays or linked lists
3. **Fast & Slow Pointers** - For cycle detection
4. **Merge Intervals** - For overlapping intervals
5. **Cyclic Sort** - For arrays with numbers in a given range
6. **In-place Reversal of LinkedList** - For reversing parts of a linked list
7. **Tree BFS** - For level-order traversal
8. **Tree DFS** - For path-based problems
9. **Two Heaps** - For median/smallest-largest problems
10. **Subsets** - For permutations/combinations
11. **Modified Binary Search** - For sorted data
12. **Bitwise XOR** - For finding unique elements
13. **Top K Elements** - For finding top/smallest/frequent K elements
14. **K-way Merge** - For merging sorted arrays
15. **0/1 Knapsack** - For optimization problems
16. **Topological Sort** - For dependency ordering

### 4. Progress Tracking
- Mark problems as: Not Started, In Progress, Stuck, Completed
- Track time spent on each problem
- Note key learnings and patterns used

### 5. Review & Reflection
- Review solved problems weekly
- Identify weak patterns that need more practice
- Update Jira tickets with solutions and learnings

## Commands

### Start a Study Session
```
"Let's work on [problem name/ID]"
```

### Get a Hint
```
"I'm stuck on [specific part], can you give me a hint?"
```

### Pattern Suggestion
```
"What pattern should I use for this problem?"
```

### Review Progress
```
"Show me my progress this week"
```

## Guidelines for AI Assistant

1. **Never solve the problem completely** - Guide with hints
2. **Ask clarifying questions** - Help understand the problem better
3. **Suggest pattern, not code** - Let the user implement
4. **Provide examples** - Use similar but simpler problems
5. **Encourage thinking** - Ask "What if...?" questions
6. **Validate approach** - Confirm if the user's approach is correct
7. **Discuss complexity** - Help analyze time/space complexity

## Integration with Jira

- Fetch work items using Jira API
- Update ticket status when problems are solved
- Add comments with pattern used and key learnings
- Track time spent on each problem
