# 🚀 Problem Learning Workflow Guide

This guide explains how to use Windsurf workflows to streamline your problem-solving learning process with Cascade AI.

---

## 📋 Overview

Windsurf workflows provide integrated AI assistance directly in Cascade. Simply reference a workflow and problem file to get structured guidance.

---

## 🎯 Quick Start

### Starting a New Problem

When you want to start learning a new problem, use the learning workflow in Cascade:

```
@[/start-problem-learning] @[problems/two-pointers/LND-30-2-contains-duplicate.md]
```

This will:
1. ✅ Analyze the problem file
2. ✅ Extract key information (title, pattern, difficulty, etc.)
3. ✅ Provide core concepts teaching
4. ✅ Guide with hints and questions (not solutions)
5. ✅ Explain pattern recognition
6. ✅ Walk through approaches step-by-step

**Cascade responds immediately with structured guidance!**

---

### Documenting a Completed Problem

When you've solved a problem and want to document it:

```
@[/document-solution] @[problems/two-pointers/LND-29-1-two-sum.md]
```

This asks Cascade to help you:
- Add well-commented code with JavaDoc
- Create visual walkthroughs
- Document complexity analysis
- Record key learnings and mistakes
- Add comprehensive test cases
- Link to similar problems
- Create a quick reference card

---

## 📁 File Structure

```
LnD/
├── start_problem.py        # Python script that does the work
├── start-problem.sh        # Shell wrapper for easy usage
└── WORKFLOW_GUIDE.md       # This file
```

---

## 🔧 Installation & Setup

### Prerequisites

1. **Python 3.x** (already installed on your system)
2. **Optional:** Install `pyperclip` for auto-copy to clipboard

```bash
pip install pyperclip
```

### Make Script Executable

```bash
chmod +x start-problem.sh
```

---

## 💡 Usage Examples

### Example 1: Start Learning a New Problem

```bash
# Navigate to your LnD directory
cd /Users/rohit.roy/Documents/LnD

# Run the workflow
./start-problem.sh problems/two-pointers/LND-30-2-contains-duplicate.md
```

**Output:**
```
📖 Reading problem file: /Users/rohit.roy/Documents/LnD/problems/two-pointers/LND-30-2-contains-duplicate.md
✅ Found problem: 2 - Contains Duplicate

🎓 **LEARNING PROMPT** (Copy and paste to Cascade):

================================================================================
🎯 **Starting New Problem: 2 - Contains Duplicate**

📋 **Problem Details:**
- **Pattern:** Two Pointers
- **Difficulty:** Easy
- **Status:** In Progress
- **LeetCode:** https://leetcode.com/problems/contains-duplicate
- **Jira:** LND-30

---

🎓 **Learning Request:**

I want to learn how to solve this problem step-by-step. Please provide:

1. **Core Concepts** - What fundamental concepts do I need to understand?
2. **Pattern Recognition** - Why is this problem categorized under "Two Pointers"?
...
================================================================================

✅ Prompt copied to clipboard!
```

**Now just paste into Cascade and start learning!**

---

### Example 2: Document a Completed Solution

```bash
./start-problem.sh --complete problems/two-pointers/LND-29-1-two-sum.md
```

This generates a completion prompt that asks Cascade to help you document everything comprehensively.

---

## 🎨 What the Workflow Generates

### For New Problems (Learning Mode)

The generated prompt asks Cascade to provide:

1. **Core Concepts** 🧠
   - Fundamental concepts needed
   - Prerequisites and background knowledge

2. **Pattern Recognition** 🔍
   - Why this pattern applies
   - Clues in the problem statement

3. **Approach Analysis** 📊
   - Brute force approach
   - Optimized approaches
   - Trade-offs between approaches

4. **Key Insights** 💡
   - The "aha!" moment
   - What makes the solution work

5. **Implementation Guidance** 🛠️
   - Hints and guidance (NOT complete solutions)
   - Step-by-step thinking process

6. **Edge Cases** ⚠️
   - What to watch out for
   - Common pitfalls

7. **Complexity Analysis** 📈
   - Time complexity breakdown
   - Space complexity trade-offs

---

### For Completed Problems (Documentation Mode)

The generated prompt asks Cascade to help you create:

1. **Well-Commented Code** 💻
   - Comprehensive inline comments
   - JavaDoc/docstring documentation
   - Implementation notes

2. **Visual Walkthrough** 🎨
   - Step-by-step example
   - ASCII diagrams
   - State transitions

3. **Complexity Analysis** 📊
   - Detailed time complexity
   - Detailed space complexity
   - Comparison with other approaches

4. **Key Learnings** 🎓
   - What you learned
   - Mistakes you made
   - Pattern insights

5. **Test Cases** 🧪
   - Comprehensive test coverage
   - Edge cases
   - Explanations

