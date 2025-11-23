---
description: Guide to workflows and slash commands
---

# Cascade Custom Workflows with Slash Commands

## Overview

This guide explains how Cascade workflows integrate with custom slash commands to create powerful, automated learning experiences.

## What Are Workflows?

Workflows are structured markdown files that define multi-step processes for Cascade to follow. They provide:
- **Consistency**: Same approach every time
- **Completeness**: Never miss important steps
- **Guidance**: Clear instructions for Cascade
- **Flexibility**: Easy to customize and extend

## How Slash Commands Trigger Workflows

### Option 1: Direct Reference (Explicit)
```
User: "/review"
Cascade: [Follows the quick-review.md workflow automatically]
```

### Option 2: Natural Language (Implicit)
```
User: "quick review this problem"
Cascade: [Recognizes intent and follows quick-review.md workflow]
```

### Option 3: Explicit Workflow Reference
```
User: "@contains-duplicate.md Let's use the quick-review workflow"
Cascade: [Applies workflow to specific file]
```

## Workflow ↔ Command Mapping

| Slash Command | Workflow File | Purpose |
|--------------|---------------|---------|
| `/learn` | `start-problem-learning.md` | Start learning new problem |
| `/document` | `document-solution.md` | Document completed solution |
| `/review` | `quick-review.md` | Quick solution review |
| `/hint` | *(command-only)* | Get targeted hint |
| `/pattern` | *(command-only)* | Identify pattern |
| `/complexity` | *(command-only)* | Analyze complexity |
| `/test` | *(command-only)* | Generate test cases |
| `/similar` | *(command-only)* | Find similar problems |

## Sample Workflow: Quick Review

The `quick-review.md` workflow demonstrates:

### ✅ **What It Does**
1. Analyzes the problem and solution
2. Identifies patterns used
3. Performs complexity analysis
4. Extracts key learnings
5. Suggests next steps

### 📋 **How to Use It**

**Method 1: Slash Command**
```
# Open a problem file, then:
/review
```

**Method 2: Natural Language**
```
quick review this problem
review my solution
let's review what I learned
```

**Method 3: Explicit Reference**
```
@LND-30-2-contains-duplicate.md Use the quick-review workflow
```

### 🎯 **Expected Output**

```markdown
📋 **Quick Review: Contains Duplicate**

**Problem**: LND-30-2 (Easy)
**Pattern**: Hash Table for Fast Lookup
**Status**: Completed ✓

**Solution Overview**:
You used a HashSet to track seen numbers. The key insight
was that duplicates mean we've encountered the number before.

**Pattern Recognition**:
Pattern: "Hash Table for Fast Lookup"
- Signature: Need O(1) lookup for previously seen items
- When to use: "Have we seen this before?" questions
- Similar: Two Sum, Valid Anagram, Group Anagrams

**Complexity**:
- Time: O(n) - single pass through array
- Space: O(n) - HashSet storage worst case
- Trade-off: Space for speed

**Key Takeaways**:
• Hash structures perfect for "existence" checks
• Always consider space vs time trade-offs
• Edge cases: empty array, single element

**Next Steps**:
→ Try: Valid Anagram (similar hash pattern)
→ Practice: Two Sum (hash + lookup)
```

## Creating Your Own Workflows

### Step 1: Create Workflow File

Create a markdown file in `.windsurf/workflows/`:

```bash
touch .windsurf/workflows/my-custom-workflow.md
```

### Step 2: Define Workflow Structure

```markdown
# My Custom Workflow Name

**Purpose**: Clear one-sentence purpose

**Trigger**: Commands that trigger this workflow

**When to Use**: Scenarios for using this workflow

---

## Workflow Steps

### Step 1: [Step Name]
- What to identify or analyze
- Questions to answer
- Context to gather

**Cascade Action**: Specific instructions for Cascade

### Step 2: [Next Step]
...

---

## Example Usage
[Show expected input/output]

---

## Tips for Cascade
[Guidance for how Cascade should execute]
```

### Step 3: Link to Slash Command (Optional)

Add or update command in `.windsurf/cascadeCustomCommands.json`:

