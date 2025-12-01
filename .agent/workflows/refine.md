---
description: Refine solution with crisp inline comments and complexity annotations
---

# Refine Solution Workflow

## Purpose

Generate a well-documented, LeetCode-ready solution with compact inline comments, complexity annotations, and clear explanations—displayed in chat only, without modifying any files.

## Code Language Preference

**IMPORTANT:** All code examples and refinements MUST use Java syntax unless the user's original code is in a different language.

- ✅ Prefer Java-style syntax for all examples
- ✅ Use Java naming conventions (camelCase for variables/methods, PascalCase for classes)
- ✅ Use Java data structures (HashSet, HashMap, ArrayList, etc.)
- ✅ Include JavaDoc-style comments for methods
- ✅ If user's code is already in another language, maintain that language but follow its best practices
- If showing plain pseudocode, use Java-like syntax

## Key Differences from /document

- **Refine:** Code-focused, inline comments only, shown in chat
- **Document:** Full documentation, updates files, generates flashcards

## Workflow Steps

### 1. Read Current Solution

- Read the problem file provided by the user
- Extract the existing solution code
- Identify the approach and pattern used
- Note the language used (Python, Java, JavaScript, etc.)

### 2. Analyze Code Structure

- Identify key sections: initialization, main logic, edge cases
- Locate loops, conditionals, data structure operations
- Find the core algorithm or pattern implementation
- Note any helper functions or methods

### 3. Generate Refined Solution

Create a polished version with:

#### **Inline Comments (Compact & Crisp):**

- ✅ One-line comments for each logical block
- ✅ Explain the "why," not just the "what"
- ✅ Use 3-5 word phrases when possible
- ✅ Place comments above the code they describe
- ❌ No verbose paragraphs
- ❌ No obvious comments ("initialize variable")

#### **Function/Method Documentation:**

- Add concise docstring/JavaDoc at function level
- Include: purpose, params, return value, time/space complexity
- Keep it under 5 lines

#### **Complexity Annotations:**

- Add time complexity as a comment at function start
- Add space complexity as a comment at function start
- Optional: Add inline complexity notes for specific operations (e.g., "O(n) iteration")

#### **Section Headers (if needed):**

- Use comments to mark major sections
- Examples: "# Step 1: Build frequency map", "// Edge case handling"

### 4. Format Rules

Follow these formatting guidelines:

**Python:**

```python
def function_name(params):
    """
    Brief description.
    Time: O(n), Space: O(1)
    """
    # Step 1: Initialize pointers
    left, right = 0, len(arr) - 1

    # Step 2: Two-pointer convergence
    while left < right:
        # Process current pair
        ...
```

**Java:**

```java
/**
 * Brief description.
 * Time: O(n), Space: O(1)
 */
public int function(int[] nums) {
    // Step 1: Initialize HashMap for frequencies
    Map<Integer, Integer> freq = new HashMap<>();

    // Step 2: Count occurrences - O(n)
    for (int num : nums) {
        freq.put(num, freq.getOrDefault(num, 0) + 1);
    }
    ...
}
```

**JavaScript:**

```javascript
/**
 * Brief description.
 * Time: O(n), Space: O(1)
 */
function functionName(arr) {
    // Step 1: Create result array
    const result = new Array(arr.length);

    // Step 2: Forward pass - accumulate products
    let product = 1;
    for (let i = 0; i < arr.length; i++) {
        result[i] = product;
        product *= arr[i];  // Update running product
    }
    ...
}
```

### 5. Comment Quality Guidelines

**✅ GOOD Comments (Crisp & Informative):**

- `// Build prefix products - O(n)`
- `# Two pointers converge from edges`
- `// HashMap stores char → last index`
- `# Early exit if array is empty`
- `// Sliding window: expand right, contract left`

**❌ BAD Comments (Verbose or Obvious):**

- `// This loop iterates through the array` ← Obvious!
- `# We are using a variable called count to count things` ← Too verbose!
- `// Increment i` ← States the obvious!
- `# This is the main algorithm` ← Not informative!

### 6. Complexity Annotation Best Practices

**Include:**

- Overall function complexity in docstring
- Complexity for non-obvious operations
- Space complexity for data structures created

**Example:**

```python
def topKFrequent(nums, k):
    """
    Find k most frequent elements.
    Time: O(n), Space: O(n)
    """
    # Count frequencies - O(n) time, O(n) space
    freq = Counter(nums)

    # Bucket sort by frequency - O(n)
    buckets = [[] for _ in range(len(nums) + 1)]

    # Collect top k elements - O(n)
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
```

### 7. Output Format Structure

Present the refined solution in the chat as:

````markdown
## 🎯 Refined Solution: [Problem Name]

### 📝 Overview

- **Pattern:** [Pattern Name]
- **Approach:** [Brief description of approach]
- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

### 💻 Refined Code

```[language]
[Fully refined code with inline comments and complexity annotations]
```
````

---

### 🔑 Key Comment Highlights

1. **[Comment topic 1]:** [Explanation]
2. **[Comment topic 2]:** [Explanation]
3. **[Comment topic 3]:** [Explanation]

---

### 📊 Complexity Breakdown

**Time Complexity: O(?)**

- [Operation 1]: O(?)
- [Operation 2]: O(?)
- Overall: O(?)

**Space Complexity: O(?)**

- [Data structure 1]: O(?)
- [Data structure 2]: O(?)
- Overall: O(?)

---

### ✨ What's Been Improved

- ✅ [Improvement 1]
- ✅ [Improvement 2]
- ✅ [Improvement 3]
- ✅ Added complexity annotations
- ✅ Crisp inline comments throughout

---

**Note:** This refined solution is shown in chat only. Would you like me to update the problem file with this refined code?

```

## Principles

### DO:
- ✅ Keep comments short and crisp (3-10 words)
- ✅ Explain the "why" and "what's happening"
- ✅ Add complexity annotations strategically
- ✅ Use consistent comment style for the language
- ✅ Mark logical sections clearly
- ✅ Show the entire refined code in chat
- ✅ Make it ready to copy-paste to LeetCode

### DON'T:
- ❌ Write verbose paragraph comments
- ❌ State the obvious ("increment variable")
- ❌ Modify any files (show in chat only)
- ❌ Change the actual algorithm or logic
- ❌ Add unnecessary complexity annotations everywhere
- ❌ Use different comment styles in same code
- ❌ Assume user wants file updates

## Success Criteria

- User receives clean, well-commented code in chat
- Comments are compact, crisp, and informative
- Complexity annotations are accurate and helpful
- Code is ready to submit to LeetCode
- No files are modified unless explicitly requested
- Solution is easy to understand and reference later
```
