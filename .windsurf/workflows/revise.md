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
For each problem, I'll provide:
- **Brief problem statement** (one-liner to refresh memory)
- Then ask you:
- **"What was the main pattern used?"**
- **"What was the key insight that solved this problem?"**
- **"What was the time/space complexity?"**
- **"What edge cases did you handle?"**

This tests your retention without showing the full solution first.

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

### 5. Spaced Repetition Tracking & Tracker Updates

**IMPORTANT**: After each problem review, automatically update `tracking/revision-tracker.json`

**Enhanced 5-Level Spaced Repetition Algorithm:**

**Base Intervals by Pattern Difficulty (Realistic for Coding Patterns):**
- **Easy Patterns** (Two Pointers, Hash Table): [1, 3, 7, 14, 21] days
- **Medium Patterns** (Sliding Window, Tree DFS): [1, 2, 5, 10, 18] days  
- **Hard Patterns** (Dynamic Programming, Backtracking): [1, 2, 4, 8, 15] days

**Quality Rating & Interval Selection:**
- ⭐⭐⭐⭐⭐ **Perfect** (5 stars) → Use interval[4] (longest)
- ⭐⭐⭐⭐ **Good** (4 stars) → Use interval[3]  
- ⭐⭐⭐ **Moderate** (3 stars) → Use interval[2]
- ⭐⭐ **Weak** (2 stars) → Use interval[1]
- ⭐ **None** (1 star) → Use interval[0] (immediate/next day)

**Personal Performance Multipliers:**
- Consistent 5⭐ in pattern → Multiply interval by 1.3x
- Frequent <3⭐ in pattern → Multiply interval by 0.7x
- First time reviewing problem → Use base interval

**Examples:**
- Hash Table problem, Perfect recall (5⭐), first review → 21 days
- DP problem, Weak recall (2⭐), struggling with pattern → 2 * 0.7 = 1.4 → 1 day
- Two Pointers, Good recall (4⭐), consistent performance → 14 * 1.3 = 18 days

**Automatic Tracker Updates:**
1. **Read current tracker**: Load `tracking/revision-tracker.json`
2. **For each problem reviewed**: 
   - Add/update problem entry with:
     - Problem ID (e.g., "LC-125")
     - Problem name
     - Pattern used
     - Date solved (from file metadata)
     - Revision entry with: date, quality rating (1-5), next_review date
   - Calculate next_review date based on quality rating
3. **Update session metadata**:
   - Set `last_revision_session` to current date
   - Keep `total_problems_solved` count accurate
4. **Save updated tracker** back to JSON file

### 6. Track Revision Progress
- Add revision notes as comments in the problem markdown files
- Automatically maintain revision log in `tracking/revision-tracker.json`:
  - Next review date for each problem
  - Revision count and quality ratings  
  - Historical revision data for progress tracking
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

## Guidelines for AI Assistant

1. **Test recall first** - Don't show the solution immediately
2. **Be encouraging** - Forgetting is part of learning
3. **Focus on patterns** - Help identify recurring themes
4. **Suggest practice** - Recommend similar problems for weak areas
5. **Track progress** - Note improvement over multiple revision sessions
6. **Make it quick** - Keep each problem review under 5 minutes
7. **Highlight growth** - Point out patterns that have become stronger
8. **AUTO-UPDATE TRACKER** - Always update `tracking/revision-tracker.json` after each revision session
9. **Calculate next review dates** - Use the 5-star system to determine spaced repetition schedule
10. **Show tracker updates** - Briefly confirm what was updated in the tracker

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

## Revision Tracker Integration

### Tracker File Structure: `tracking/revision-tracker.json`

```json
{
  "last_check_in": "2026-01-20",
  "current_streak": 5,
  "best_streak": 12,
  "total_problems_solved": 25,
  "last_revision_session": "2026-01-20",
  "problems": {
    "LC-125": {
      "name": "Valid Palindrome",
      "pattern": "Two Pointers",
      "date_solved": "2025-12-06",
      "revisions": [
        {
          "date": "2026-01-20",
          "quality": 5,
          "next_review": "2026-01-27"
        }
      ],
      "next_review": "2026-01-27"
    }
  }
}
```

### Integration Points:

1. **After each problem review**: Add revision entry with quality rating
2. **Update next_review**: Calculate based on spaced repetition algorithm  
3. **Track patterns**: Note which patterns need more practice
4. **Session metadata**: Update last_revision_session timestamp

### Enhanced Spaced Repetition Algorithm:

```java
// Pattern difficulty base intervals (in days)
Map<String, int[]> patternIntervals = {
    // Easy patterns - realistic intervals (max 3 weeks)
    "Two Pointers": [1, 3, 7, 14, 21],
    "Hash Table": [1, 3, 7, 14, 21],
    "Binary Search": [1, 3, 7, 14, 21],
    
    // Medium patterns - moderate intervals (max 2.5 weeks)  
    "Sliding Window": [1, 2, 5, 10, 18],
    "Tree DFS": [1, 2, 5, 10, 18],
    "Merge Intervals": [1, 2, 5, 10, 18],
    
    // Hard patterns - frequent intervals (max 2 weeks)
    "Dynamic Programming": [1, 2, 4, 8, 15],
    "Backtracking": [1, 2, 4, 8, 15],
    "Graph": [1, 2, 4, 8, 15]
};

// Calculate next review date
int calculateNextInterval(String pattern, int quality, float personalMultiplier) {
    int[] intervals = patternIntervals.get(pattern);
    int baseInterval = intervals[quality - 1]; // quality 1-5 → index 0-4
    return Math.max(1, Math.round(baseInterval * personalMultiplier));
}

// Personal multiplier based on pattern performance
float getPersonalMultiplier(String pattern, List<Integer> recentQualities) {
    double avgQuality = recentQualities.stream().mapToInt(q -> q).average().orElse(3.0);
    if (avgQuality >= 4.5) return 1.3f;      // Consistent excellence
    if (avgQuality >= 3.5) return 1.0f;      // Normal performance  
    if (avgQuality >= 2.5) return 0.8f;      // Below average
    return 0.7f;                             // Struggling
}
```

This enables the `/daily-check` workflow to show which problems are due for revision!
