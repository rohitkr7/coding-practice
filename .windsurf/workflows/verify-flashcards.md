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

### Step 3a: Verify HINTS Quality ⚠️ CRITICAL

**Goal**: Ensure hints are complete, meaningful, and not truncated mid-word

**Actions**:

- Navigate to the `## 🎴 FRONT (Problem)` section of the flashcard
- Locate the `💡 HINTS:` section
- Verify each hint individually

**Comprehensive HINTS Checklist**:

- [ ] **All hints are present** (should have 2-3 hints from problem file)
- [ ] **Complete sentences** - no mid-word truncation (e.g., "creating a re..." ❌)
- [ ] **Grammatically correct** - hints make sense when read aloud
- [ ] **Meaningful content** - hints guide thinking, not just generic questions
- [ ] **No critical information lost** due to truncation
- [ ] **Proper punctuation** - questions end with "?" if applicable
- [ ] **Actionable guidance** - hints point toward solution approach

**Example of CORRECT hints** (LC-217 Contains Duplicate):

```
💡 HINTS:
• Have we seen this element before?
• What data structure provides O(1) lookup?
• Do we need to store values or just check existence?
```

✅ All complete sentences, clear meaning, guides toward HashSet solution

**Example of INCORRECT hints** (Truncated):

```
💡 HINTS:
• Have we seen this element bef...   ❌ Truncated mid-word!
• What data structure provides O(1) lo...   ❌ Missing critical word "lookup"
• Do we need to store values or just   ❌ Incomplete sentence!
```

**Example of INCORRECT hints** (Vague/Generic):

```
💡 HINTS:
• What data structure should we use?   ❌ Too generic!
• How to solve this problem?   ❌ No value!
• Think about the approach   ❌ Not actionable!
```

**Specific Truncation Issues to Flag**:

1. **Mid-Word Truncation** ❌ CRITICAL

   - Example: "creating a re..." (should be "reversed string")
   - Example: "aren't evenl..." (should be "evenly distributed")
   - **Action**: Report as MAJOR ISSUE - hints must be shortened in problem file

2. **Missing Critical Words** ❌ CRITICAL

   - Example: "What if elements are" (missing "duplicated" or "repeated")
   - Example: "Can we use a Hash" (missing "Map" or "Set")
   - **Action**: Report as MAJOR ISSUE - obscures meaning

3. **Incomplete Questions** ❌ MAJOR ISSUE

   - Example: "How can you check" (missing object/method)
   - Example: "What data structure for" (missing purpose)
   - **Action**: Report as ISSUE - hint doesn't guide effectively

4. **Acceptable Truncation** (if must fit)
   - Only if full meaning is preserved
   - Only if context makes completion obvious
   - Must end at natural word boundary, not mid-word

**Verification Process**:

For each hint, ask:

1. **Can I read this aloud?** (grammar check)
2. **Does it make complete sense?** (meaning check)
3. **Would this guide someone who's stuck?** (usefulness check)
4. **Is any critical information missing?** (truncation check)

**Comparison with Problem File**:

- Open the problem's `## 🎴 Flashcard Content` section
- Compare flashcard hints with source **HINTS:**
- Calculate truncation severity:
  - **No truncation**: ✅ Perfect
  - **Minor** (ends at word boundary, meaning clear): ✅ Acceptable
  - **Mid-word** truncation: ❌ CRITICAL - must fix
  - **Meaning lost**: ❌ CRITICAL - must fix

**Report Format**:

```markdown
**HINTS Quality Check**:

Hint 1: "How can you check symmetry without creating a re..."

- Status: ❌ CRITICAL - Mid-word truncation
- Issue: "re" is incomplete (should be "reversed string")
- Impact: Obscures the key insight (avoid creating reversed string)
- Fix Required: Shorten to "How to check symmetry without extra space?"

Hint 2: "What if non-alphanumeric characters aren't evenl..."

- Status: ❌ CRITICAL - Mid-word truncation
- Issue: "evenl" is incomplete (should be "evenly distributed")
- Impact: Incomplete sentence, unclear meaning
- Fix Required: Shorten to "What if special chars are scattered?"

Hint 3: [Not visible or truncated completely]

- Status: ❌ MAJOR - Third hint missing from flashcard
- Fix Required: Check if third hint exists in problem file
```

**Action if hints are truncated**:

1. **Flag as CRITICAL ISSUE** in verification report
2. **Recommend shortening hints** in problem file's Flashcard Content section
3. **Provide specific rephrasings** that fit within ~50 character limit
4. **Regenerate flashcard** after fixing problem file
5. **Re-verify** to ensure hints are now complete

**Suggested Hint Length Guidelines**:

