# 📊 Problem Tracker Guide

## Overview

The problem tracker automatically maintains an up-to-date list of all coding problems in your repository, showing their status, difficulty, and providing quick links to both the problem files and external resources.

---

## 🎯 Features

### Automatic Tracking
- Scans all problem files in `problems/` directory
- Extracts metadata (status, difficulty, pattern, title)
- Generates organized tables by pattern
- Shows progress statistics

### Visual Organization
- **Status Icons:**
  - ✅ Completed
  - ⏳ To Do
  - 🟡 In Progress
  - 🟠 Stuck

- **Difficulty Badges:**
  - 🟢 Easy
  - 🟡 Medium
  - 🔴 Hard

### Quick Access
- Clickable links to problem documentation files
- Direct links to LeetCode problems
- Jira ticket references
- Progress tracking per pattern

---

## 🚀 How to Use

### After Solving a Problem

1. **Document your solution** using `/document-solution` workflow
2. **Update the tracker** automatically:
   ```bash
   ./update_tracker.sh
   ```
   or
   ```bash
   python3 update_problem_tracker.py
   ```

### View Your Progress

Open `README.md` and scroll to the **Problem Tracker** section to see:
- Overall progress percentage
- Progress by pattern category
- All problems organized in tables
- Quick links to everything

---

## 📁 File Structure

```
/Users/rohit.roy/Documents/LnD/
├── README.md                      # Contains the tracker table
├── update_problem_tracker.py      # Main tracker script
├── update_tracker.sh              # Quick wrapper script
└── problems/
    ├── two-pointers/
    │   ├── LND-27-3-valid-anagram.md  ✅
    │   ├── LND-29-1-two-sum.md        ⏳
    │   └── ...
    ├── binary-search/
    │   └── ...
    └── ...
```

---

## 🔄 Workflow Integration

The tracker is automatically integrated into the `/document-solution` workflow:

**Step 10** of documentation workflow:
```markdown
### 10. Update README Problem Tracker
After documenting the solution, update the centralized problem tracker:
- Run the tracker update script
- README.md is automatically updated
- Shows current progress across all patterns
```

---

## 🛠️ How It Works

### 1. Scanning
The script walks through all subdirectories in `problems/`:
```python
for root, dirs, files in os.walk(problems_dir):
    for file in files:
        if file.endswith('.md') and file.startswith('LND-'):
            # Extract metadata from file
```

### 2. Extracting Metadata
From each problem file, it extracts:
- **Title:** First heading (e.g., "3 - Valid Anagram")
- **Status:** From `**Status:**` field
- **Difficulty:** From `**Difficulty:**` field
- **Pattern:** From `**Pattern:**` field
- **LeetCode URL:** From `**LeetCode:**` field
- **Jira Ticket:** From markdown link format

### 3. Generating Tables
Organizes problems by pattern and creates markdown tables:
```markdown
| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ✅ | [3 - Valid Anagram](problems/...) | 🟢 Easy | LND-27 | [LC](...) |
```

### 4. Updating README
Inserts the generated tracker between special markers:
```html
<!-- PROBLEM_TRACKER_START -->
[Generated tracker content]
<!-- PROBLEM_TRACKER_END -->
```

---

## 📊 Example Output

```markdown
## 📊 Problem Tracker

**Progress:** 3/77 problems completed (3%)

---

### Hash Table / Frequency Counter
**Progress:** 1/1 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ✅ | [3 - Valid Anagram](problems/two-pointers/LND-27-3-valid-anagram.md) | 🟢 Easy | LND-27 | [LC](https://leetcode.com/problems/valid-anagram) |

### Two Pointers
**Progress:** 0/20 completed

| Status | Problem | Difficulty | Jira | Links |
|--------|---------|------------|------|-------|
| ⏳ | [1 - Two Sum](problems/two-pointers/LND-29-1-two-sum.md) | 🟢 Easy | LND-29 | [LC](https://leetcode.com/problems/two-sum) |
...
```

---

## 🎨 Customization

### Adding New Status Types
Edit `update_problem_tracker.py` and modify the `generate_status_icon()` function:
```python
def generate_status_icon(status):
    status_lower = status.lower()
    if '✅' in status or 'completed' in status_lower:
        return '✅'
    elif 'your-custom-status' in status_lower:
        return '🆕'  # Your custom icon
    # ... more cases
```

### Changing Difficulty Colors
Modify the `generate_difficulty_badge()` function:
```python
def generate_difficulty_badge(difficulty):
    if difficulty.lower() == 'easy':
        return '🟢 Easy'  # Change emoji/text
    # ... more cases
```

---

## 💡 Tips

1. **Run after every documented problem** to keep the tracker current
2. **Check the tracker before starting** to see what's left to do
3. **Use it for weekly reviews** to see progress over time
4. **Filter by pattern** to focus on specific topics
5. **Share your progress** - the tracker makes it easy to show what you've accomplished!

---

## 🐛 Troubleshooting

### Tracker not updating?
```bash
# Check if script is executable
chmod +x update_tracker.sh

# Run manually to see errors
python3 update_problem_tracker.py
```

### Missing problems in tracker?
- Ensure problem files are named `LND-*.md`
- Check that files have `**Status:**`, `**Difficulty:**`, and `**Pattern:**` fields
- Verify files are in the `problems/` directory or subdirectories

### Incorrect status showing?
- Check the status field in your problem file
- Ensure it matches expected values: "To Do", "✅ Completed", "In Progress", "Stuck"
- Re-run the tracker script after fixing

---

## 📚 Related Files

- **Main Script:** `update_problem_tracker.py`
- **Wrapper:** `update_tracker.sh`
- **Workflow:** `.windsurf/workflows/document-solution.md`
- **Output:** `README.md` (Problem Tracker section)
- **This Guide:** `TRACKER_GUIDE.md`

---

## ✅ Current Statistics

As of the last update:
- **Total Problems:** 77
- **Completed:** 3 (3%)
- **Patterns Covered:** 16
- **Latest Completion:** Valid Anagram (LND-27) ✅

---

**Keep solving and tracking your progress!** 🚀
