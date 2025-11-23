# Custom Slash Commands Guide

This guide explains how to use custom commands in Windsurf Cascade.

---

## 📋 Available Custom Commands

I've created the following custom commands for your learning workflow:

### `/learn` - Start Learning a Problem
Provides structured guidance with hints and concepts (no complete solutions).

**Usage:**
```
/learn
```

**What it does:**
- Explains core concepts
- Identifies patterns
- Analyzes approaches
- Provides key insights
- Guides implementation
- Discusses edge cases
- Analyzes complexity

---

### `/document` - Document Completed Solution
Helps create comprehensive documentation for a solved problem.

**Usage:**
```
/document
```

**What it does:**
- Adds well-commented code
- Creates visual walkthroughs
- Documents complexity analysis
- Records key learnings
- Generates test cases
- Lists similar problems
- Creates quick reference

---

### `/hint` - Get a Hint
Provides a nudge in the right direction without spoiling the solution.

**Usage:**
```
/hint
```

**What it does:**
- Asks what you've tried
- Identifies where you're stuck
- Gives targeted hints
- Suggests next steps

---

### `/pattern` - Identify Pattern
Helps recognize which coding pattern applies to the problem.

**Usage:**
```
/pattern
```

**What it does:**
- Identifies applicable patterns
- Explains pattern characteristics
- Points out clues in problem
- Discusses when to use pattern

---

### `/complexity` - Analyze Complexity
Guides you through time/space complexity analysis.

**Usage:**
```
/complexity
```

**What it does:**
- Analyzes time complexity
- Analyzes space complexity
- Compares approaches
- Discusses trade-offs

---

### `/test` - Generate Test Cases
Creates comprehensive test cases for the problem.

**Usage:**
```
/test
```

**What it does:**
- Basic test cases
- Edge cases
- Boundary conditions
- Special values
- Explains each test

---

### `/review` - Review Solution
Provides constructive feedback on your solution code.

**Usage:**
```
/review
```

**What it does:**
- Checks correctness
- Identifies bugs
- Suggests improvements
- Reviews code quality
- Recommends best practices

---

### `/similar` - Find Similar Problems
Suggests related problems to practice the same pattern.

**Usage:**
```
/similar
```

**What it does:**
- Lists problem variations
- Groups by pattern
- Categorizes by difficulty
- Helps build mastery

---

## 🔧 Setup Instructions

### Method 1: JSON Configuration (If Supported)

The file `cascadeCustomCommands.json` has been created with all commands.

**Location:** `.windsurf/cascadeCustomCommands.json`

If Windsurf supports this format, the commands should appear in your `/` menu automatically.

---

### Method 2: Manual Usage (Always Works)

If custom commands don't appear in the `/` menu, you can still use them by typing the command name naturally:

**Instead of:** `/learn`  
**Type:** `Let's start learning this problem`

**Instead of:** `/hint`  
**Type:** `Can you give me a hint?`

**Instead of:** `/pattern`  
**Type:** `What pattern applies here?`

I'll recognize these requests and respond according to the command's purpose!

---

## 🎯 Quick Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/learn` | Start learning | Beginning a new problem |
| `/document` | Document solution | After solving a problem |
| `/hint` | Get a hint | When stuck |
| `/pattern` | Identify pattern | Need pattern recognition help |
| `/complexity` | Analyze complexity | Understanding time/space |
| `/test` | Generate tests | Need test cases |
| `/review` | Review code | Want feedback on solution |
| `/similar` | Find similar | Want more practice |

---

## 💡 Pro Tips

### 1. Combine with File References
```
@[problems/two-pointers/LND-30-2-contains-duplicate.md] /learn
```

### 2. Use in Context
```
I've implemented this solution:
[paste code]

/review
```

### 3. Chain Commands
```
/learn
[work on problem]
/hint
[continue working]
/review
[after solving]
/document
```

---

## 🔍 Troubleshooting

### Commands Don't Appear in `/` Menu

This is normal! Windsurf's custom command support varies by version. You have two options:

**Option A: Use Natural Language**
Instead of `/learn`, just say: "Let's start learning this problem"

**Option B: Check Windsurf Settings**
- Open Windsurf settings
- Look for "Custom Commands" or "Cascade Commands"
- Check if there's a way to import/enable custom commands

---

## 🚀 Alternative: Use Keywords

Since I have these commands in memory, you can trigger them with keywords:

| Keyword | Triggers |
|---------|----------|
| "start learning", "learn this problem" | `/learn` |
| "document this", "help me document" | `/document` |
| "give me a hint", "I'm stuck" | `/hint` |
| "what pattern", "identify pattern" | `/pattern` |
| "analyze complexity", "time complexity" | `/complexity` |
| "test cases", "generate tests" | `/test` |
| "review my code", "feedback" | `/review` |
| "similar problems", "related problems" | `/similar` |

---

## 📚 Examples

### Example 1: Learning a New Problem
```
@[problems/two-pointers/LND-30-2-contains-duplicate.md]

Let's start learning this problem
```

### Example 2: Getting a Hint
```
I'm trying to solve this with a hash map but I'm stuck on handling duplicates.

Can you give me a hint?
```

### Example 3: Documenting Solution
```
I've solved the Two Sum problem! Here's my code:
[paste code]

Help me document this solution
```

---

## 🎓 Best Practices

1. **Start with `/learn`** when beginning a problem
2. **Use `/hint`** when stuck (not `/learn` again)
3. **Use `/pattern`** if you can't identify the pattern
4. **Use `/complexity`** to verify your analysis
5. **Use `/review`** before submitting to LeetCode
6. **Use `/document`** after successful submission
7. **Use `/similar`** to find more practice problems

---

## 🔄 Workflow Integration

### Typical Problem-Solving Flow:

```
1. Open problem file
2. /learn (or "start learning")
3. Think through the problem
4. /hint (if stuck)
5. /pattern (if unsure about pattern)
6. Implement solution
7. /test (verify test cases)
8. /complexity (analyze)
9. /review (get feedback)
10. Submit to LeetCode
11. /document (create documentation)
12. /similar (find next problems)
```

---

## ✨ Summary

**If slash commands work:** Use them directly from the `/` menu

**If they don't work:** Use natural language keywords - I'll recognize them!

Either way, you have powerful commands to streamline your learning! 🚀

---

**Questions?** Just ask! I'm here to help you learn effectively.
