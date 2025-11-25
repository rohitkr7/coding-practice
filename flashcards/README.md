# 🎴 Printable Flashcards System

Sticky-style flashcards for active recall and spaced repetition practice!

---

## 📋 What's Inside

```
flashcards/
├── README.md              ← You are here
├── print-all.html         ← Open in browser to print all cards
├── individual/            ← One markdown file per problem
│   ├── LND-27-valid-anagram.md
│   ├── LND-28-group-anagrams.md
│   ├── LND-29-two-sum.md
│   └── LND-30-contains-duplicate.md
└── by-pattern/            ← Organized by coding pattern (coming soon)
```

---

## 🎴 Flashcard Format

Each flashcard has **TWO SIDES:**

### FRONT (Problem)
- Problem ID and title
- Difficulty badge (🟢 Easy, 🟡 Medium, 🔴 Hard)
- Brief problem description
- 💡 Hints (not solutions!)
- Pattern category

### BACK (Solution)
- 💡 Key insight
- 📝 Approach overview
- 💻 Code template (Java)
- ⏱️ Time complexity
- 💾 Space complexity
- Reference to full solution

---

## 🖨️ How to Print

### Method 1: Print All (Recommended)

1. Open `print-all.html` in your browser
2. File → Print (or Ctrl/Cmd + P)
3. **Important:** Check "Print background graphics/colors"
4. Select your printer or "Save as PDF"
5. Print!

**Result:** Gets 2 cards per problem (front + back)

### Method 2: Print Individual Cards

1. Open any `.md` file in `individual/` folder
2. Copy the ASCII art cards
3. Paste into your favorite note-taking app
4. Print from there

---

## ✂️ After Printing

### Option A: Index Cards (4x6 inches)
- Cut along the borders
- Keep front and back together
- Shuffle and practice!

### Option B: Fold & Cut
- Print double-sided if your printer supports it
- Fold along the middle
- Cut to size
- Perfect sticky notes!

### Option C: Digital Flashcards
- Keep the HTML open on your phone/tablet
- Use for on-the-go review
- No printing needed!

---

## 🔄 Generating Flashcards

### Automatically (Recommended)
When you complete a problem and use `/document` workflow:
```
Flashcard is automatically generated!
```

### Manually for All Completed Problems
```bash
./scripts/generate_flashcards.sh
```

### Manually for Specific Problem
```bash
python3 scripts/generate_flashcard.py problems/hash-table/LND-27-valid-anagram.md
```

---

## 📚 How to Use for Study

### Daily Review (5-10 min)
1. Shuffle your flashcard deck
2. Read front (problem + hints)
3. Try to recall: Pattern, approach, complexity
4. Flip to back to check
5. Mark cards you struggled with

### Spaced Repetition Schedule
- **Day 1:** Learn the problem
- **Day 2:** Review flashcard (1st review)
- **Day 7:** Review flashcard (2nd review)
- **Day 30:** Review flashcard (3rd review)

### Before Interviews
- Review all flashcards in target pattern
- Focus on "hard" difficulty cards
- Practice explaining approach out loud

---

## 🎯 Flashcard Best Practices

### ✅ DO:
- Read hints first, try to solve before flipping
- Cover the back while reading the front
- Say the solution out loud
- Note patterns you struggle with
- Review regularly (not just once)

### ❌ DON'T:
- Peek at the solution immediately
- Skip hints and go straight to code
- Only review once
- Ignore complexity analysis
- Study without actually understanding

---

## 🔧 Customization

### Change Card Size
Edit `print-all.html` CSS:
```css
@page {
    size: 4in 6in;  /* Change to 3x5, A6, etc. */
}
```

### Change Colors
Difficulty borders in `print-all.html`:
```css
.easy { border-color: #28a745; }    /* Green */
.medium { border-color: #ffc107; }  /* Yellow */
.hard { border-color: #dc3545; }    /* Red */
```

---

## 📊 Current Stats

- **Total Flashcards:** 4 problems × 2 cards = 8 cards
- **Patterns Covered:** Hash Table (4 problems)
- **Difficulty:** 3 Easy, 1 Medium
- **Ready to Print:** ✅ Yes!

---

## 🎓 Study Tips

1. **Active Recall:** Don't just read - actively try to remember
2. **Pattern Focus:** Group cards by pattern for focused study
3. **Interleaving:** Mix different patterns for better retention
4. **Explain Out Loud:** Teaching solidifies understanding
5. **Track Progress:** Mark cards you've mastered vs. need review

---

## 🚀 Next Steps

1. Open `print-all.html` in browser
2. Print your first set of flashcards
3. Cut them out
4. Start reviewing!
5. Generate more as you complete problems

---

**Happy Learning!** 🎴✨

Remember: The goal isn't to memorize code, but to recognize patterns and approaches!
