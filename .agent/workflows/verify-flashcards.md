---
description: Verify flashcard contents are correct and problem-specific
---

# Verify Flashcard Contents Workflow

**Purpose**: Systematically verify that flashcards contain correct, problem-specific content instead of generic algorithms

**Trigger**: Use `/verify-flashcards` command or say "verify flashcards" or "check flashcard content"

**When to Use**:
- After generating new flashcards
- When flashcards have generic "Use HashMap" text
- During quality assurance reviews
- Before printing flashcard sets
- After updating problem files

---

## Workflow Steps

### Step 1: Identify Flashcard to Verify
**Goal**: Determine which flashcard(s) need verification

**Actions**:
- List all generated flashcards in `flashcards/individual/`
- Ask user which specific flashcard to verify, or check all
- Note the problem number (e.g., LC-217, LC-238)

**Example**:
```bash
# List all flashcards
ls flashcards/individual/

# Output: LC-217-contains-duplicate.md, LC-238-product-of-array-except-self.md, etc.
```

---

### Step 2: Check Problem File Has Flashcard Content Section
**Goal**: Verify the source problem file has the required Flashcard Content section

**Actions**:
- Open the corresponding problem file in `problems/hash-table/LC-XXX-problem-name.md`
- Look for `## 🎴 Flashcard Content` section
- Verify it appears BEFORE `## 📚 Resources` section
- Confirm it contains all three required subsections:
  - **HINTS:** (2-3 bullet points with guiding questions)
  - **KEY INSIGHT:** (1-2 sentences describing the core approach)
  - **ALGORITHM:** (4-5 numbered steps, concrete and actionable)

**Expected Format**:
```markdown
## 🎴 Flashcard Content

**HINTS:**
- [Question or hint 1]
- [Question or hint 2]
- [Question or hint 3]

**KEY INSIGHT:**
[Problem-specific approach description]

**ALGORITHM:**
1. [Concrete step 1]
2. [Concrete step 2]
3. [Concrete step 3]
4. [Concrete step 4]
5. [Concrete step 5]
```

**If missing**: Report that the problem file needs a Flashcard Content section added before flashcard can be verified.

---

### Step 3: Verify Generated Flashcard Content
**Goal**: Check that the generated flashcard has correct, problem-specific content

**Actions**:
- Open `flashcards/individual/LC-XXX-problem-name.md`
- Navigate to the `## 🎴 BACK (Solution)` section
- Verify the following elements:

**Checklist**:
- [ ] **KEY INSIGHT** is problem-specific (not generic "Use HashMap to store..." text)
- [ ] **ALGORITHM** lists 4-5 concrete steps specific to THIS problem
- [ ] Complexity notations (⏱️ and 💾) are present and accurate
- [ ] No text truncation or overflow
- [ ] Steps are actionable and clear
- [ ] Content fits within card boundaries (~50 chars per line)

**Example of CORRECT content** (LC-217 Contains Duplicate):
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

**Example of INCORRECT content** (Generic):
```
💡 KEY INSIGHT:
Use HashMap to store value→index

🔢 ALGORITHM:
1. Create HashMap to store value→index
2. For each element:
- Check if complement exists in map
```

---

### Step 4: Compare Against Expected Content
**Goal**: Ensure flashcard matches the problem's Flashcard Content section

**Actions**:
- Compare flashcard's KEY INSIGHT with problem file's KEY INSIGHT
- Compare flashcard's ALGORITHM with problem file's ALGORITHM
- Check for common issues:
  - Wrong algorithm from a different problem (e.g., Two Sum algorithm on Contains Duplicate)
  - Generic text without problem context
  - Missing steps or incomplete algorithm
  - Truncated text due to length

**Report**:
- ✅ If content matches: "Flashcard verified - content is correct and problem-specific"
- ❌ If content differs: List specific discrepancies and what needs to be fixed

---

### Step 5: Regenerate If Incorrect
**Goal**: Fix flashcards that have incorrect content

