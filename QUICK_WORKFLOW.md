# ⚡ Quick Workflow Commands

Use these commands to streamline your problem-solving workflow with Cascade AI.

---

## 🚀 Starting a New Problem

```bash
./start-problem.sh problems/two-pointers/LND-30-2-contains-duplicate.md
```

**What it does:**
1. Reads your problem file
2. Generates a comprehensive learning prompt
3. Copies it to clipboard (if pyperclip installed)
4. You paste into Cascade and start learning!

---

## ✅ Documenting a Completed Problem

```bash
./start-problem.sh --complete problems/two-pointers/LND-29-1-two-sum.md
```

**What it does:**
1. Generates a documentation prompt
2. Asks Cascade to help you create comprehensive docs
3. Updates your problem file with all learnings

---

## 💡 Pro Tips

### Create Shell Aliases

Add to your `~/.zshrc`:

```bash
# Quick aliases for problem workflow
alias learn='cd /Users/rohit.roy/Documents/LnD && ./start-problem.sh'
alias complete='cd /Users/rohit.roy/Documents/LnD && ./start-problem.sh --complete'
```

Then use anywhere:
```bash
learn problems/two-pointers/LND-30-2-contains-duplicate.md
complete problems/two-pointers/LND-29-1-two-sum.md
```

### Install Clipboard Support

```bash
pip install pyperclip
```

This auto-copies the prompt to your clipboard!

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
