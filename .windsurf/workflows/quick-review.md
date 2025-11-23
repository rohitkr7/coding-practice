---
description: Quick review of problem solution and patterns
---

# Quick Review Workflow

**Purpose**: Quickly review a problem's solution, patterns used, and key takeaways

**Trigger**: Use `/review` command or say "quick review" or "review this problem"

**When to Use**:
- After solving a problem to reinforce learning
- Before similar problem attempts
- During weekly review sessions
- When you need a quick refresher

---

## Workflow Steps

### Step 1: Identify the Problem
- Extract problem title and difficulty
- Confirm the problem category (which of the 16 patterns)
- Note if this is a first attempt or revisit

**Cascade Action**: Analyze the current problem file and provide a brief summary

### Step 2: Solution Overview
- What approach did you use?
- What was the key insight that cracked the problem?
- Were there any edge cases you missed initially?

**Cascade Action**: Review the solution code and highlight:
- The main algorithm/pattern used
- Critical lines of code
- Any optimization opportunities

### Step 3: Pattern Recognition
- Which coding pattern(s) does this problem demonstrate?
- What are the telltale signs of this pattern?
- What similar problems use the same pattern?

**Cascade Action**: 
- Identify the pattern from the 16 coding patterns
- List 2-3 similar problems from your repository
- Explain the pattern signature (how to recognize it)

### Step 4: Complexity Analysis
- Time complexity: Best, Average, Worst case
- Space complexity: What data structures were used?
- Could it be optimized further?

**Cascade Action**: Provide Big-O analysis with explanation

### Step 5: Key Takeaways
- What did you learn from this problem?
- What would you do differently next time?
- How does this fit into the bigger picture?

**Cascade Action**: Generate 3-5 bullet points of key learnings

### Step 6: Update Documentation
- Ensure problem file has all required sections
- Update Jira ticket if applicable
- Mark completion status

**Cascade Action**: 
- Verify all documentation sections are complete
- Suggest any missing information
- Provide Jira update command if needed

---

## Example Usage

```
User: "/review" or "quick review this problem"

Cascade Response:
📋 **Quick Review: Two Sum**

**Problem**: LND-30-2 Contains Duplicate (Easy)
**Pattern**: Two Pointers / Hash Table
**Status**: Completed ✓

**Solution Overview**:
You used a HashSet approach to detect duplicates in O(n) time.
Key insight: A duplicate exists if we've seen the number before.

**Pattern Recognition**:
This demonstrates the "Hash Table for Fast Lookup" pattern.
Signature: Need to track seen elements for O(1) lookup.
Similar problems: Valid Anagram, Two Sum, Group Anagrams

**Complexity**:
- Time: O(n) - single pass through array
- Space: O(n) - HashSet storage in worst case

**Key Takeaways**:
• HashSet is perfect for "have we seen this?" questions
• Trade space for time: O(n) space for O(n) time vs O(1) space for O(n²)
• Always consider edge cases: empty array, single element

**Next Steps**:
✓ Documentation complete
✓ Pattern identified
→ Try similar problem: LND-XX Valid Anagram
```

---

## Integration with Slash Commands

This workflow is designed to work with the custom `/review` command defined in `.windsurf/cascadeCustomCommands.json`.

**Alternative Triggers**:
- "review this solution"
- "what did I learn from this"
- "quick review mode"
- "analyze my solution"

---

## Tips for Cascade

When executing this workflow:
1. **Be Concise**: Keep review under 2 minutes of reading
2. **Be Specific**: Reference actual code and line numbers
3. **Be Encouraging**: Celebrate progress and growth
4. **Be Forward-Looking**: Suggest next problems to try
5. **Check Context**: Make sure you're looking at the right problem file

---

## Customization

You can customize this workflow by:
- Adding more pattern-specific questions
- Including comparison with optimal solutions
- Generating flashcard-style Q&A
- Creating a progress tracking update
- Suggesting related reading materials