6. **Similar Problems** 🔗
   - Related problems to practice
   - Pattern variations
   - Next steps

7. **Quick Reference** 📝
   - Template code
   - Key formulas
   - Pattern summary

---

## 🔄 Typical Workflow

Here's how you'd use this in your daily practice:

### 1. **Pick a Problem from Jira**
```bash
# Look at your Jira board or PROBLEM_INDEX.md
```

### 2. **Start Learning**
```bash
./start-problem.sh problems/two-pointers/LND-30-2-contains-duplicate.md
# Paste the generated prompt into Cascade
```

### 3. **Learn with Guidance**
- Cascade provides hints and concepts
- You think through the problem
- You implement the solution
- You test on LeetCode

### 4. **Document Your Solution**
```bash
./start-problem.sh --complete problems/two-pointers/LND-30-2-contains-duplicate.md
# Paste the generated prompt into Cascade
```

### 5. **Review and Move On**
- Your problem file is now fully documented
- You have a reference for future review
- Move to the next problem!

---

## 🎯 Benefits

### ⏱️ **Saves Time**
- No need to manually write learning prompts
- Consistent format every time
- Quick command-line usage

### 📚 **Better Learning**
- Structured learning approach
- Focuses on concepts, not just solutions
- Encourages pattern recognition

### 📖 **Better Documentation**
- Comprehensive problem documentation
- Easy to review later
- Consistent format across all problems

### 🔄 **Repeatable Process**
- Same workflow for every problem
- Build good habits
- Track progress systematically

---

## 🛠️ Customization

### Modify the Learning Prompt

Edit `start_problem.py` and update the `generate_learning_prompt()` function:

```python
def generate_learning_prompt(info):
    """Generate a comprehensive learning prompt based on problem info."""
    
    prompt = f"""
    # Add your custom prompt template here
    """
    
    return prompt.strip()
```

### Modify the Completion Prompt

Edit `start_problem.py` and update the `generate_completion_prompt()` function.

---

## 🐛 Troubleshooting

### Script Not Executable
```bash
chmod +x start-problem.sh
```

### Python Not Found
```bash
# Check Python installation
python3 --version

# If not installed, install Python 3
```

### File Not Found
```bash
# Make sure you're in the LnD directory
cd /Users/rohit.roy/Documents/LnD

# Use relative or absolute paths
./start-problem.sh problems/two-pointers/LND-30-2-contains-duplicate.md
```

### Clipboard Not Working
```bash
# Install pyperclip for auto-copy
pip install pyperclip

# Or manually copy the output
```

---

## 📝 Tips & Best Practices

### 1. **Use Tab Completion**
```bash
./start-problem.sh problems/two-<TAB>
# Your shell will auto-complete the path
```

### 2. **Create Aliases**
Add to your `~/.zshrc` or `~/.bashrc`:

```bash
alias learn='cd /Users/rohit.roy/Documents/LnD && ./start-problem.sh'
alias complete='cd /Users/rohit.roy/Documents/LnD && ./start-problem.sh --complete'
```

Then you can use:
```bash
learn problems/two-pointers/LND-30-2-contains-duplicate.md
complete problems/two-pointers/LND-29-1-two-sum.md
```

### 3. **Keep Problem Files Updated**
- Make sure your problem files have the standard format
- Include all metadata (Jira ticket, LeetCode URL, etc.)
- The script extracts information from these fields

### 4. **Use with Cascade**
- The prompts are designed specifically for Cascade AI
- They align with your learning preferences (hints, not solutions)
- They follow the 16 coding patterns approach

---

## 🔗 Integration with Your Workflow

This workflow integrates seamlessly with your existing setup:

- ✅ **Jira Integration** - References your Jira tickets
- ✅ **LeetCode Links** - Includes LeetCode problem URLs
- ✅ **Pattern-Based Learning** - Organized by the 16 coding patterns
- ✅ **Problem Templates** - Works with your existing problem file format
- ✅ **Cascade AI** - Optimized for your AI learning assistant

---

## 📚 Related Documentation

- [GETTING_STARTED.md](./GETTING_STARTED.md) - Initial setup guide
- [PATTERNS_GUIDE.md](./PATTERNS_GUIDE.md) - Overview of the 16 patterns
- [SOLUTION_TEMPLATE.md](./SOLUTION_TEMPLATE.md) - Problem file template
- [10_WEEK_STUDY_PLAN.md](./10_WEEK_STUDY_PLAN.md) - Your study schedule

---

## 🎉 Summary

**Starting a new problem:**
```bash
./start-problem.sh <problem_file>
```

**Documenting a completed problem:**
```bash
./start-problem.sh --complete <problem_file>
```

**That's it!** Copy the generated prompt, paste into Cascade, and start learning! 🚀

---

**Happy Learning!** 📚✨
