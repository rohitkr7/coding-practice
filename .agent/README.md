# Workflow Migration Guide

## 📁 Dual Workflow System

This project now supports **both Windsurf and Antigravity** workflows!

```
LnD/
├── .windsurf/workflows/     ← Windsurf workflows (original)
└── .agent/workflows/        ← Antigravity workflows (new)
```

Both directories contain the same 6 workflows, adapted for their respective AI assistants.

---

## 🔄 Available Workflows

| Workflow | Slug | Purpose |
|----------|------|---------|
| **Learn** | `/learn` | Start learning a new problem with guided hints |
| **Document** | `/document` | Document completed solutions with automation |
| **Debug** | `/debug` | Systematically debug failing solutions |
| **Review** | `/review` | Quick review of problem and patterns |
| **Revise** | `/revise` | Revise last 5 problems with spaced repetition |
| **Jira** | `/jira` | Track and sync problems from Jira board |

---

## 🔀 Key Differences

### Windsurf Workflows (`.windsurf/workflows/`)
- **Format**: YAML frontmatter + Markdown
- **Cascade Actions**: Uses "Cascade Action" annotations
- **Custom Commands**: Integrates with `.windsurf/cascadeCustomCommands.json`
- **Execution**: Designed for Windsurf's AI (Cascade)

### Antigravity Workflows (`.agent/workflows/`)
- **Format**: YAML frontmatter + Markdown (same structure)
- **Turbo Mode**: Uses `// turbo` annotations for auto-running commands
- **Command Execution**: Auto-runs safe commands when `// turbo` is present
- **Execution**: Designed for Antigravity AI assistant

---

## ⚡ Turbo Mode (Antigravity Only)

Antigravity workflows support **automatic command execution**:

### `// turbo` - Single Step Auto-run
```markdown
// turbo
### Step 4: Generate Flashcard
```bash
python3 scripts/generate_flashcard.py problem.md
```
```
This step will auto-run without asking for permission.

### `// turbo-all` - All Steps Auto-run
```markdown
// turbo-all

### Step 1: Update tracker
```bash
./scripts/update_tracker.sh
```

### Step 2: Generate flashcard
```bash
python3 scripts/generate_flashcard.py problem.md
```
```
ALL bash commands in this workflow will auto-run.

**Note**: windsurf workflows use "Cascade Action" instead of turbo annotations.

---

## 🚀 How to Use

### Using Windsurf
1. Open project in Windsurf
2. Type slash command: `/learn`, `/document`, `/debug`, etc.
3. Windsurf will automatically use workflows from `.windsurf/workflows/`

### Using Antigravity
1. Open project in Antigravity (this editor!)
2. Type slash command: `/learn`, `/document`, `/debug`, etc.
3. Antigravity will automatically use workflows from `.agent/workflows/`
4. Commands marked with `// turbo` will auto-run when appropriate

---

## 📝 Workflow Usage Examples

### 1. Learn a New Problem
```
/learn
```
Then specify which problem file to analyze, or just say:
```
Let's work on LC-1-two-sum.md
```

### 2. Document a Completed Solution
```
/document
```
This will:
- ✅ Add comprehensive code comments
- ✅ Create visual walkthroughs
- ✅ Document complexity analysis
- ✅ Generate flashcard (auto-runs in Antigravity)
- ✅ Update README tracker (auto-runs in Antigravity)

### 3. Debug a Failing Solution
```
/debug
```
Then describe the issue:
```
My solution is failing for input [1,2,3,1], expected True but getting False
```

### 4. Quick Review
```
/review
```
Get a quick summary of the current problem's solution and patterns.

### 5. Revise Recent Problems
```
/revise
```
Test your recall on the last 5 solved problems with spaced repetition.

### 6. Sync with Jira
```
/jira
```
Fetch and sync problems from your Jira board.

---

## 🔧 Maintenance

### Adding a New Workflow

1. **Create in Windsurf**:
   - Add file: `.windsurf/workflows/my-workflow.md`
   - Use "Cascade Action" for automatic actions

2. **Create in Antigravity**:
   - Add file: `.agent/workflows/my-workflow.md`
   - Use `// turbo` for auto-running commands

3. **Keep them in sync** (manually for now)

### Updating Existing Workflows

- **Best Practice**: Update both versions to keep feature parity
- **Windsurf**: Edit `.windsurf/workflows/[name].md`
- **Antigravity**: Edit `.agent/workflows/[name].md`

---

## 🎯 Best Practices

### When to Use Each Tool

**Use Windsurf when:**
- You prefer the Windsurf IDE
- You want Cascade-specific features
- You're already working in Windsurf

**Use Antigravity when:**
- You prefer this editor
- You want turbo mode for faster automation
- You need specific Antigravity features

**Use Both:**
- Switch between them based on your current workflow
- Both will work seamlessly with the same problem files
- Both will update the same README tracker
- Both will generate the same flashcards

---

## 🔗 Integration Points

Both workflow systems integrate with:

✅ **Problem Files** (`problems/*/`)
- Both read/write the same markdown files
- Status updates work the same way

✅ **Scripts** (`scripts/`)
- Same Python scripts used by both
- `generate_flashcard.py`, `update_tracker.py`, etc.

✅ **Jira Integration** (`jira/`)
- Same Jira config and sync scripts
- Same board, same tickets

✅ **Flashcards** (`flashcards/`)
- Same flashcard generation
- Same HTML output

✅ **README Tracker**
- Both update the same progress section
- Visual progress bars sync automatically

---

## 📊 Workflow Comparison

| Feature | Windsurf | Antigravity |
|---------|----------|-------------|
| Auto-complete problems | ✅ | ✅ |
| Generate flashcards | ✅ Manual | ✅ Auto (turbo) |
| Update tracker | ✅ Manual | ✅ Auto (turbo) |
| Jira sync | ✅ | ✅ |
| Pattern guidance | ✅ | ✅ |
| Debug assistance | ✅ | ✅ |
| Spaced repetition | ✅ | ✅ |
| Command format | Cascade Actions | Turbo Mode |

---

## 🆘 Troubleshooting

### "Workflow not found"
- **Windsurf**: Check `.windsurf/workflows/` exists
- **Antigravity**: Check `.agent/workflows/` exists

### "Command didn't auto-run"
- **Antigravity**: Verify `// turbo` annotation is present
- Check that `SafeToAutoRun` would be true for the command

### "Both workflows out of sync"
- Manually compare and update both versions
- Focus on keeping the logic the same, adjust syntax for each tool

---

## 💡 Tips

1. **Start with one tool** - Master workflows in your preferred editor first
2. **Keep both updated** - When you improve a workflow, update both versions
3. **Use automation** - Leverage `// turbo` in Antigravity for faster workflows
4. **Stay organized** - Both tools work with the same file structure
5. **Switch freely** - No lock-in, use whichever tool fits your current task

---

## 📚 Resources

- **Windsurf Workflows**: `.windsurf/workflows/`
- **Antigravity Workflows**: `.agent/workflows/`
- **Patterns Guide**: `PATTERNS_GUIDE.md`
- **Solution Template**: `SOLUTION_TEMPLATE.md`
- **Main README**: `README.md`

---

**Happy Learning! 🚀**

Use the best tool for each task, and let the workflows guide your learning journey!
