---
description: Verify flashcard contents are correct and problem-specific
---

# Verify Flashcard Contents Workflow

This workflow systematically verifies that flashcards contain correct, problem-specific content instead of generic algorithms.

## Prerequisites
- Problem file exists in `problems/` directory
- Flashcard has been generated in `flashcards/individual/`

## Steps

### 1. Identify Flashcard to Verify
**Action:** Specify the problem number or flashcard file to verify.

Example:
```bash
# List all flashcards
ls flashcards/individual/
```

### 2. Check Problem File Has Flashcard Content Section
**Action:** Verify the problem file contains a `## 🎴 Flashcard Content` section with:
- HINTS (3 bullet points)
- KEY INSIGHT (problem-specific description)
- ALGORITHM (5-step breakdown)

**Verification:**
```bash
# Search for Flashcard Content section in problem file
grep -A 20 "## 🎴 Flashcard Content" problems/hash-table/LC-XXX-problem-name.md
```

**Expected:** Section exists with all three subsections filled.

### 3. Verify Generated Flashcard Content
**Action:** Open the generated flashcard and check the BACK (Solution) section.

**File location:** `flashcards/individual/LC-XXX-problem-name.md`

**Check for:**
1. **KEY INSIGHT** is problem-specific (not "Use HashMap to store..." generic text)
2. **ALGORITHM** lists 4-5 concrete steps specific to the problem
3. **Complexity notations** (⏱️ and 💾) are present and accurate
4. **No truncation** - all text fits within the card boundaries

### 4. Compare Against Expected Content
**Action:** Verify the flashcard algorithm matches the problem's Flashcard Content section.

**Common issues to catch:**
- Generic "HashMap" or "HashSet" text without problem context
- Wrong algorithm from a different problem
- Missing or incomplete steps
- Truncated KEY INSIGHT or ALGORITHM text

### 5. Regenerate If Incorrect
**Action:** If flashcard has wrong content, regenerate it.

// turbo
```bash
python3 scripts/generate_flashcard.py problems/hash-table/LC-XXX-problem-name.md
```

### 6. Batch Verification (Optional)
**Action:** Verify multiple flashcards at once.

**Script to check all flashcards:**
```bash
# Check which flashcards contain generic "HashMap to store" text
grep -l "Use HashMap to store" flashcards/individual/*.md

# Check which flashcards are missing ALGORITHM section
grep -L "🔢 ALGORITHM:" flashcards/individual/*.md
```

### 7. Visual Inspection Checklist
**For each flashcard, verify:**
- [ ] Problem number and title are correct
- [ ] Pattern/difficulty badge matches problem file
- [ ] HINTS section has 2-3 targeted hints
- [ ] KEY INSIGHT is one clear sentence about the approach
- [ ] ALGORITHM has 4-5 numbered, concrete steps
- [ ] Time/space complexity is accurate
- [ ] No text overflow or truncation
- [ ] Content is problem-specific, not generic

## Expected Outcomes

### ✅ Correct Flashcard Example (LC-217 Contains Duplicate):
```
💡 KEY INSIGHT:
Use HashSet to track seen elements - if we see
an element that's already in the set, we found a

🔢 ALGORITHM:
1. Create empty HashSet
2. For each number in array
3. If number exists in set: return true
4. Add number to set
5. Return false (no duplicates found)
```

### ❌ Incorrect Flashcard Example (Generic):
```
💡 KEY INSIGHT:
Use HashMap to store value→index

🔢 ALGORITHM:
1. Create HashMap to store value→index
2. For each element:
- Check if complement exists in map
- If yes: return indices
- If no: add current to map
```

## Troubleshooting

**Problem:** Flashcard still has wrong content after regeneration
**Solution:** Check that problem file's `## 🎴 Flashcard Content` section exists BEFORE `## 📚 Resources` section

**Problem:** Algorithm text is truncated
**Solution:** Shorten the algorithm steps in the problem file's Flashcard Content section to fit within 50 characters per line

**Problem:** Multiple flashcards need fixing
**Solution:** Use the batch regeneration script:
```bash
./scripts/generate_flashcards.sh
```

## Success Criteria
- All flashcards have problem-specific algorithms
- No generic "Use HashMap" or "Use HashSet" without context
- KEY INSIGHT clearly explains the unique approach
- ALGORITHM steps are concrete and actionable
- All content fits within card boundaries without truncation
