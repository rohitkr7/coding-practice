# Windsurf Cascade Workflows

This directory contains workflow definitions that Cascade can use to provide structured, consistent assistance for your learning journey.

---

## 📋 Available Workflows

### 1. **study-helper.md**
General study helper workflow for tracking and solving coding problems from your Jira board.

**Use when:** You want general guidance on your study process.

---

### 2. **start-problem-learning.md** ⭐ NEW
Structured workflow for learning a new problem with guided hints and concepts.

**Use when:** Starting a new problem and want step-by-step learning guidance.

**How to use:**
```
@[problem-file.md] Let's start learning this problem using the start-problem-learning workflow.
```

**What it provides:**
- Core concepts explanation
- Pattern recognition guidance  
- Approach analysis (brute force → optimized)
- Key insights and hints (NOT complete solutions)
- Implementation guidance with pseudocode
- Edge cases discussion
- Complexity analysis teaching

---

### 3. **document-solution.md** ⭐ NEW
Structured workflow for documenting a completed solution comprehensively.

**Use when:** You've solved a problem and want to document it for future reference.

**How to use:**
```
@[problem-file.md] I've solved this problem. Let's document it using the document-solution workflow.
```

**What it provides:**
- Well-commented code with explanations
- Visual step-by-step walkthrough
- Detailed complexity analysis
- Key learnings and mistakes
- Comprehensive test cases
- Similar problems list
- Quick reference card

---

## 🎯 How Workflows Work

Windsurf Cascade workflows are markdown files that define:
1. **Purpose** - What the workflow accomplishes
2. **Steps** - Structured steps to follow
3. **Principles** - Guidelines for execution
4. **Output Format** - How to structure responses

When you reference a workflow, Cascade follows these guidelines to provide consistent, high-quality assistance.

---

## 💡 Usage Tips

### Reference a Workflow
```
Let's use the [workflow-name] workflow for this task.
```

### Reference Problem File + Workflow
```
@[problems/two-pointers/LND-30-2-contains-duplicate.md] 
Let's start learning this using the start-problem-learning workflow.
```

### Combine with Context
```
@[problem-file.md] I'm stuck on the approach. 
Can you use the start-problem-learning workflow to guide me through the pattern recognition?
```

---

## 🔄 Workflow vs Command-Line Tools

### Windsurf Workflows (This Directory)
- **Location:** `.windsurf/workflows/*.md`
- **Usage:** Reference in Cascade chat
- **Purpose:** Guide Cascade's behavior
- **Benefit:** Integrated, context-aware assistance

### Command-Line Tools (Root Directory)
- **Location:** `start_problem.py`, `start-problem.sh`
- **Usage:** Run in terminal
- **Purpose:** Generate prompts to paste into Cascade
- **Benefit:** Quick automation, clipboard integration

**Both are useful!** Use workflows for integrated Cascade assistance, use command-line tools for quick prompt generation.

---

## 🎓 Best Practices

1. **Starting New Problems:**
   - Option A: Run `./start-problem.sh <file>` and paste prompt
   - Option B: Reference file + mention `start-problem-learning` workflow

2. **Documenting Solutions:**
   - Option A: Run `./start-problem.sh --complete <file>` and paste prompt
   - Option B: Reference file + mention `document-solution` workflow

3. **General Study Help:**
   - Reference the `study-helper` workflow

---

## 📚 Related Documentation

- **Command-Line Tools:** See `/WORKFLOW_GUIDE.md` and `/QUICK_WORKFLOW.md`
- **Problem Templates:** See `/SOLUTION_TEMPLATE.md`
- **Pattern Guide:** See `/PATTERNS_GUIDE.md`

---

## ✨ Examples

### Example 1: Start Learning
```
@[problems/two-pointers/LND-30-2-contains-duplicate.md]

Let's deep dive on this problem using the start-problem-learning workflow. 
Teach me all the concepts to solve this problem.
```

### Example 2: Document Solution
```
@[problems/two-pointers/LND-29-1-two-sum.md]

I've solved this problem! Here's my solution code:
[paste code]

Can you help document this using the document-solution workflow?
```

### Example 3: Pattern Guidance
```
I'm working on a problem that involves finding pairs in an array. 
Which pattern from the study-helper workflow should I consider?
```

---

**Happy Learning!** 🚀
