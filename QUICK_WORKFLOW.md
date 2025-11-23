# ⚡ Quick Workflow - Windsurf Workflows

Use Windsurf workflows to streamline your problem-solving with Cascade AI.

---

## 🚀 Starting a New Problem

In Windsurf Cascade, use:

```
@[/start-problem-learning] @[path/to/problem-file.md]
```

**Example:**
```
@[/start-problem-learning] @[problems/two-pointers/LND-30-2-contains-duplicate.md]
```

**What it does:**
1. ✅ Analyzes the problem file
2. ✅ Provides core concepts teaching
3. ✅ Guides with hints (not solutions)
4. ✅ Explains pattern recognition
5. ✅ Walks through approaches step-by-step

---

## ✅ Documenting a Completed Problem

After solving, document your solution:

```
@[/document-solution] @[path/to/problem-file.md]
```

**Example:**
```
@[/document-solution] @[problems/two-pointers/LND-29-1-two-sum.md]
```

**What it does:**
1. ✅ Adds comprehensive code comments
2. ✅ Creates visual walkthroughs
3. ✅ Documents complexity analysis
4. ✅ Records key learnings and mistakes
5. ✅ Adds test cases and similar problems
6. ✅ Creates quick reference card

---

## 💡 Pro Tips

### Available Workflows

All workflows in `.windsurf/workflows/`:
- `/start-problem-learning` - Start learning a new problem
- `/document-solution` - Document completed solution
- `/debug-solution` - Debug a failing solution
- `/quick-review` - Quick review of solution
- `/study-helper` - Track progress from Jira

### Quick Access

Type `/` in Cascade to see all available workflows!

### Natural Language

Cascade also understands natural language:
- "start learning" → triggers learning workflow
- "document this" → triggers documentation workflow
- "help me debug" → triggers debug workflow

---

## 📖 Full Documentation

See [WORKFLOW_GUIDE.md](./WORKFLOW_GUIDE.md) for complete documentation.

---

## 🎯 Typical Daily Workflow

```bash
# 1. Pick a problem from your Jira board
# 2. Start learning
./start-problem.sh problems/pattern-name/problem-file.md

# 3. Paste prompt into Cascade
# 4. Learn with guidance (hints, not solutions)
# 5. Implement and test on LeetCode
# 6. Document your solution
./start-problem.sh --complete problems/pattern-name/problem-file.md

# 7. Paste prompt into Cascade
# 8. Your problem file is now fully documented!
```

---

**That's it!** Two simple commands for your entire learning workflow. 🎉
