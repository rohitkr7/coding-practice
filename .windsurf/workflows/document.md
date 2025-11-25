---
description: Document a completed solution with detailed explanations
---

# Document Solution Workflow

## Purpose
Help document a completed problem solution with comprehensive comments, explanations, and learning notes for future reference.

## Workflow Steps

### 1. Solution Review
- Review the user's implemented solution code
- Understand the approach they used
- Identify the pattern applied
- Note any unique insights or techniques

### 2. Code Enhancement
Improve the solution with:
- **Comprehensive comments:**
  - JavaDoc/docstring for methods
  - Inline comments explaining logic
  - Comments on why, not just what
- **Better variable naming** (if needed)
- **Code structure improvements** (if applicable)
- **Best practices** (interface over implementation, etc.)

### 3. Visual Walkthrough Creation
Create step-by-step visual explanation:
- Show initial state
- Trace through each iteration
- Display data structure states
- Show how variables change
- Highlight key decision points
- Verify final result

Use ASCII art, tables, or structured text for visualization.

### 4. Complexity Analysis Documentation
Provide detailed analysis:
- **Time Complexity:**
  - Break down each operation
  - Count iterations
  - Explain best/average/worst cases
  - Show the math: O(n), O(log n), etc.
- **Space Complexity:**
  - List all extra space used
  - Explain why it's needed
  - Consider recursion stack if applicable
- **Comparison Table:**
  - Compare with alternative approaches
  - Show trade-offs

### 5. Key Learnings Documentation
Capture learning insights:
- **What I Learned:**
  - Core concepts mastered
  - Pattern understanding
  - New techniques discovered
  - Complexity analysis insights
- **Mistakes Made:**
  - Initial wrong approaches
  - Bugs encountered
  - Misconceptions corrected
- **Pattern Insights:**
  - When to use this pattern
  - When NOT to use it
  - Related patterns
  - Pattern variations

### 6. Test Cases Documentation
Document comprehensive test cases:
- Basic examples from problem
- Edge cases (empty, single element, etc.)
- Boundary conditions
- Special values (negatives, zero, duplicates)
- Large inputs
- Each with explanation of what it tests

### 7. Similar Problems Reference
Link to related problems:
- Direct variations of the same problem
- Problems using the same pattern
- Problems with similar concepts
- Next difficulty level problems
- Categorize by: Easy/Medium/Hard

### 8. Quick Reference Card
Create a concise reference:
- Pattern name and key insight
- Template code structure
- Time/space complexity
- Key formulas or relationships
- When to use this approach
- Common pitfalls to avoid

### 9. Problem File Update
Update the markdown file with all sections:
- ✅ Status changed to "Completed"
- ✅ Updated timestamp
- ✅ All sections filled in
- ✅ Code with comments
- ✅ Visual explanation
- ✅ Complexity analysis
- ✅ Test cases
- ✅ Key learnings
- ✅ Similar problems
- ✅ Quick reference

### 10. Update README Problem Tracker
After documenting the solution, update the centralized problem tracker:
- Run the tracker update script: `./update_tracker.sh` or `python3 update_problem_tracker.py`
- This automatically scans all problem files and updates the README with current status
- The tracker shows:
  - Overall progress (X/Y problems completed)
  - Progress by pattern
  - Clickable links to each problem file
  - Difficulty badges and status icons
  - Links to LeetCode and Jira tickets

**Cascade Action:** Automatically run the update script after documenting a problem

## Documentation Template Structure

```markdown
## 💻 Implementation

### [Language] Solution (Optimized with Comments)

```[language]
[Well-commented code with JavaDoc/docstrings]
```

### Key Implementation Details:
[Explain important design decisions]

### Code Explanation
[Line-by-line or section-by-section breakdown]

---

## 🎨 Visual Explanation

### Example Walkthrough: [example]

```
[ASCII art showing step-by-step execution]
```

### Why This Works:
[Explain the intuition]

---

## 🧪 Test Cases

### Test Case 1: [Description]
```
Input: [input]
Expected Output: [output]
Actual Output: [output]
Status: ✅ Passed
Explanation: [why this test is important]
```

[More test cases...]

---

## 📊 Complexity Analysis

### Time Complexity: O(?)
**Breakdown:**
[Detailed explanation]

### Space Complexity: O(?)
**Breakdown:**
[Detailed explanation]

### Comparison with Other Approaches:
[Table comparing approaches]

---

## 🎓 Key Learnings

### What I Learned
[List of learnings]

### Mistakes I Made
[List of mistakes and lessons]

### Pattern Insights
[When to use, when not to use]

---

## 🔗 Similar Problems

[Categorized list of related problems]

---

## 🎯 Quick Reference Card

**Pattern:** [Pattern Name]
**Key Insight:** [One-liner insight]
**Time:** O(?) | **Space:** O(?)

**Template:**
```[language]
[Minimal template code]
```

**Remember:** [Key point to remember]
```

## Quality Checklist

Before completing, ensure:
- [ ] Code is well-commented and clear
- [ ] Visual walkthrough is easy to follow
- [ ] Complexity analysis is detailed and accurate
- [ ] All test cases have explanations
- [ ] Key learnings capture insights and mistakes
- [ ] Similar problems are categorized and relevant
- [ ] Quick reference is concise and useful
- [ ] All markdown sections are properly formatted
- [ ] Status is updated to "Completed"
- [ ] Timestamp is current

## Teaching Approach

- Explain WHY, not just WHAT
- Connect concepts to the bigger picture
- Highlight patterns that apply to other problems
- Make it easy to review and remember
- Create reference material for future use