**Actions**:
- If flashcard content is wrong, regenerate it using the script
- Use the problem file as the source (ensure it has Flashcard Content section)
- Re-verify after regeneration

**Command**:
```bash
python3 scripts/generate_flashcard.py problems/hash-table/LC-XXX-problem-name.md
```

**After regeneration**: Return to Step 3 to verify the fix worked.

---

### Step 6: Batch Verification (Optional)
**Goal**: Verify multiple flashcards efficiently

**Actions**:
- Search for common indicators of incorrect flashcards
- List all flashcards that need attention
- Provide commands to regenerate all at once

**Batch Check Commands**:
```bash
# Find flashcards with generic "HashMap to store" text
grep -l "Use HashMap to store" flashcards/individual/*.md

# Find flashcards missing ALGORITHM section
grep -L "🔢 ALGORITHM:" flashcards/individual/*.md

# Regenerate all flashcards
./scripts/generate_flashcards.sh
```

**Output**: List of problematic flashcards with specific issues identified.

---

### Step 7: Final Visual Inspection
**Goal**: Perform comprehensive quality check

**Actions**:
For each flashcard, verify the complete checklist:

**Complete Verification Checklist**:
- [ ] Problem number and title are correct
- [ ] Pattern and difficulty badge match problem file
- [ ] FRONT section has 2-3 targeted hints
- [ ] FRONT section shows correct problem description
- [ ] BACK section has problem-specific KEY INSIGHT
- [ ] BACK section has 4-5 numbered, concrete ALGORITHM steps
- [ ] Time complexity is accurate (⏱️)
- [ ] Space complexity is accurate (💾)
- [ ] No text overflow or truncation issues
- [ ] Content is problem-specific, not generic
- [ ] Algorithm steps are actionable (not vague)

**Report**: Provide summary of verification status for all checked flashcards.

---

## Example Usage

```
User: "/verify-flashcards" or "check if flashcards are correct"

Response:
🎴 **Flashcard Verification Report**

**Checking**: 4 flashcards in hash-table category

---

✅ **LC-217 Contains Duplicate** - VERIFIED
- KEY INSIGHT: Problem-specific ✓
- ALGORITHM: 5 steps, all specific to duplicate detection ✓
- Content: Fits within boundaries ✓

❌ **LC-238 Product of Array Except Self** - NEEDS FIX
- KEY INSIGHT: Mentions prefix/suffix products ✓
- ALGORITHM: Step 4 is truncated ✗
- Issue: Text overflows card boundary
- Fix: Shorten step descriptions in problem file

✅ **LC-242 Valid Anagram** - VERIFIED
- KEY INSIGHT: Mentions character frequency counting ✓
- ALGORITHM: 4 steps, all specific to anagram validation ✓
- Content: Fits within boundaries ✓

❌ **LC-49 Group Anagrams** - NEEDS FIX
- KEY INSIGHT: Generic "Use HashMap" text ✗
- ALGORITHM: Wrong algorithm (shows Two Sum approach) ✗
- Issue: Problem file missing Flashcard Content section
- Fix: Add Flashcard Content section to problem file, then regenerate

---

**Summary**: 2/4 verified ✓ | 2/4 need fixes ✗

**Next Steps**:
1. Fix LC-238: Shorten algorithm text in problem file
2. Fix LC-49: Add Flashcard Content section to problem file
3. Regenerate both flashcards
4. Re-verify to confirm fixes
```

---

## Integration with Slash Commands

This workflow is designed to work with the custom `/verify-flashcards` command.

**Alternative Triggers**:
- "verify flashcard content"
- "check flashcards for problems"
- "are my flashcards correct"
- "validate flashcard algorithms"

---

## Common Issues and Fixes

### Issue 1: Generic "Use HashMap" Text
**Symptom**: Flashcard shows generic "Use HashMap to store value→index"
**Cause**: Problem file missing Flashcard Content section
**Fix**: Add Flashcard Content section to problem file before `## 📚 Resources`

