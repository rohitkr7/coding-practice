---
description: Revise last 5 solved problems with spaced repetition
---

# Problem Revision Workflow

## Purpose
This workflow helps you revise the last 5 problems you've solved to reinforce learning and identify patterns you need to practice more.

## Workflow Steps

### 1. Fetch Recently Solved Problems
- Connect to Jira board: https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35
- Filter for problems marked as "Completed" or "Done"
- Sort by completion date (most recent first)
- Display the last 5 solved problems with:
  - Problem name and ID
  - Date completed
  - Pattern(s) used
  - Time complexity
  - Space complexity
  - Key learnings (if documented)

### 2. Quick Recall Test
For each problem, I'll ask you:
- **"What was the main pattern used?"**
- **"What was the key insight that solved this problem?"**
- **"What was the time/space complexity?"**
- **"What edge cases did you handle?"**

This tests your retention without looking at the solution first.

### 3. Solution Review
After your recall attempt, I'll:
- Show your original solution approach
- Highlight the pattern used
- Review the key insights
- Discuss any alternative approaches

### 4. Pattern Reinforcement
- Identify common patterns across the 5 problems
- Suggest similar problems for patterns you struggled to recall
- Note patterns that need more practice

### 5. Spaced Repetition Tracking
- Mark problems for future review based on recall quality:
  - **Easy recall** → Review in 7 days
  - **Moderate recall** → Review in 3 days
  - **Difficult recall** → Review tomorrow
  - **No recall** → Redo the problem today

### 6. Update Jira
- Add revision notes to Jira tickets
- Update custom fields for next review date
- Track revision count for each problem

## Commands

### Start Revision Session
```
"Let's revise my last 5 problems"
or
"/revise"
```

### Skip to Specific Problem
```
"Show me problem [name/ID] from my recent solutions"
```

### Deep Dive on Pattern
```
"I need more practice with [pattern name]"
```

### Check Revision Schedule
```
"What problems should I review this week?"
```

## Revision Quality Assessment

After each problem review, I'll ask you to rate your recall:
- ⭐⭐⭐⭐⭐ **Perfect** - Remembered everything including edge cases
- ⭐⭐⭐⭐ **Good** - Remembered pattern and approach, minor details forgotten
- ⭐⭐⭐ **Moderate** - Remembered pattern but struggled with implementation details
- ⭐⭐ **Weak** - Vague memory, needed significant hints
- ⭐ **None** - Completely forgot, need to redo

## Guidelines for AI Assistant

1. **Test recall first** - Don't show the solution immediately
2. **Be encouraging** - Forgetting is part of learning
3. **Focus on patterns** - Help identify recurring themes
4. **Suggest practice** - Recommend similar problems for weak areas
5. **Track progress** - Note improvement over multiple revision sessions
6. **Make it quick** - Keep each problem review under 5 minutes
7. **Highlight growth** - Point out patterns that have become stronger

## Benefits of This Workflow

- **Reinforces learning** through active recall
- **Identifies weak spots** that need more practice
- **Builds pattern recognition** across multiple problems
- **Prevents forgetting** through spaced repetition
- **Tracks progress** over time
- **Efficient review** - Only 5 problems per session (15-25 minutes)

## Integration with Study Workflow

This workflow complements the `/study` workflow:
- `/study` - For learning new problems
- `/revise` - For reinforcing solved problems
- `/review` - For quick pattern review

Use `/revise` regularly (2-3 times per week) to maintain and strengthen your problem-solving skills!
