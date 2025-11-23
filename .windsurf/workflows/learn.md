---
description: Start learning a new coding problem with guided hints
---

# Start Problem Learning Workflow

## Purpose
Automatically analyze a problem file and provide structured learning guidance aligned with Rohit's learning preferences (hints and guidance, not complete solutions).

## Workflow Steps

### 1. Problem File Analysis
- Read the problem markdown file provided by the user
- Extract key metadata:
  - Problem title and number
  - Jira ticket reference
  - LeetCode URL
  - Pattern category
  - Difficulty level
  - Current status
  - Problem description and examples

### 2. Core Concepts Teaching
Explain the fundamental concepts needed:
- What data structures are involved?
- What algorithms might be relevant?
- What mathematical concepts apply?
- What are the prerequisites?

### 3. Pattern Recognition Guidance
Help identify why this pattern applies:
- What clues in the problem statement point to this pattern?
- What are the characteristics of this pattern?
- When should this pattern be used vs. alternatives?
- What are common variations of this pattern?

### 4. Approach Analysis
Walk through different approaches:
- **Brute Force:** What's the obvious solution? What's its complexity?
- **Optimized Approaches:** What improvements can we make? Why?
- **Trade-offs:** Time vs. space complexity considerations
- **Pattern Application:** How does the identified pattern help?

### 5. Key Insights & Hints
Provide the "aha!" moments WITHOUT giving the solution:
- What's the key insight that unlocks this problem?
- What relationship between data elements should we notice?
- What property can we exploit?
- What's the clever trick or observation?

### 6. Implementation Guidance
Guide with questions and hints:
- What data structure should we use? Why?
- What should we track/store as we iterate?
- What are the loop conditions?
- What edge cases need special handling?
- Provide pseudocode structure, not complete code

### 7. Edge Cases Discussion
Help identify corner cases:
- Empty input
- Single element
- Duplicate values
- Negative numbers
- Maximum/minimum constraints
- Special values (zero, null, etc.)

### 8. Complexity Analysis
Teach how to analyze:
- Time complexity: What operations? How many times?
- Space complexity: What extra space? Why needed?
- Best/average/worst case scenarios
- Comparison with alternative approaches

## Teaching Principles

### DO:
- ✅ Ask clarifying questions to guide thinking
- ✅ Provide hints and nudges in the right direction
- ✅ Explain concepts and patterns thoroughly
- ✅ Use visual examples and walkthroughs
- ✅ Encourage independent problem-solving
- ✅ Validate the user's approach and thinking
- ✅ Point out when they're on the right track
- ✅ Suggest what to think about next

### DON'T:
- ❌ Give complete code solutions upfront
- ❌ Solve the problem for the user
- ❌ Provide answers without explanation
- ❌ Skip the learning process
- ❌ Just show the optimal solution

## Output Format

Structure the response as:

```
🎯 **Problem: [Title]**

📋 **Problem Details:**
- Pattern: [Pattern Name]
- Difficulty: [Easy/Medium/Hard]
- LeetCode: [URL]

---

## 🧠 Core Concepts

[Explain fundamental concepts needed]

---

## 🔍 Pattern Recognition

[Explain why this pattern applies and what clues point to it]

---

## 💡 Approach Analysis

### Brute Force
[Explain obvious approach and complexity]

### Optimized Approach
[Guide toward better solution with hints]

---

## 🔑 Key Insights

[Provide the "aha!" moments as hints]

---

## 🛠️ Implementation Guidance

[Guide with questions and pseudocode structure]

---

## ⚠️ Edge Cases

[List edge cases to consider]

---

## 📊 Complexity Analysis

[Teach how to analyze time/space complexity]

---

## 🤔 Guided Questions

[Ask questions to help user think through the problem]
```

## Reference Materials

- 16 Coding Patterns: `/Users/rohit.roy/Documents/LnD/PATTERNS_GUIDE.md`
- Pattern Repository: https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews

## Success Criteria

- User understands the core concepts
- User can identify the pattern independently
- User can explain why the approach works
- User implements the solution themselves
- User can analyze complexity
- User recognizes when to apply this pattern to similar problems
