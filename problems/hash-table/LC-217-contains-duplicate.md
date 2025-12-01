# 2 - Contains Duplicate

**Jira Ticket:** [LND-30](https://rohitroy007.atlassian.net/browse/LND-30)  
**LeetCode:** https://leetcode.com/problems/contains-duplicate  
**Pattern:** Hash Table / Array & Hashing
**Difficulty:** Easy  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Easy  
**Created:** 2025-08-21  
**Last Updated:** 2025-09-09

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/contains-duplicate
Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
Difficulty: Medium
Category: Array

---

## 🤔 Initial Thoughts

### Understanding the Problem
- **Goal**: Determine if any value appears at least twice in the array
- **Input**: An integer array `nums`
- **Output**: Boolean - `true` if duplicate exists, `false` if all elements are distinct
- **Edge Cases**: 
  - Single element array (no duplicate possible)
  - All unique elements
  - All same elements
  - Duplicate at start/middle/end
  - Negative numbers
  - Large numbers (±10^9)

### Pattern Recognition
**Why Hash Set? (Optimal Pattern)**
- Need to check "have we seen this element before?"
- Hash Set provides O(1) lookup for membership testing
- Order doesn't matter for detecting duplicates
- Single pass through array is sufficient

**Alternative: Two Pointers?**
- After sorting, duplicates become adjacent
- Can use two pointers to scan neighbors
- Trade-off: O(n log n) time but O(1) space

---

## 💡 Approach

### Approach 1: Brute Force ❌ (Not Recommended)
**Idea:**
- Compare every element with every other element
- Use nested loops to check all pairs

**Algorithm:**
```
For each element at index i:
    For each element at index j (where j > i):
        If nums[i] == nums[j]:
            Return true
Return false
```

**Time Complexity:** O(n²) - Too slow for n = 10^5  
**Space Complexity:** O(1)

---

### Approach 2: Sorting + Two Pointers ⚡
**Idea:**
- Sort the array first
- In sorted array, duplicates must be adjacent
- Scan with adjacent pointers checking neighbors

**Algorithm Steps:**
1. Sort the array
2. Iterate from index 0 to length-2
3. Compare nums[i] with nums[i+1]
4. If equal, return true
5. If loop completes, return false

**Time Complexity:** O(n log n) - dominated by sorting  
**Space Complexity:** O(1) or O(n) depending on sort implementation

---

### Approach 3: Hash Set ✅ (Optimal - Used)
**Idea:**
- Use a HashSet to track elements we've seen
- For each element, check if it's already in the set
- If yes → duplicate found, return true
- If no → add to set and continue
- If loop completes → no duplicates, return false

**Algorithm Steps:**
1. Create empty HashSet called `seen`
2. For each number in array:
   - Check if number exists in `seen`
   - If yes: return true (duplicate found)
   - If no: add number to `seen`
3. Return false (no duplicates found)

**Time Complexity:** O(n) - single pass through array  
**Space Complexity:** O(n) - worst case, store all unique elements

---

## 🎨 Visual Explanation

### Example 1: `nums = [1, 2, 3, 1]` (Duplicate Found)

```
Initial State:
nums = [1, 2, 3, 1]
seen = {}
result = ?

─────────────────────────────────────────
Iteration 1: num = 1
  ❓ Is 1 in seen? NO
  ➕ Add 1 to seen
  
  nums = [1̲, 2, 3, 1]
  seen = {1}

─────────────────────────────────────────
Iteration 2: num = 2
  ❓ Is 2 in seen? NO
  ➕ Add 2 to seen
  
  nums = [1, 2̲, 3, 1]
  seen = {1, 2}

─────────────────────────────────────────
Iteration 3: num = 3
  ❓ Is 3 in seen? NO
  ➕ Add 3 to seen
  
  nums = [1, 2, 3̲, 1]
  seen = {1, 2, 3}

─────────────────────────────────────────
Iteration 4: num = 1
  ❓ Is 1 in seen? YES! ✅
  🎯 DUPLICATE FOUND!
  
  nums = [1, 2, 3, 1̲]
  seen = {1, 2, 3}
  
  ➡️ RETURN true
```

---

### Example 2: `nums = [1, 2, 3, 4]` (No Duplicate)

```
Initial State:
nums = [1, 2, 3, 4]
seen = {}

─────────────────────────────────────────
Iteration 1: num = 1
  ❓ Is 1 in seen? NO
  ➕ Add 1 to seen
  seen = {1}

Iteration 2: num = 2
  ❓ Is 2 in seen? NO
  ➕ Add 2 to seen
  seen = {1, 2}

Iteration 3: num = 3
  ❓ Is 3 in seen? NO
  ➕ Add 3 to seen
  seen = {1, 2, 3}

Iteration 4: num = 4
  ❓ Is 4 in seen? NO
  ➕ Add 4 to seen
  seen = {1, 2, 3, 4}

─────────────────────────────────────────
✅ Loop completed without finding duplicates
➡️ RETURN false
```

---

### Why This Works:

**Key Insight:** A HashSet only stores unique elements. If we try to check for an element that's already in the set, we've found our duplicate!

**Efficiency:** We can stop as soon as we find the first duplicate - no need to check remaining elements.

---

## 💻 Implementation

### Java Solution (Hash Set - Optimal)

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Checks if the array contains any duplicate elements.
     * 
     * Approach: Use a HashSet to track seen elements.
     * - HashSet provides O(1) average-case lookup and insertion
     * - For each element, check if it's already in the set
     * - If found, we have a duplicate; if not, add it to the set
     * 
     * @param nums The input integer array
     * @return true if any value appears at least twice, false otherwise
     * 
     * Time Complexity: O(n) where n is the length of nums
     * Space Complexity: O(n) worst case when all elements are unique
     */
    public boolean containsDuplicate(int[] nums) {
        // Create a HashSet to store elements we've encountered
        // Using Set interface for flexibility (can swap implementations)
        Set<Integer> seen = new HashSet<>();
        
        // Iterate through each number in the array
        for (int num : nums) {
            // Check if this number has been seen before
            // contains() is O(1) average case for HashSet
            if (seen.contains(num)) {
                // Duplicate found! Return immediately
                return true;
            }
            
            // First time seeing this number, add it to our set
            // add() is also O(1) average case for HashSet
            seen.add(num);
        }
        
        // Checked all elements without finding duplicates
        return false;
    }
}
```

---

### Alternative Solution: Two Pointers (Sorting)

```java
import java.util.Arrays;