### Issue 2: Wrong Algorithm
**Symptom**: Flashcard shows Two Sum algorithm on a different problem
**Cause**: Fallback algorithm used when Flashcard Content section missing
**Fix**: Add problem-specific Flashcard Content section, regenerate

### Issue 3: Text Truncation
**Symptom**: Algorithm steps cut off mid-sentence
**Cause**: Text exceeds ~50 characters per line
**Fix**: Shorten descriptions in problem file's Flashcard Content section

### Issue 4: Missing Complexity Notations
**Symptom**: No ⏱️ or 💾 symbols on flashcard
**Cause**: Generator script issue or template problem
**Fix**: Regenerate flashcard, check generator script

### Issue 5: Flashcard Still Wrong After Regeneration
**Symptom**: Content unchanged after running generate script
**Cause**: Flashcard Content section in wrong location (after Resources)
**Fix**: Move Flashcard Content section BEFORE Resources section

---

## Tips for Effective Verification

When executing this workflow:
1. **Start with Batch Check**: Use grep commands to find all problematic flashcards first
2. **Fix Source First**: Always fix problem files before regenerating flashcards
3. **Verify Incrementally**: Check flashcards immediately after generation
4. **Keep Content Concise**: Aim for 40-50 chars per line max
5. **Be Specific**: Avoid vague steps like "Process the data" - be concrete
6. **Test Print**: Verify visual appearance before mass printing

---

## Success Criteria

A flashcard passes verification when:
- ✅ KEY INSIGHT is unique to the problem (no generic text)
- ✅ ALGORITHM has 4-5 concrete, actionable steps
- ✅ All steps are specific to THIS problem's solution
- ✅ Complexity notations are accurate
- ✅ No truncation or overflow issues
- ✅ Content fits within physical card boundaries
- ✅ Problem number, title, pattern, difficulty all match source

---

## Problem-Specific Examples

### LC-217: Contains Duplicate ✅
**KEY INSIGHT**: "Use HashSet to track seen elements - if we see an element that's already in the set, we found a duplicate!"
**ALGORITHM**: HashSet creation → iterate → check existence → add to set → return result
**Pattern**: Hash Table for membership testing

### LC-238: Product of Array Except Self ✅
**KEY INSIGHT**: "Use two passes - prefix products left→right, then multiply by suffix products right→left"
**ALGORITHM**: Create result → forward pass → backward pass → multiply → return
**Pattern**: Prefix-Suffix array manipulation

### LC-242: Valid Anagram ✅
**KEY INSIGHT**: "Count character frequencies - two strings are anagrams if they have identical character counts"
**ALGORITHM**: Check length → count frequencies → compare → return result
**Pattern**: Frequency counter with arrays

### LC-49: Group Anagrams ✅
**KEY INSIGHT**: "Use sorted string as HashMap key - all anagrams will have the same sorted representation"
**ALGORITHM**: Create HashMap → sort each string → use as key → add to list → return values
**Pattern**: Hash Table for grouping by signature

---

## Quick Verification Template

```markdown
🎴 **Flashcard Verification: [Problem Name]**

**File**: flashcards/individual/LC-XXX-problem-name.md
**Status**: [✅ Verified | ❌ Needs Fix | ⚠️ Minor Issues]

---

**KEY INSIGHT Check**:
- [ ] Problem-specific (not generic)
- [ ] Clear and concise
- [ ] Fits within card boundaries
- Content: [Quote the actual text]

---

**ALGORITHM Check**:
- [ ] Has 4-5 numbered steps
- [ ] Steps are concrete and actionable
- [ ] Specific to this problem
- [ ] No truncation
- Steps:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
  4. [Step 4]
  5. [Step 5]

---

**Complexity Check**:
- [ ] Time complexity correct: ⏱️ [Expected]
- [ ] Space complexity correct: 💾 [Expected]

---

**Issues Found**: [List any problems]
**Recommended Action**: [Fix description or "None - verified ✓"]
```
