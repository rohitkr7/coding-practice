---
description: Fetch and populate missing problem details from LeetCode/NeetCode
---

# Enrich Problem Statement Workflow

## Purpose

Automatically check if a problem file has incomplete or vague problem statements, and if so, fetch the complete details from the source URL (LeetCode, NeetCode, etc.) and populate the problem file with accurate information.

## When to Use

- 📄 Problem file only has a URL reference but no actual problem description
- ❓ Problem statement section is vague or says "Visit the URL for details"
- 🔄 Need to refresh/update problem details from the source
- ✅ Want to ensure all problems have consistent, complete information
- 🆕 Just created a problem file from a template and need to fill it in

## What This Workflow Does

✅ **DOES:**

- Checks if problem statement is missing or incomplete
- Fetches problem details from LeetCode/NeetCode URLs
- Extracts: problem description, examples, constraints, difficulty
- Populates the problem file with complete, formatted information
- Preserves any existing work (solutions, notes, etc.)
- Updates metadata (difficulty, LeetCode number, etc.)

❌ **DOES NOT:**

- Provide solutions or hints
- Modify existing solution code
- Change pattern assignments
- Overwrite completed sections

## Workflow Steps

### 1. Identify Problem File

First, identify which problem file to enrich:

- User may provide a file path
- User may mention a problem name or number
- User may have the file already open

### 2. Check Current Problem File Content

Read the problem file and check:

**Missing Required Sections:**

```markdown
## 📝 Problem Statement

[Write or paste the problem statement here] ← VAGUE - needs enrichment
```

**Vague Descriptions:**

```markdown
Problem Description:
Solve the Valid Palindrome coding problem according to the LeetCode description.
Visit the problem URL for the complete description and examples. ← VAGUE
```

**Incomplete Examples:**

```markdown
**Example 1:**
Input:
Output:
Explanation: ← EMPTY - needs enrichment
```

**Missing Constraints:**

```markdown
**Constraints:**

-               ← EMPTY - needs enrichment
```

### 3. Extract Problem URL

Find the URL in the problem file:

**Check these fields:**

```markdown
**LeetCode:** https://leetcode.com/problems/valid-palindrome
Problem URL: https://leetcode.com/problems/valid-palindrome
**NeetCode:** https://neetcode.io/problems/is-palindrome
```

**Supported URLs:**

- LeetCode: `https://leetcode.com/problems/*`
- NeetCode: `https://neetcode.io/problems/*`
- Others as needed

### 4. Fetch Problem Details from URL

Use `read_url_content` tool to fetch the problem page.

**Extract the following information:**

1. **Problem Title** (exact name)
2. **Problem Number** (e.g., LC-125)
3. **Problem Description** (the full statement)
4. **Examples** (all provided examples with input/output/explanation)
5. **Constraints** (all constraint bullets)
6. **Difficulty** (Easy/Medium/Hard)

### 5. Format the Problem Statement

Create a properly formatted problem statement section:

```markdown
## 📝 Problem Statement

[Full problem description goes here - in plain text, well-formatted]

**Example 1:**
```

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**
```

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**
```

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.
```

### 6. Update Problem File

**Update these sections ONLY if they are empty/vague:**

1. **Problem Statement Section** - Replace vague text with full details
2. **Examples** - Add all examples with proper formatting
3. **Constraints** - Add all constraint bullets
4. **Difficulty** - Update if incorrect
5. **Title** - Update with exact LeetCode title if different

**PRESERVE these sections (never overwrite):**

- Any existing solution code
- Test cases you've written
- Personal notes and learnings
- Complexity analysis you've done
- Any checkboxes you've checked

### 7. Verify LeetCode Number

Extract the LeetCode number from the URL and ensure the filename is correct:

```
URL: https://leetcode.com/problems/valid-palindrome
LeetCode #: 125
Expected filename: LC-125-valid-palindrome.md
```

If filename doesn't match, notify the user.

### 8. Update Problem Metadata

Update the header metadata if present:

```markdown
# 9 - Valid Palindrome ← Problem number in tracker

**LeetCode #:** 125 ← Add this if missing
**LeetCode:** https://leetcode.com/problems/valid-palindrome
**Difficulty:** Easy ← Update if wrong
**Pattern:** Two Pointers
```

### 9. Confirm Changes

Show the user:

- What sections were updated
- What information was added
- Any sections that were preserved
- If filename needs changing

## Output Format

After enriching, provide a summary:

```markdown
# ✅ Problem Statement Enriched!

## 📋 Updates Made:

### Problem: Valid Palindrome (LC-125)

**Added:**
✅ Full problem description (previously vague)
✅ 3 examples with input/output/explanation
✅ 2 constraint bullets
✅ LeetCode number: 125

**Preserved:**
📌 Existing pattern assignment (Two Pointers)
📌 Jira ticket reference
📌 File structure and checklist

**File Updated:** `problems/two-pointers/LC-125-valid-palindrome.md`

---

**Next Steps:**

- Problem statement is now complete!
- You can use `/explain` to understand the problem
- Use `/learn` to start solving with hints
- The file is ready for you to add your solution
```

## Example Transformation

**Before (Vague):**

```markdown
## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/valid-palindrome
Problem Description:
Solve the Valid Palindrome coding problem according to the LeetCode description.
Visit the problem URL for the complete description and examples.
Difficulty: Easy
Category: Two Pointers
```

**After (Enriched):**

```markdown
## 📝 Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**
```

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**
```

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**
```

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.
```

## Edge Cases to Handle

### 1. URL Not Found

```
❌ No URL found in problem file
→ Ask user to provide the LeetCode/NeetCode URL
```

### 2. URL Fetch Fails

```
❌ Could not fetch content from URL
→ Check if URL is valid
→ Try alternative methods
→ Ask user to provide problem details manually
```

### 3. Problem Already Complete

```
✅ Problem statement section is already complete
→ Ask: "Problem details look complete. Do you want to refresh them?"
```

### 4. File Has Solution Code

```
✅ File has existing solution code
→ Preserve all solution sections
→ Only update problem statement area
```

### 5. Multiple URLs Present

```
⚠️ Found both LeetCode and NeetCode URLs
→ Ask which one to use as primary source
→ Default to LeetCode if both present
```

## Success Criteria

After running this workflow:

✅ Problem statement is complete and accurate  
✅ All examples are present with input/output/explanation  
✅ All constraints are listed  
✅ Difficulty matches the source  
✅ LeetCode number is identified  
✅ No existing work is lost or overwritten  
✅ File follows the standard template format

## Important Notes

**DO:**

- Fetch from the official source (LeetCode/NeetCode)
- Preserve all existing user work
- Format examples consistently with backticks
- Include ALL examples and constraints
- Update metadata accurately
- Use proper markdown formatting

**DON'T:**

- Overwrite existing solution code
- Change pattern assignments without confirmation
- Remove user notes or learnings
- Modify test cases user has written
- Change file structure dramatically
- Add solution hints (this workflow is for problem statement only)

## Integration with Other Workflows

This workflow pairs well with:

- `/explain` - After enriching, explain the complete problem
- `/learn` - After enriching, start learning with hints
- `/jira` - Enrich problems fetched from Jira board
- Run this automatically when creating new problems

## Batch Processing

Can also enrich multiple problems:

```
Find all problems with vague statements:
→ Search for "Visit the problem URL" or "[Write or paste"
→ Batch enrich all at once
→ Report which ones succeeded/failed
```
