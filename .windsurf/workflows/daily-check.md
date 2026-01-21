---
description: Daily check-in for revision tracking and progress
---

# Daily Check Workflow

## Purpose
A quick 30-second check-in to see what problems need revision today and track your learning streak. Think of this as your daily standup with yourself!

## Workflow Steps

### 1. Load Revision Tracker
- Read `tracking/revision-tracker.json`
- If file doesn't exist, create it with default structure
- Parse current revision schedule

### 2. Show Today's Dashboard

Display a clean, motivating dashboard with enhanced visual indicators:

```
📅 Daily Check-In - [Current Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 Revision Streak: [X days] | 📈 Revision Debt: [Y days] | ⚡ Pattern Mastery: [Z%]
📊 Total Problems Solved: [Y problems] | 🎯 Weekly Goal: [X/7 revisions]
⏰ Last Revision: [Date or "Not yet today"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 DUE TODAY ([count] problems) - Priority Order:
[List by pattern weakness priority:]
  🔴 [Problem ID] - [Problem Name] | [Pattern] | Overdue: [X] days | Difficulty: ⭐⭐⭐
  🟡 [Problem ID] - [Problem Name] | [Pattern] | Due today | Last: [X] days ago

⚠️  REVISION DEBT ([count] problems) - [Total days overdue]:
[List overdue problems by urgency:]
  🔴 [Problem ID] - [Problem Name] | [Pattern] | [X] days overdue | Priority: HIGH
  🟠 [Problem ID] - [Problem Name] | [Pattern] | [X] days overdue | Priority: MED

📊 PATTERN ANALYSIS:
  🔴 Weak: [Pattern Names] ([X] problems overdue)
  🟡 Needs Practice: [Pattern Names] ([X] problems due)
  🟢 Strong: [Pattern Names] ([X] problems mastered)

📆 UPCOMING THIS WEEK ([count] problems):
[Smart scheduling by pattern and difficulty:]
  • [Problem ID] - [Problem Name] | [Pattern] | [Day] | Next interval: [X] days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ SMART ACTIONS (Ordered by Impact):
  🎯 Priority: '/revise [pattern]' - Focus on weakest pattern first
  📚 Standard: '/revise' - Review all due problems  
  🚫 Blocked: '/learn' (BLOCKED - Clear revision debt first!)
  ⏭️  Skip: Update next check-in (adds 1 day to revision debt)
  
💡 TIP: Pattern mastery = consistency! Focus on your red patterns first.
```

### 3. Update Last Check-In Time
- Record current timestamp as last check-in
- Update daily streak (consecutive days with check-ins)

### 4. Provide Context-Aware Suggestions

**If no problems are due:**
```
🎉 You're all caught up! Great work staying consistent.

Want to:
  • Solve a new problem? → /learn
  • Get ahead and review early? → /revise
  • Challenge yourself? → /roast [paste your solution]
```

**If 1-3 problems are due:**
```
Perfect timing! You have just [X] problems to review.
This should take about 10-15 minutes.

Ready? Type '/revise' to start!
```

**If 4+ problems are due:**
```
You have [X] problems to review. That's a bit much for one session.

Suggestion:
  • Review [Y] critical patterns today → /revise [specify count]
  • Schedule the rest for tomorrow

Remember: Quality over quantity! Better to deeply review 3 problems than rush through 10.
```

**If problems are overdue (Revision Debt > 0):**
```
⚠️  Revision Debt: [X] days across [Y] problems

🚨 ENFORCEMENT ACTIVE:
  • '/learn' workflow blocked until debt < 3 days
  • Streak bonus paused until caught up
  • Pattern mastery calculation affected

📋 SMART RECOVERY PLAN:
  🎯 Today: [List 3 highest priority problems by pattern weakness]
  📅 Tomorrow: [List next 3 problems]
  🏁 Target: Debt-free by [Date]

💪 Recovery Motivation:
  • Clearing debt = +5 streak bonus
  • Pattern mastery will jump +15% when caught up
  • You've successfully recovered [X] times before!

Your patterns aren't lost, they just need activation! 🧠⚡
```

**If revision debt >= 7 days (Critical):**
```
🚨 CRITICAL: [X] days revision debt - Pattern retention at risk!

🛑 EMERGENCY MODE ACTIVATED:
  • All workflows except /revise are blocked
  • Simplified recovery: 2 problems per day maximum
  • Focus ONLY on strongest patterns first (easier wins)
  • Weekly reset available: Type '/reset-debt' (lose streak but clear debt)

🎯 EMERGENCY RECOVERY:
  Today: [Easiest 2 problems from strongest patterns]
  Goal: Reduce debt to <7 days, then normal recovery plan

Remember: Even experts have rough weeks. This is temporary! 💪
```

