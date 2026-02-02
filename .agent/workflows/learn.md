---
description: Start learning a new coding problem with guided hints
---

# Start Problem Learning Workflow

## Purpose

Automatically analyze a problem file and provide structured learning guidance aligned with Rohit's learning preferences (hints and guidance, not complete solutions).

## Code Language Preference

**IMPORTANT:** All code examples, pseudocode, and implementation guidance MUST use Java syntax.

- ✅ Use Java-style syntax for all examples
- ✅ Use Java naming conventions (camelCase for variables/methods, PascalCase for classes)
- ✅ Use Java data structures (HashSet, HashMap, ArrayList, etc.)
- ❌ Never use Python syntax or Python-specific constructs
- If showing plain pseudocode, use Java-like syntax

## Workflow Steps

### 1. Smart Problem Selection

**CRITICAL: Intelligently suggest next problem based on learning progress**

- Analyze current pattern mastery from `tracking/revision-tracker.json`
- Identify knowledge gaps and recommend next learning targets
- Scan `problems/` directory for available problems
- Consider pattern distribution and difficulty progression
- Present 2-3 smart recommendations with clear rationale

**Smart Selection Logic:**
```
🧠 Analyzing Your Learning Profile...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CURRENT MASTERY:
  🟢 Strong: [List strong patterns] ([X] problems each)
  🟡 Learning: [List developing patterns] ([X] problems each)  
  🔴 Missing: [List unlearned patterns]

🎯 RECOMMENDED NEXT STEPS:
  
  1. 🔥 [Problem Name] ([Pattern]) - [Difficulty]
     💡 Why: [Builds on your Two Pointers strength + introduces Sliding Window]
     📂 File: problems/[pattern]/[filename].md
     ⏱️  Est. Time: 45-60 minutes
     
  2. 📚 [Problem Name] ([Pattern]) - [Difficulty]  
     💡 Why: [Foundation pattern - unlocks 15+ future problems]
     📂 File: problems/[pattern]/[filename].md
     ⏱️  Est. Time: 60-90 minutes
     
  3. ⚡ [Problem Name] ([Pattern]) - [Difficulty]
     💡 Why: [Quick win - similar to problems you've mastered]
     📂 File: problems/[pattern]/[filename].md
     ⏱️  Est. Time: 30-45 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤔 What interests you most?
  • Type '1', '2', or '3' to select a recommendation
  • Type 'random' for surprise selection
  • Type 'pattern:X' to focus on specific pattern
  • Or specify your own: 'problems/[path]/[file].md'
```

**Pattern Priority Algorithm:**
1. **Foundational First**: Prioritize patterns that unlock many other problems
2. **Progressive Difficulty**: Build from Easy → Medium → Hard within patterns
3. **Complementary Skills**: Suggest patterns that build on existing strengths
4. **Frequency-Based**: Focus on most commonly used interview patterns
5. **Recency Balance**: Avoid suggesting same pattern repeatedly

### 2. Problem File Analysis

**After user selects a problem:**

- Read the selected problem markdown file
- Extract key metadata:
  - Problem title and number
  - Jira ticket reference
  - LeetCode URL
  - Pattern category
  - Difficulty level
  - Current status
  - Problem description and examples

### 3. Problem Understanding & Clarification

**CRITICAL: Spend significant time here before jumping to solutions**

Break down the problem statement:

- **What are we given?** (Inputs, data types, constraints)
- **What are we asked to find?** (Output, return type, format)
- **What does the problem really mean?** (Rephrase in simpler terms)
- **What are the constraints?** (Size limits, value ranges, special conditions)
- **What assumptions can we make?** (Sorted? Unique? Non-empty?)
- **What assumptions should we NOT make?** (Common misconceptions)

Walk through examples step-by-step:

- **Trace Example 1:** What happens at each step?
- **Trace Example 2:** How does this differ from Example 1?
- **Create a mental model:** What's the relationship between input and output?
- **Identify transformations:** How does input become output?

Ask clarifying questions to deepen understanding:

- What if the input is empty?
- What if there's only one element?
- Can values repeat?
- Are there any special values to watch for?
- What's the expected behavior in edge cases?

### 4. Initial Intuitions & Observations

Before discussing any specific pattern or approach:

- What do you notice about the examples?
- What patterns or relationships do you see in the data?
- What's your gut feeling about how to approach this?
- What simpler problem does this remind you of?
- If you had to explain this to a friend, how would you describe it?

### 5. **PAUSE FOR USER ENGAGEMENT** 🛑

**CRITICAL: Stop here and wait for user response**

After presenting the problem understanding and initial intuition prompts, STOP and ask the user to share their thoughts:

