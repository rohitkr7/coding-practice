---
description: Quick reference guide for using workflows
---

# Cascade Workflows - Quick Reference Card

## 🎯 What Are Workflows?

Workflows are structured guides that Cascade follows to help you with multi-step processes. Think of them as "recipes" for common tasks.

## 🚀 How to Use

### Method 1: Slash Command (Easiest)
```
/review
/learn
/document
```

### Method 2: Natural Language
```
"quick review this problem"
"start learning"
"debug this solution"
```

### Method 3: Explicit Reference
```
@problem-file.md Use the quick-review workflow
```

## 📚 Available Workflows

### 1️⃣ Learning & Practice

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| **Start Learning** | `start-problem-learning.md` | `/learn` | Begin new problem with hints |
| **Quick Review** | `quick-review.md` | `/review` | Review solved problem |
| **Debug Solution** | `debug-solution.md` | `debug this` | Systematically debug issues |

### 2️⃣ Documentation

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| **Document Solution** | `document-solution.md` | `/document` | Comprehensively document completed solution |

### 3️⃣ Guides & Templates

| File | Purpose |
|------|---------|
| `WORKFLOW_SLASH_COMMAND_GUIDE.md` | Complete guide on creating and using workflows |
| `WORKFLOWS_QUICK_REFERENCE.md` | This file - quick reference |
| `README.md` | Overview of workflow system |

## ⚡ Quick Examples

### Example 1: Starting a New Problem
```
# Open: LND-45-merge-intervals.md

You: "/learn"

Cascade:
✅ Analyzes problem
✅ Identifies pattern (Merge Intervals)
✅ Provides core concepts
✅ Gives progressive hints
✅ Guides without spoiling solution
```

### Example 2: Quick Review After Solving
```
# Just completed: LND-30-contains-duplicate.md

You: "/review"

Cascade:
📋 Problem summary
🎯 Pattern identification
⚡ Complexity analysis
💡 Key takeaways
➡️ Next similar problems
```

### Example 3: Debugging a Solution
```
# Tests failing on: LND-42-two-sum.md

You: "debug this solution"

Cascade:
🔍 Identifies failing test
🧪 Suggests logging points
📊 Traces execution
💭 Forms hypotheses
🛠️ Guides toward fix (no spoilers!)
```

## 🎨 Workflow Features

### ✅ What Workflows DO:
- Provide structured, step-by-step guidance
- Maintain consistency across sessions
- Ensure nothing is missed
- Teach problem-solving patterns
- Guide without spoiling solutions

### ❌ What Workflows DON'T Do:
- Give away solutions immediately
- Replace your thinking process
- Work without context
- Guarantee correct solutions

## 🛠️ Creating Custom Workflows

### Quick Template:
```markdown
# My Workflow Name

**Purpose**: One-sentence description

**Trigger**: Commands that invoke this

**When to Use**: Scenarios for usage

---

## Workflow Steps

### Step 1: [Name]
- What to analyze
- Questions to answer

**Cascade Action**: Specific instructions

### Step 2: [Name]
...
```

### Save as:
`.windsurf/workflows/my-workflow-name.md`

### Use it:
```
"use my workflow name"
```

## 📖 Learn More

| Want to... | Read... |
|-----------|---------|
| Understand workflows deeply | `WORKFLOW_SLASH_COMMAND_GUIDE.md` |
| See all workflow details | Individual workflow `.md` files |
| Learn about commands | `.windsurf/cascadeCustomCommands.json` |
| Understand system design | `.windsurf/workflows/README.md` |

## 🎓 Your Learning Workflow

Your complete learning cycle:

```
1. Start New Problem
   ↓ /learn
   
2. Work on Solution
   ↓ (get hints as needed: /hint)
   
3. Debug if Needed
   ↓ "debug this"
   
4. Document Solution
   ↓ /document
   
5. Quick Review
   ↓ /review
   
6. Find Similar Problems
   ↓ /similar
   
7. Repeat! 🔄
```

## 💡 Pro Tips

### Tip 1: Chain Workflows
```
"Let's use /learn to start, then when I'm done, use /document"
```

### Tip 2: Customize Triggers
Add your own keywords to workflow files to trigger them naturally

### Tip 3: Combine with Context
```
"@two-sum.md @merge-intervals.md compare these using review workflow"
```

### Tip 4: Iterate
Workflows improve with use - update them as you learn what works!

### Tip 5: Use // turbo
Add `// turbo` before a step to auto-run commands without approval

## 🆘 Troubleshooting

### Workflow not triggering?
- Check file is in `.windsurf/workflows/`
- Try explicit: `use the [workflow-name] workflow`
- Verify markdown formatting

### Cascade not following steps?
- Make "Cascade Action" sections more specific
- Add example outputs
- Break complex steps into smaller ones

### Not getting expected results?
- Provide more context (attach problem file)
- Be specific about what you want
- Ask Cascade to explain its interpretation

## 📊 Workflow Comparison

| Need | Quick Command | Full Workflow | Best When |
|------|---------------|---------------|-----------|
| Single hint | `/hint` | - | Stuck on one thing |
| Pattern ID | `/pattern` | - | Just need pattern |
| Full guidance | `/learn` | `start-problem-learning.md` | New problem |
| Document | `/document` | `document-solution.md` | After solving |
| Review | `/review` | `quick-review.md` | Quick refresher |
| Debug | - | `debug-solution.md` | Systematic debugging |

## 🎯 Next Steps

1. ✅ **Try it now**: Pick a problem and use `/review`
2. 📝 **Create custom**: Use template above for your needs
3. 🔄 **Iterate**: Refine workflows as you use them
4. 📚 **Share**: Document what works for future you

---

## Remember:

> **Workflows are tools to enhance your learning, not replace it.**
> **They guide you to discover solutions, not hand them to you.**
> **The best workflow is one that fits YOUR learning style.**

---

**Questions?** Check `WORKFLOW_SLASH_COMMAND_GUIDE.md` for detailed explanations!

**Want to create your own?** Follow the template in the guide!

**Happy Learning! 🚀**