class Solution {
    /**
     * Alternative approach using sorting and two pointers.
     * 
     * @param nums The input integer array
     * @return true if any value appears at least twice, false otherwise
     * 
     * Time Complexity: O(n log n) due to sorting
     * Space Complexity: O(1) if sort is in-place, O(n) otherwise
     */
    public boolean containsDuplicate(int[] nums) {
        // Sort the array - duplicates will be adjacent
        Arrays.sort(nums);
        
        // Check adjacent elements
        // Loop to length-1 to avoid index out of bounds
        for (int i = 0; i < nums.length - 1; i++) {
            // If current element equals next element, we found a duplicate
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        
        // No adjacent duplicates found
        return false;
    }
}
```

---

### Key Implementation Details:

**Hash Set Approach (Your Solution):**
1. **Data Structure Choice**: `HashSet<Integer>` perfect for membership testing
2. **Early Return**: Exit as soon as duplicate found (optimization)
3. **Interface Usage**: `Set<Integer>` interface allows flexibility
4. **Auto-boxing**: Java automatically boxes `int` to `Integer` for the set

**Why HashSet over ArrayList?**
- `contains()` on HashSet: O(1) average case
- `contains()` on ArrayList: O(n) linear search
- For this problem, HashSet is significantly faster!

**Two Pointers Approach:**
1. **Sorting First**: Transforms problem - duplicates become neighbors
2. **Index Safety**: Loop to `length - 1` to safely access `i + 1`
3. **In-place**: Modifies original array (side effect to consider)

---

### Code Explanation (Your Solution)

**Line-by-line breakdown:**

```java
Set<Integer> seen = new HashSet<>();
```
- Creates empty HashSet to track encountered numbers
- O(1) insertion and lookup on average

```java
for (int num : nums) {
```
- Enhanced for-loop iterates through each element
- Cleaner syntax than index-based loop

```java
if (seen.contains(num)) {
    return true;
}
```
- Check if current number already exists in set
- If yes, we found a duplicate - return immediately
- Early return optimization (don't process remaining elements)

```java
seen.add(num);
```
- First time seeing this number, add to set
- Ensures we can detect it if it appears again

```java
return false;
```
- Reached end of array without finding duplicates
- All elements are unique

---

## 🧪 Test Cases

### Test Case 1: Basic Example - Duplicate Found
```java
Input: nums = [1, 2, 3, 1]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: The value 1 appears twice (at index 0 and 3)
```

### Test Case 2: All Unique Elements
```java
Input: nums = [1, 2, 3, 4]
Expected Output: false
Actual Output: false
Status: ✅ Passed

Explanation: All elements are distinct, no duplicates
```

### Test Case 3: Multiple Duplicates
```java
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Multiple values appear more than once (1, 2, 3, 4 all have duplicates)
Note: Algorithm returns true on first duplicate found (second 1)
```

### Test Case 4: Edge Case - Single Element
```java
Input: nums = [1]
Expected Output: false
Actual Output: false
Status: ✅ Passed

Explanation: Only one element, cannot have duplicates
Note: Loop executes once, adds 1 to set, then returns false
```

### Test Case 5: Edge Case - Two Elements (Duplicate)
```java
Input: nums = [1, 1]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Both elements are the same
Note: First iteration adds 1, second iteration finds it in set
```

### Test Case 6: Edge Case - Two Elements (Unique)
```java
Input: nums = [1, 2]
Expected Output: false
Actual Output: false
Status: ✅ Passed

Explanation: Both elements are different
```

### Test Case 7: Negative Numbers
```java
Input: nums = [-1, -2, -3, -1]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Works with negative numbers, -1 appears twice
```

### Test Case 8: Mixed Positive and Negative
```java
Input: nums = [-1, 0, 1, 0, -1]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Both -1 and 0 appear twice
```

### Test Case 9: Large Numbers (Boundary)
```java
Input: nums = [1000000000, -1000000000, 1000000000]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Tests constraint boundaries (±10^9), duplicate found
```

### Test Case 10: Duplicate at End
```java
Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
Expected Output: true
Actual Output: true
Status: ✅ Passed

Explanation: Ensures algorithm checks all elements, not just beginning
```

---

## 📊 Complexity Analysis

### Hash Set Approach (Your Solution) ✅

#### Time Complexity: **O(n)**
**Breakdown:**
- **Single Pass**: We iterate through the array once
  - Loop runs at most `n` times (where n = length of nums)
- **Per-iteration Operations**:
  - `seen.contains(num)`: O(1) average case for HashSet
  - `seen.add(num)`: O(1) average case for HashSet
- **Best Case**: O(1) - First two elements are duplicates
- **Average Case**: O(n) - Iterate through most/all elements
- **Worst Case**: O(n) - No duplicates, check all elements

**Why O(1) for HashSet operations?**
- HashSet uses hash table internally
- Hash function computes index in O(1)
- Average case: no collisions or minimal collisions
- Worst case: O(n) if all elements hash to same bucket (very rare)

#### Space Complexity: **O(n)**
**Breakdown:**
- **HashSet Storage**: 
  - Best Case: O(1) - Duplicate found immediately, set has 1 element
  - Average Case: O(n/2) - Duplicate found halfway
  - Worst Case: O(n) - All elements unique, store all in set
- **Input Array**: O(n) - not counted (already exists)
- **Other Variables**: O(1) - just the `num` variable

**Total**: O(n) worst case for the HashSet

---

### Two Pointers Approach (Alternative)

#### Time Complexity: **O(n log n)**
**Breakdown:**
- **Sorting**: O(n log n) - Arrays.sort() uses Dual-Pivot Quicksort
- **Comparison Loop**: O(n) - scan through sorted array once
- **Total**: O(n log n) + O(n) = **O(n log n)** (sorting dominates)

#### Space Complexity: **O(1) or O(n)**
**Breakdown:**
- **Best Case (In-place sort)**: O(1) extra space
  - Some sort implementations modify array in-place
- **Worst Case**: O(n) 
  - Java's Arrays.sort() may use O(n) auxiliary space for merge operations
  - Recursion stack in quicksort: O(log n)
- **Note**: Modifies original array (side effect)

---

### Brute Force Approach (Not Recommended)

#### Time Complexity: **O(n²)**
- Nested loops: outer loop n times, inner loop up to n times
- Total comparisons: n × (n-1) / 2 ≈ n²/2 = O(n²)

#### Space Complexity: **O(1)**
- No extra data structures, only loop variables

---

### Comparison Table

| Approach | Time Complexity | Space Complexity | Modifies Input? | Best For |
|----------|----------------|------------------|-----------------|----------|
| **Hash Set** | O(n) | O(n) | No | Most cases (optimal) |
| **Two Pointers** | O(n log n) | O(1) or O(n) | Yes | Space-constrained |
| **Brute Force** | O(n²) | O(1) | No | Very small arrays only |

### Which Approach to Use?

**Use Hash Set (Your Solution) when:**
- ✅ You want optimal O(n) time complexity
- ✅ Space is not a critical constraint
- ✅ You need to preserve the original array
- ✅ This is the default choice for interviews!

**Use Two Pointers when:**
- Space is extremely limited (embedded systems)
- You don't mind modifying the input array
- Input is already sorted or nearly sorted

**Never use Brute Force for:**
- Any array larger than ~100 elements
- Production code or coding interviews

---

## 🎓 Key Learnings

### What I Learned

1. **Hash Set Pattern for "Seen Before" Problems**
   - When you need to check if an element has appeared before, HashSet is your friend
   - O(1) lookup makes it perfect for duplicate detection
   - This pattern applies to many problems: finding pairs, checking uniqueness, etc.

2. **Early Return Optimization**
   - Don't process all elements if you can determine the answer early
   - Returning `true` immediately on first duplicate is more efficient
   - Saves both time and space (smaller set)

3. **Trade-offs: Time vs Space**
   - Hash Set: O(n) time, O(n) space - fast but uses memory
   - Two Pointers: O(n log n) time, O(1) space - slower but memory efficient
   - Understanding these trade-offs helps choose the right approach

4. **HashSet Operations**
   - `contains()` is O(1) average case
   - `add()` is O(1) average case
   - Much faster than ArrayList's O(n) `contains()`

5. **Java Collections Best Practices**
   - Declare with interface type: `Set<Integer>` not `HashSet<Integer>`
   - Allows easy swapping of implementations if needed
   - Auto-boxing handles int to Integer conversion

6. **Pattern Recognition**
   - "Contains duplicate" → Think: HashSet or Sorting
   - "Have we seen this?" → Think: HashSet, HashMap, or Set
   - "Check all pairs" → Often can optimize with HashSet

---

### Mistakes to Avoid

1. **Using ArrayList instead of HashSet**
   - ❌ `list.contains(num)` is O(n) - leads to O(n²) overall!
   - ✅ `set.contains(num)` is O(1) - keeps it O(n)
   - Common beginner mistake that fails on large inputs

2. **Forgetting Auto-boxing Overhead**
   - Every `int` is boxed to `Integer` for the set
   - Minor performance cost but negligible for this problem
   - For performance-critical code, consider primitive-based libraries

3. **Modifying Array Without Considering Side Effects**
   - Sorting approach modifies original array
   - Might not be acceptable if array is used later
   - Always clarify with interviewer if modification is allowed

4. **Off-by-One Error in Two Pointers**
   - ❌ Loop to `length` → ArrayIndexOutOfBoundsException at `nums[i+1]`
   - ✅ Loop to `length - 1` → safe access to `nums[i+1]`

5. **Not Considering Edge Cases**
   - Single element array (no duplicate possible)
   - Empty array (though constraint says n ≥ 1)
   - All same elements (return true immediately)

---

### Pattern Insights

**When to use Hash Set for Duplicate Detection:**
- ✅ Need O(n) time complexity
- ✅ Can afford O(n) space
- ✅ Order doesn't matter
- ✅ Need to preserve original array
- ✅ Looking for ANY duplicate (not count or positions)

**When NOT to use Hash Set:**
- ❌ Extremely space-constrained (use sorting + two pointers)
- ❌ Need to find duplicate count or all duplicates (use HashMap instead)
- ❌ Need to maintain order (use different data structure)
- ❌ Working with primitives in performance-critical code (boxing overhead)

**Related Patterns:**
- **Two Sum**: Similar HashSet usage for O(n) solution
- **Longest Consecutive Sequence**: HashSet for O(1) membership
- **Valid Anagram**: Can use HashMap for character frequency

**Key Takeaway:**
> "When you need to check 'have I seen this before?', think HashSet first. It's the go-to pattern for O(1) membership testing." 

---

## 🔗 Similar Problems

### Easy Problems (Same Pattern)
1. **[217. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)** 
   - Similar but with index distance constraint
   - Uses HashMap to track indices
   
2. **[1. Two Sum](https://leetcode.com/problems/two-sum/)**
   - Uses HashMap for O(1) lookups
   - Similar "have we seen this?" pattern

3. **[268. Missing Number](https://leetcode.com/problems/missing-number/)**
   - Can be solved with HashSet
   - Finding what's missing vs what's duplicate

### Medium Problems (Related Patterns)
4. **[219. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)**
   - More complex constraints on duplicates
   - Uses TreeSet for range queries

5. **[442. Find All Duplicates in Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)**
   - Find ALL duplicates, not just detect
   - Can use in-place marking or HashMap

6. **[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)**
   - Only one duplicate, find which one
   - Can use cycle detection (Floyd's algorithm)

### Hard Problems (Advanced)
7. **[128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)**
   - HashSet for O(1) membership testing
   - Building on the same data structure concept

---

## 🎯 Quick Reference Card

### Pattern: Hash Set for Duplicate Detection

**Key Insight:** Use HashSet to check membership in O(1) time

**Template Code:**
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) return true;
        seen.add(num);
    }
    return false;
}
```

**Complexity:**
- Time: O(n)
- Space: O(n)

**When to Use:**
- Need to check "have we seen this before?"
- Detecting duplicates, pairs, or unique elements
- Order doesn't matter
- Can afford O(n) space

**Remember:**
- HashSet.contains() is O(1) average case
- ArrayList.contains() is O(n) - avoid for large data!
- Early return when duplicate found
- Use interface type: `Set<Integer>` not `HashSet<Integer>`

**Common Variations:**
- Use HashMap to store indices/counts
- Use TreeSet for sorted order
- Use LinkedHashSet to maintain insertion order

---

## 🎴 Flashcard Content

**HINTS:**
- Have we seen this element before?
- What data structure gives O(1) lookup?
- Do we need to track indices or just existence?

**KEY INSIGHT:**
Use HashSet to track seen elements - if we see an element that's already in the set, we found a duplicate!

**ALGORITHM:**
1. Create empty HashSet
2. For each number in array
3. If number exists in set: return true
4. Add number to set
5. Return false (no duplicates found)

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#two-pointers)
- [GitHub: 16 Coding Patterns](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)
- [LeetCode Discussion](https://leetcode.com/problems/contains-duplicate/discuss/)
- [Java HashSet Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html)

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified
- [x] Brute force solution considered
- [x] Optimized solution implemented
- [x] All test cases pass
- [x] Complexity analyzed
- [x] Code reviewed and documented
- [x] Learnings documented
- [x] Jira ticket updated
- [x] ✅ **COMPLETED!**