- Ask them to think about how they would approach the problem
- Request they share any patterns they notice
- Ask if they want to see the core concepts or if they want to try thinking more first
- Only proceed to Core Concepts after the user explicitly responds

This creates active learning rather than passive reading.

### 6. Core Concepts Teaching

**ONLY show this section after user has shared their thoughts and wants to proceed**

Explain the fundamental concepts needed:

- What data structures are involved?
- What algorithms might be relevant?
- What mathematical concepts apply?
- What are the prerequisites?

### 7. Pattern Recognition Guidance

Help identify why this pattern applies:

- What clues in the problem statement point to this pattern?
- What are the characteristics of this pattern?
- When should this pattern be used vs. alternatives?
- What are common variations of this pattern?

### 8. Approach Analysis

Walk through different approaches:

- **Brute Force:** What's the obvious solution? What's its complexity?
- **Optimized Approaches:** What improvements can we make? Why?
- **Trade-offs:** Time vs. space complexity considerations
- **Pattern Application:** How does the identified pattern help?

### 9. Key Insights & Hints

Provide the "aha!" moments WITHOUT giving the solution:

- What's the key insight that unlocks this problem?
- What relationship between data elements should we notice?
- What property can we exploit?
- What's the clever trick or observation?

### 10. Implementation Guidance

Guide with questions and hints:

- What data structure should we use? Why?
- What should we track/store as we iterate?
- What are the loop conditions?
- What edge cases need special handling?
- Provide pseudocode structure, not complete code

### 11. Edge Cases Discussion

Help identify corner cases:

- Empty input
- Single element
- Duplicate values
- Negative numbers
- Maximum/minimum constraints
- Special values (zero, null, etc.)

### 12. Complexity Analysis

Teach how to analyze:

- Time complexity: What operations? How many times?
- Space complexity: What extra space? Why needed?
- Best/average/worst case scenarios
- Comparison with alternative approaches

## Teaching Principles

### DO:

- ✅ **FIRST:** Thoroughly explain what the problem is asking (spend significant time here)
- ✅ Break down the problem statement into simple, understandable parts
- ✅ Walk through examples step-by-step to build intuition
- ✅ Ask clarifying questions to guide thinking
- ✅ **PAUSE after Initial Intuitions and wait for user to engage**
- ✅ Ask user to share their thinking before showing core concepts
- ✅ Only reveal core concepts after user has attempted their own thinking
- ✅ Provide hints and nudges in the right direction
- ✅ Explain concepts and patterns thoroughly
- ✅ Use visual examples and walkthroughs
- ✅ Encourage independent problem-solving
- ✅ Validate the user's approach and thinking
- ✅ Point out when they're on the right track
- ✅ Suggest what to think about next

### DON'T:

- ❌ Jump directly to solutions or approaches without problem understanding
- ❌ Assume the user understands what the problem is asking
- ❌ **Show core concepts before user has thought about the problem**
- ❌ Skip the engagement pause - always wait for user response
- ❌ Give complete code solutions upfront
- ❌ Solve the problem for the user
- ❌ Provide answers without explanation
- ❌ Skip the learning process
- ❌ Just show the optimal solution
- ❌ Continue past Initial Intuitions without user confirmation

## Output Format

Structure the response as:

```
🎯 **Problem: [Title]**

📋 **Problem Details:**
- Pattern: [Pattern Name]
- Difficulty: [Easy/Medium/Hard]
- LeetCode: [URL]

---

## 📖 Understanding the Problem

### What are we given?
[Input types, data structures, initial conditions]

### What are we asked to find?
[Output type, expected result format]

### What does this problem really mean?
[Rephrase in simpler terms, explain the core task]

### Constraints & Assumptions
[Size limits, value ranges, special conditions]
[What we CAN assume vs. what we should NOT assume]

### Example Walkthrough
[Step-by-step trace of Example 1]
[Step-by-step trace of Example 2]
[Mental model of input → output transformation]

---

## 💭 Initial Intuitions

[Before discussing patterns or approaches]
- What do you notice in the examples?
- What relationships or patterns do you see?
- What simpler problem does this remind you of?
- How would you explain this to a friend?

---

## 🛑 YOUR TURN TO THINK

**Stop here! Before I show you the core concepts and solution approaches:**

1. **Take a moment** to think about how you might solve this
2. **Share your thoughts:** What approach would you try? What data structures come to mind?
3. **Ask yourself:** Have I seen anything similar? What patterns do I notice?

**Let me know when you're ready to see the core concepts, or if you want to discuss your ideas first!**

[STOP HERE - Wait for user response before showing Core Concepts]

---

## 🧠 Core Concepts
**[Only show this section after user has shared their thoughts]**

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