### 5. Streak Motivation

**Streak milestones:**
- Day 1: "🌱 Starting fresh! Day 1 of building a habit."
- Day 3: "🔥 3 days! The habit is forming."
- Day 7: "⭐ One week streak! You're building momentum."
- Day 14: "🚀 Two weeks! This is becoming second nature."
- Day 30: "🏆 30-day streak! You're a consistency master!"
- Day 60+: "💎 [X]-day streak! Legendary dedication!"

**If streak breaks:**
```
Your streak reset, but that's okay! Every master has off days.
Previous best: [X] days
Current: 1 day (fresh start!)

"The best time to start was yesterday. The second best time is now."
```

## How the Revision Tracker Works

### File Structure: `tracking/revision-tracker.json`

```json
{
  "last_check_in": "2026-01-20",
  "current_streak": 5,
  "best_streak": 12,
  "total_problems_solved": 25,
  "last_revision_session": "2026-01-19",
  "problems": {
    "LC-1": {
      "name": "Two Sum",
      "pattern": "Hash Table",
      "date_solved": "2026-01-10",
      "revisions": [
        {
          "date": "2026-01-11",
          "quality": 4,
          "next_review": "2026-01-18"
        },
        {
          "date": "2026-01-18",
          "quality": 5,
          "next_review": "2026-01-25"
        }
      ],
      "next_review": "2026-01-25"
    }
  }
}
```

### When Tracker Updates:
- **After `/revise` session**: Add revision entry, update next_review date
- **After `/learn` completion**: Add new problem
- **After `/daily-check`**: Update last_check_in, calculate streak

## Integration with Other Workflows

### `/revise` Workflow Update
After each problem review, update tracker:
```
User rates recall quality (1-5 stars)
→ Calculate next review date:
  ⭐⭐⭐⭐⭐ (5 stars) → +7 days
  ⭐⭐⭐⭐ (4 stars)   → +5 days
  ⭐⭐⭐ (3 stars)     → +3 days
  ⭐⭐ (2 stars)       → +1 day
  ⭐ (1 star)         → today (immediate redo)
→ Save to tracker
```

### `/learn` Workflow Update
After documenting a new problem:
```
→ Add problem to tracker
→ Set first review date: tomorrow
```

## Guidelines for AI Assistant

1. **Be encouraging, not guilt-tripping**
   - ✅ "Welcome back! Let's refresh those patterns."
   - ❌ "You missed 5 days. You're falling behind."

2. **Keep it fast** (< 30 seconds to read)
   - Show only essential info
   - Use emojis for quick scanning
   - Avoid long explanations

3. **Make it actionable**
   - Always suggest next step
   - Provide one-command solutions
   - Remove decision fatigue

4. **Celebrate progress**
   - Highlight streak milestones
   - Note pattern improvements
   - Track total problems solved

5. **Adapt to context**
   - Sunday evening: "Great week! Here's what's coming Monday..."
   - Monday morning: "Start strong! Here's today's quick review..."
   - Late at night: "Quick check before bed. Tomorrow's plan ready!"

## Usage

### Start Your Day Right
```bash
# Morning routine:
1. Open workspace
2. Type: /daily-check
3. See what's due
4. Run /revise if needed
5. Get to work!
```

### Quick Evening Check
```bash
# Before closing workspace:
1. Type: /daily-check
2. If missed revisions: Schedule for tomorrow
3. Feel good about progress
```

## Benefits

✅ **Prevents forgetting**: See what's due before it slips  
✅ **Builds habits**: Streak tracking motivates consistency  
✅ **Reduces anxiety**: Know exactly what needs attention  
✅ **Quick feedback**: 30-second check vs. 30-minute "what should I do?"  
✅ **Flexible**: Skip days without guilt, just see updated plan  

## Optional Enhancements

If you want to supercharge this:

1. **Weekly Report**: Every Sunday, show pattern mastery stats
2. **GitHub Integration**: Auto-commit tracker updates
3. **Slack/Discord Webhook**: Daily reminder DM
4. **Flashcard Integration**: Link to Anki/flashcard system
5. **Goal Setting**: "Solve X problems this week" progress bar

---

**Remember**: The goal isn't perfection. It's consistent progress. Even checking in (without reviewing) keeps you connected to your learning journey. 🌟
