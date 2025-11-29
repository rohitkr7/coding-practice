---
description: Revise last 5 solved problems with spaced repetition
---

# Problem Revision Workflow

## Purpose
This workflow helps you revise the last 5 problems you've solved to reinforce learning and identify patterns you need to practice more.

## Workflow Steps

### 1. Fetch Recently Solved Problems
- Search locally in the `problems/` directory for files with status "✅ Completed"
- Use file modification timestamps to determine completion order
- Sort by modification date (most recent first)
- Display the last 5 solved problems with:
  - Problem name and ID
  - Date completed (from file modification time)
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

### 6. Track Revision Progress
- Add revision notes as comments in the problem markdown files
- Create a local revision log to track:
  - Next review date for each problem
  - Revision count and quality ratings
  - Patterns that need more practice
- Optional: Sync revision notes to Jira if needed

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

## Guidelines for Effective Revision

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

This workflow complements other workflows:
- `/learn` - For learning new problems
- `/revise` - For reinforcing solved problems
- `/review` - For quick pattern review
- `/document` - For documenting solutions

Use `/revise` regularly (2-3 times per week) to maintain and strengthen your problem-solving skills!

## Example Revision Session

```
🔄 **Revision Session: Last 5 Completed Problems**

---

### 1. Two Sum (LC-1) - Completed 3 days ago
**Pattern**: Hash Table
**Recall Test**: What was the key insight?

[Wait for user response]

**Solution Review**:
Key insight: For each number X, look for (target - X) in HashMap
Time: O(n), Space: O(n)
Edge cases: duplicates, negatives, zero

**Recall Quality**: [User rates 1-5 stars]
**Next Review**: [Based on quality - tomorrow/3 days/7 days]

---

### 2. Contains Duplicate (LC-217) - Completed 5 days ago
[Repeat process...]

---

**Session Summary**:
- Patterns Mastered: Hash Table ✓
- Patterns to Practice More: Two Pointers, Sliding Window
- Overall Progress: 3/5 problems recalled perfectly
- Next Session: [Recommended date]
```

## Spaced Repetition Schedule

### First Review: 1 day after solving
- Tests immediate retention
- Reinforces fresh learning

### Second Review: 3 days later
- Checks short-term memory
- Solidifies understanding

### Third Review: 7 days later
- Validates long-term retention
- Confirms pattern mastery

### Fourth Review: 30 days later
- Ensures lasting knowledge
- Identifies patterns for refresher

## Customization Options

You can customize this workflow by:
- Changing number of problems (default: 5)
- Adjusting review intervals
- Adding specific pattern focus
- Including complexity analysis quiz
- Generating performance metrics
