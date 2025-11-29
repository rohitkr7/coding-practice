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

**Actions**: Analyze the current problem file and provide a brief summary

### Step 2: Solution Overview
- What approach did you use?
- What was the key insight that cracked the problem?
- Were there any edge cases you missed initially?

**Actions**: Review the solution code and highlight:
- The main algorithm/pattern used
- Critical lines of code
- Any optimization opportunities

### Step 3: Pattern Recognition
- Which coding pattern(s) does this problem demonstrate?
- What are the telltale signs of this pattern?
- What similar problems use the same pattern?

**Actions**: 
- Identify the pattern from the 16 coding patterns
- List 2-3 similar problems from your repository
- Explain the pattern signature (how to recognize it)

### Step 4: Complexity Analysis
- Time complexity: Best, Average, Worst case
- Space complexity: What data structures were used?
- Could it be optimized further?

**Actions**: Provide Big-O analysis with explanation

### Step 5: Key Takeaways
- What did you learn from this problem?
- What would you do differently next time?
- How does this fit into the bigger picture?

**Actions**: Generate 3-5 bullet points of key learnings

### Step 6: Update Documentation
- Ensure problem file has all required sections
- Update Jira ticket if applicable
- Mark completion status

**Actions**: 
- Verify all documentation sections are complete
- Suggest any missing information
- Provide Jira update command if needed

---

## Example Usage

```
User: "/review" or "quick review this problem"

Response:
📋 **Quick Review: Two Sum**

**Problem**: LC-1 Two Sum (Easy)
**Pattern**: Hash Table / Array & Hashing
**Status**: Completed ✓

**Solution Overview**:
You used a HashMap approach to find two numbers that sum to target in O(n) time.
Key insight: For each number, check if its complement (target - num) exists.

**Pattern Recognition**:
This demonstrates the "Hash Table for Complement Lookup" pattern.
Signature: Need to find pairs that satisfy a condition with O(1) lookup.
Similar problems: Valid Anagram, Contains Duplicate, Group Anagrams

**Complexity**:
- Time: O(n) - single pass through array
- Space: O(n) - HashMap storage in worst case

**Key Takeaways**:
• HashMap enables O(1) complement lookup vs O(n²) nested loops
• Trade space for time: O(n) space for O(n) time improvement
• Check complement BEFORE adding to prevent same element reuse
• Always consider edge cases: empty array, duplicates, negatives

**Next Steps**:
✓ Documentation complete
✓ Pattern identified
→ Try similar problem: Two Sum II (sorted array, use two pointers)
```

---

## Integration with Slash Commands

This workflow is designed to work with the custom `/review` command.

**Alternative Triggers**:
- "review this solution"
- "what did I learn from this"
- "quick review mode"
- "analyze my solution"

---

## Tips for Effective Reviews

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

---

## Quick Review Template

```markdown
📋 **Quick Review: [Problem Name]**

**Problem**: [ID] - [Title] ([Difficulty])
**Pattern**: [Pattern Name]
**Status**: [Status Icon]

---

**Solution Overview**:
[1-2 sentences on approach and key insight]

---

**Pattern Recognition**:
- **Pattern**: [Name and description]
- **Signature**: [How to recognize this pattern]
- **Similar Problems**: [List 2-3 similar problems]

---

**Complexity**:
- **Time**: O(?) - [Brief explanation]
- **Space**: O(?) - [Brief explanation]

---

**Key Takeaways**:
• [Takeaway 1]
• [Takeaway 2]
• [Takeaway 3]
• [Takeaway 4]

---

**Next Steps**:
[Completion status and suggested next problems]
```