- **Target**: 40-45 characters per hint line
- **Maximum**: 50 characters (hard limit for card format)
- **Best practice**: Keep hints concise, sacrifice detail if needed
- **Tip**: Use abbreviations sparingly but strategically

**Examples of Good Short Hints**:

- "Need O(1) lookup?" (16 chars) ✅
- "Track seen values?" (18 chars) ✅
- "Can elements repeat?" (20 chars) ✅
- "Sorted input?" (13 chars) ✅
- "Two pointers from edges?" (24 chars) ✅

**Examples of Hints to Shorten**:

- "How can you check for symmetry without creating a reversed string?"
  - **Shorten to**: "Check symmetry without reversing?"
- "What if the non-alphanumeric characters aren't evenly distributed?"
  - **Shorten to**: "What if special chars scattered?"
- "How do you prevent going out of bounds when skipping invalid characters?"
  - **Shorten to**: "How to avoid index errors when skipping?"

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
- [ ] HINTS are complete sentences (no mid-word truncation)
- [ ] HINTS make grammatical sense when read aloud
- [ ] HINTS guide thinking without revealing solution
- [ ] HINTS are specific to the problem (not generic)
- [ ] FRONT section shows correct problem description
- [ ] BACK section has problem-specific KEY INSIGHT
- [ ] BACK section has 4-5 numbered, concrete ALGORITHM steps
- [ ] Time complexity is accurate (⏱️)
- [ ] Space complexity is accurate (💾)
- [ ] No text overflow or truncation issues (especially in HINTS)
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

### Issue 6: HINTS Truncated Mid-Word ⚠️ CRITICAL

**Symptom**: Hints on flashcard FRONT are cut off mid-word or incomplete

- Examples: "creating a re...", "aren't evenl...", "can we use a Has..."
- Hints don't make grammatical sense
- Key words are missing from hint questions

**Cause**: Hints in problem file's Flashcard Content section are too long (>50 chars)
**Impact**: **CRITICAL** - Flashcard is unusable for study, hints provide no guidance

**How to Identify**:

```bash
# Check for truncation indicators in hints
grep -A 5 "💡 HINTS:" flashcards/individual/*.md | grep "\.\.\."
```

**Fix Process**:

1. **Open problem file** and locate `## 🎴 Flashcard Content` section
2. **Measure hint length** - each hint should be ≤45 characters
3. **Rewrite hints** to be concise while preserving meaning:
   - Remove unnecessary words ("can you", "how do you")
   - Use abbreviations strategically ("chars" instead of "characters")
   - Focus on core question
   - Remove redundancy
4. **Update problem file** with shortened hints
5. **Regenerate flashcard**: `python3 scripts/generate_flashcard.py problems/.../LC-XXX.md`
6. **Re-verify** to confirm hints are now complete

**Example Fix**:

**Before** (67 chars - TOO LONG):

```
- How can you check for symmetry without creating a reversed string?
```

**After** (37 chars - PERFECT):

```
- Check symmetry without reversing?
```

**Before** (68 chars - TOO LONG):

```
- What if the non-alphanumeric characters aren't evenly distributed?
```

**After** (34 chars - PERFECT):

```
- What if special chars scattered?
```

**Before** (73 chars - TOO LONG):

```
- How do you prevent going out of bounds when skipping invalid characters?
```

**After** (39 chars - PERFECT):

```
- How to avoid bounds errors skipping?
```

**Quality Check After Fix**:

- [ ] All hints < 50 characters
- [ ] No mid-word truncation
- [ ] Hints make complete sense
- [ ] Key guidance preserved
- [ ] Grammatically correct

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

- ✅ **HINTS are complete sentences** (no mid-word truncation)
- ✅ **HINTS make grammatical sense** and guide thinking
- ✅ **HINTS are problem-specific** (not generic questions)
- ✅ KEY INSIGHT is unique to the problem (no generic text)
- ✅ ALGORITHM has 4-5 concrete, actionable steps
- ✅ All steps are specific to THIS problem's solution
- ✅ Complexity notations are accurate
- ✅ No truncation or overflow issues (especially in HINTS)
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

**HINTS Check** ⚠️:

- [ ] All hints present (2-3 from problem file)
- [ ] Complete sentences (no mid-word truncation)
- [ ] Grammatically correct
- [ ] Make sense when read aloud
- [ ] Problem-specific (not generic)
- [ ] Guide thinking without revealing solution
- Hints:
  1. "[Hint 1 text]" - [✅ Complete | ❌ Truncated at...]
  2. "[Hint 2 text]" - [✅ Complete | ❌ Truncated at...]
  3. "[Hint 3 text]" - [✅ Complete | ❌ Missing/Truncated]

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
