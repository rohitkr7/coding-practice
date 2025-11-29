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
- Show problem metadata (title, difficulty, pattern, status)

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
- Update problem files with status

### 5. Review & Reflection
- Review solved problems weekly
- Identify weak patterns that need more practice
- Update Jira tickets with solutions and learnings
- Generate progress reports

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

### Sync with Jira
```
"Sync my Jira work items"
or
"Fetch new problems from Jira"
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

### Fetch Work Items
Use scripts to sync with Jira:
```bash
python3 scripts/sync_jira.py
```

This will:
- Fetch all LND project items
- Create/update problem files in appropriate pattern folders
- Sync status and metadata

### Update Problem Status
When you complete a problem:
1. Update the problem markdown file status to "✅ Completed"
2. Document your solution
3. Run tracker update: `./scripts/update_tracker.sh`
4. (Optional) Manually update Jira ticket status

## Problem Selection Strategy

### For Beginners:
Start with Easy problems in fundamental patterns:
- Two Pointers (2-3 problems)
- Sliding Window (2-3 problems)
- Hash Table (3-4 problems)
- Tree DFS (2-3 problems)

### For Intermediate:
Focus on Medium problems and advanced patterns:
- Dynamic Programming
- Binary Search variations
- Top K Elements
- Merge Intervals

### For Advanced:
Hard problems and complex patterns:
- Topological Sort
- Two Heaps
- K-way Merge
- Advanced DP

## Jira Board Structure

**Project Key**: LND  
**Board ID**: 35  
**Assignee**: Rohit

**Issue Types**:
- Problem (LeetCode coding problem)
- Task (Study-related task)

**Status Flow**:
1. To Do → Not started
2. In Progress → Currently working
3. Stuck → Need hints/guidance
4. Done → Completed and documented

**Labels**:
- Difficulty: Easy, Medium, Hard
- Pattern: Two-Pointers, Sliding-Window, Hash-Table, etc.
- Priority: High, Medium, Low

## Weekly Review Process

Every week, review your Jira board:
1. Count problems solved by difficulty
2. Identify patterns used most/least
3. Note average time per problem
4. Update README tracker
5. Plan next week's problems

## Tips for Success

1. **Start Simple**: Master Easy problems before Medium
2. **Learn Patterns**: Focus on understanding patterns deeply
3. **Track Progress**: Use Jira to visualize progress
4. **Review Regularly**: Use `/revise` workflow weekly
5. **Document Well**: Good notes help future you
6. **Be Consistent**: Solve 1-2 problems daily
7. **Don't Rush**: Understanding > Speed

## Resources

- **Jira Board**: https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35
- **Patterns Guide**: `/Users/rohit.roy/Documents/LnD/PATTERNS_GUIDE.md`
- **GitHub Reference**: https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews

## Troubleshooting

**Can't connect to Jira?**
- Check credentials in `.env` file
- Verify API token is valid
- Ensure network connection

**Problems not syncing?**
- Run `python3 scripts/process_jira_items.py` manually
- Check Jira board URL in `jira/jira-config.json`

**Tracker not updating?**
- Run `./scripts/update_tracker.sh` manually
- Verify problem files have correct status markers