```json
{
  "name": "mycommand",
  "description": "Brief description",
  "prompt": "Reference the my-custom-workflow.md workflow and..."
}
```

### Step 4: Test the Workflow

```
User: "/mycommand" or "use my custom workflow"
```

## Workflow Templates

### Template 1: Analysis Workflow
```markdown
# Problem Analysis Workflow

### Step 1: Problem Understanding
- Read problem statement
- Identify inputs/outputs
- List constraints

**Cascade Action**: Summarize problem in 2-3 sentences

### Step 2: Pattern Recognition
...
```

### Template 2: Implementation Workflow
```markdown
# Implementation Guidance Workflow

### Step 1: Design Phase
- Outline approach
- Identify data structures
- Plan edge cases

**Cascade Action**: Validate approach without providing code
...
```

### Template 3: Documentation Workflow
```markdown
# Solution Documentation Workflow

### Step 1: Code Review
- Check solution correctness
- Verify edge cases
- Optimize if needed

**Cascade Action**: Review code and suggest improvements
...
```

## Advanced: Workflow Chaining

You can chain multiple workflows together:

```
User: "Let's start with /learn, then when done, use /document"

Cascade:
1. Executes start-problem-learning.md workflow
2. Waits for completion signal
3. Executes document-solution.md workflow
```

## Best Practices

### ✅ DO:
- **Be Specific**: Give clear instructions for each step
- **Add Context**: Explain why each step matters
- **Include Examples**: Show expected outputs
- **Stay Focused**: One workflow = one purpose
- **Document Triggers**: List all ways to invoke

### ❌ DON'T:
- **Be Vague**: "Do something useful" is not helpful
- **Overload**: Too many steps = confusing workflow
- **Duplicate**: If command exists, use it instead
- **Forget Edge Cases**: Consider all scenarios

## Troubleshooting

### Workflow Not Triggering?
- Check file is in `.windsurf/workflows/`
- Verify markdown formatting
- Try explicit reference: `@workflow-file.md`

### Cascade Not Following Steps?
- Make instructions more specific
- Add "Cascade Action" headers
- Include example outputs
- Break complex steps into smaller ones

### Command vs Workflow Confusion?
- **Commands**: Quick, single-purpose actions
- **Workflows**: Multi-step, structured processes
- Use commands for atomic actions
- Use workflows for complex procedures

## Examples from Your Setup

### Example 1: Learning New Problem
```
User opens: LND-45-merge-intervals.md

User: "/learn"

Cascade follows: start-problem-learning.md
→ Identifies pattern (Merge Intervals)
→ Provides core concepts
→ Gives progressive hints
→ Guides toward solution
```

### Example 2: Documenting Solution
```
User has completed: LND-30-contains-duplicate.md

User: "/document"

Cascade follows: document-solution.md
→ Adds comprehensive comments
→ Creates visual walkthrough
→ Analyzes complexity
→ Documents learnings
→ Updates Jira ticket
```

### Example 3: Quick Review
```
User: "/review" on LND-30-contains-duplicate.md

Cascade follows: quick-review.md
→ Summarizes problem & solution
→ Identifies pattern
→ Analyzes complexity
→ Lists key takeaways
→ Suggests next problems
```

## Integration with Your Learning System

Your workflows integrate with:
- **16 Coding Patterns**: Pattern recognition in workflows
- **Jira Board**: Automatic ticket updates
- **Problem Repository**: Organized by pattern
- **Learning Preferences**: Hints, not solutions

## Quick Reference

| Want to... | Use... | File... |
|-----------|--------|---------|
| Start new problem | `/learn` | `start-problem-learning.md` |
| Get a hint | `/hint` | *(command only)* |
| Identify pattern | `/pattern` | *(command only)* |
| Document solution | `/document` | `document-solution.md` |
| Quick review | `/review` | `quick-review.md` |
| Create custom | - | Template above |

## Next Steps

1. ✅ **Try the sample workflow**: Use `/review` on any completed problem
2. 📝 **Create your own**: Use templates above
3. 🔄 **Iterate**: Refine based on what works
4. 📚 **Share**: Document successful patterns

---

**Pro Tip**: Workflows are living documents. Update them as you discover better approaches!
