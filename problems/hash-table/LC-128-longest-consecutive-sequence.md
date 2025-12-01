# 8 - Longest Consecutive Sequence

**Jira Ticket:** [LND-35](https://rohitroy007.atlassian.net/browse/LND-35)  
**LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence  
**Pattern:** Hash Table / Array & Hashing
**Difficulty:** Medium  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-12-01

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/longest-consecutive-sequence
Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem

- Find the length (not the sequence itself) of the longest consecutive sequence
- Input: Unsorted array of integers (may contain duplicates, negatives)
- Output: Integer representing the length
- Must be O(n) time complexity (cannot sort!)
- Edge cases: empty array, single element, all duplicates, no consecutive sequences

### Pattern Recognition

**Why Hash Table?**

- Need O(1) lookups to check if consecutive numbers exist
- Cannot sort (would be O(n log n), violates constraint)
- HashSet perfect for "does this exist?" queries

**What clues in the problem point to this pattern?**

- O(n) time requirement → need constant-time lookups
- Need to find relationships between numbers → existence checks
- Unsorted array → can't rely on order, need fast access

---

## 💡 Approach

### Brute Force

**Idea:**

- Sort the array, then scan through counting consecutive runs
- Handle duplicates by skipping them

**Time Complexity:** O(n log n) - sorting dominates  
**Space Complexity:** O(1) or O(n) - depending on sorting algorithm

**Why this doesn't work:** Violates the O(n) time requirement!

### Optimized Approach (HashSet)

**Idea:**

- Use HashSet for O(1) existence checks
- Only count sequences from their starting point (where num-1 doesn't exist)
- Iterate over unique values (HashSet) not the raw array

**Algorithm Steps:**

1. Handle edge case: empty array returns 0
2. Build HashSet from array (eliminates duplicates, enables O(1) lookups)
3. **CRITICAL:** Iterate over HashSet, not original array (optimization for duplicates)
4. For each number, check if it's a sequence start (num-1 doesn't exist)
5. If it's a start, count consecutive numbers using while loop
6. Track maximum length found

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 🎨 Visual Explanation

### Example 1: nums = [100, 4, 200, 1, 3, 2]

```
Step 1: Build HashSet
  nums = [100, 4, 200, 1, 3, 2]
  numSet = {100, 4, 200, 1, 3, 2}

Step 2: Iterate over HashSet and find sequence starts

Iteration 1: num = 100
  ✅ Check: Is 99 in set? NO → This is a sequence start!
  Count: 100 → 101? NO
  Sequence: [100] (length 1)
  maxLength = 1

Iteration 2: num = 4
  ❌ Check: Is 3 in set? YES → Not a start, skip!
  (Saves redundant work)

Iteration 3: num = 200
  ✅ Check: Is 199 in set? NO → This is a sequence start!
  Count: 200 → 201? NO
  Sequence: [200] (length 1)
  maxLength = 1

Iteration 4: num = 1
  ✅ Check: Is 0 in set? NO → This is a sequence start!
  Count: 1 → 2? YES
         2 → 3? YES
         3 → 4? YES
         4 → 5? NO
  Sequence: [1, 2, 3, 4] (length 4)
  maxLength = 4 ✅

Iteration 5: num = 3
  ❌ Check: Is 2 in set? YES → Not a start, skip!

Iteration 6: num = 2
  ❌ Check: Is 1 in set? YES → Not a start, skip!

Final Answer: 4
```

### Why This Works:

- **Only count from starts:** Checking `num-1` ensures we start each sequence once
- **O(1) lookups:** HashSet.contains() is constant time
- **Each number visited ≤ 2 times:** Once in main loop, once when extending a sequence
- **Iterate over HashSet:** Avoids processing duplicates multiple times

---

## 💻 Implementation

### Java Solution (Optimized with Comments)

```java
class Solution {
    /**
     * Find the length of the longest consecutive sequence in an unsorted array.
     * Uses HashSet for O(1) existence checks and only counts from sequence starts.
     *
     * @param nums - unsorted array of integers (may contain duplicates)
     * @return length of longest consecutive sequence
     * Time: O(n), Space: O(n)
     */
    public int longestConsecutive(int[] nums) {
        // Edge case: empty array
        if (nums.length == 0) return 0;

        // Step 1: Store all numbers in HashSet for O(1) lookups
        // Also eliminates duplicates automatically
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int maxLength = 0;

        // Step 2: Iterate over unique values (CRITICAL optimization!)
        for (int num : numSet) {  // NOT: for (int num : nums)
            // Only count from sequence start (num-1 doesn't exist)
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentLength = 1;

                // Extend sequence while consecutive numbers exist
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentLength += 1;
                }

                // Update max if current sequence is longer
                maxLength = Math.max(maxLength, currentLength);
            }
        }

        return maxLength;
    }
}
```

### Key Implementation Details:

1. **HashSet vs Array Iteration (CRITICAL!):**

   - `for (int num : numSet)` NOT `for (int num : nums)`
   - Avoids processing duplicates multiple times
   - Can reduce 100,000 iterations to just 1,000 on duplicate-heavy inputs
   - This is what prevents Time Limit Exceeded!

2. **Sequence Start Detection:**

   - `!numSet.contains(num - 1)` identifies sequence starts
   - Ensures each sequence is counted exactly once
   - Prevents redundant work

3. **Amortized O(n) Analysis:**
   - Outer loop: O(k) where k = unique elements
   - Inner while loops: O(n) total across all iterations
   - Each number extended at most once
   - Total: O(n)

### Code Explanation

- **Line 11:** Edge case handling for empty array
- **Lines 14-17:** Build HashSet for O(1) lookups and automatic duplicate removal
- **Line 22:** **CRITICAL:** Iterate over HashSet (unique values) not array
- **Line 24:** Only process numbers that start sequences (optimization)
- **Lines 28-31:** Extend sequence by checking consecutive numbers
- **Line 34:** Track maximum length encountered

---

---

## 🧪 Test Cases

### Test Case 1: Basic Example

```
Input: nums = [100, 4, 200, 1, 3, 2]
Expected Output: 4
Actual Output: 4
Status: ✅ Passed
Explanation: Tests basic functionality. Sequence [1,2,3,4] has length 4.
```

### Test Case 2: Edge Case - Empty Input

```
Input: nums = []
Expected Output: 0
Actual Output: 0
Status: ✅ Passed
Explanation: Tests edge case of empty array. Should return 0.
```

### Test Case 3: Edge Case - Single Element

```
Input: nums = [1]
Expected Output: 1
Actual Output: 1
Status: ✅ Passed
Explanation: Single element forms a sequence of length 1.
```

### Test Case 4: All Consecutive

```
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Expected Output: 9
Actual Output: 9
Status: ✅ Passed
Explanation: Nearly all elements (0-8) form one long sequence. Duplicate 0 doesn't affect result.
```

### Test Case 5: No Consecutive Sequences

```
Input: nums = [10, 20, 30, 40]
Expected Output: 1
Actual Output: 1
Status: ✅ Passed
Explanation: No consecutive numbers exist. Each forms its own sequence of length 1.
```

### Test Case 6: Many Duplicates (Performance Test)

```
Input: nums = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3]
Expected Output: 3
Actual Output: 3
Status: ✅ Passed
Explanation: Tests the critical optimization (iterate over HashSet). Sequence is [1,2,3].
Why important: Iterating over array would process 16 elements, but HashSet has only 3 unique values!
```

### Test Case 7: Negative Numbers

```
Input: nums = [-3, -2, -1, 0, 1]
Expected Output: 5
Actual Output: 5
Status: ✅ Passed
Explanation: Consecutive sequences work with negative numbers too.
```

### Test Case 8: Two Separate Sequences

```
Input: nums = [1, 2, 3, 10, 11, 12, 13]
Expected Output: 4
Actual Output: 4
Status: ✅ Passed
Explanation: Two sequences exist ([1,2,3] and [10,11,12,13]). Return longest (4).
```

---

## 📊 Complexity Analysis

### Time Complexity: O(n)

**Breakdown:**

- **Building HashSet:** O(n) - iterate through array once, each add() is O(1)
- **Main loop (iterate over HashSet):** O(k) where k = number of unique elements ≤ n
- **For each sequence start:**
  - Check if num-1 exists: O(1)
  - While loop extending sequence: O(L) where L = length of that sequence
- **Key insight:** Each number is visited at most twice total:
  - Once in the outer loop (checking if it's a start)
  - Once when it's counted as part of a sequence (in the while loop)
- **Total:** O(n) + O(n) = **O(n)**

**Why nested loops are still O(n):**

```
Consider [1, 2, 3, 4, 5]:

Outer loop iterations:
  num=1: Check 0? No → START
         While: check 2✓, check 3✓, check 4✓, check 5✓, check 6✗
         (Visits 1, extends to 2,3,4,5)

  num=2: Check 1? Yes → SKIP (not a start)
  num=3: Check 2? Yes → SKIP
  num=4: Check 3? Yes → SKIP
  num=5: Check 4? Yes → SKIP

Total operations:
- Outer loop: 5 checks
- While loops: 4 extensions (only from num=1)
- Each number processed at most 2 times total
- 5 + 4 = 9 operations for 5 elements = O(n)
```

### Space Complexity: O(n)

**Breakdown:**

- **HashSet storage:** O(n) in worst case (all elements unique)
  - Best case: O(k) where k = unique elements
  - Worst case: O(n) when no duplicates
- **Variables:** O(1) - maxLength, currentNum, currentLength
- **Overall:** **O(n)**

### Comparison with Other Approaches:

| Approach                    | Time Complexity               | Space Complexity | Passes O(n) Requirement?    | Notes                                     |
| --------------------------- | ----------------------------- | ---------------- | --------------------------- | ----------------------------------------- |
| **Sorting**                 | O(n log n)                    | O(1) to O(n)     | ❌ No                       | Too slow, fails constraint                |
| **Brute Force**             | O(n³)                         | O(1)             | ❌ No                       | Check each number, search for consecutive |
| **HashSet (iterate array)** | O(n) worst, TLE on duplicates | O(n)             | ⚠️ Technically yes, but TLE | Processes duplicates multiple times       |
| **HashSet (iterate set)**   | O(n)                          | O(n)             | ✅ Yes                      | **Optimal solution!**                     |

---

## 🎓 Key Learnings

### What I Learned

1. **HashSet for O(1) lookups:** Using HashSet enables constant-time existence checks, which is crucial for meeting O(n) requirements.

2. **Start detection optimization:** Checking `!numSet.contains(num - 1)` ensures we only count each sequence once from its true beginning, avoiding redundant work.

3. **Iterate over unique values, not raw input:** `for (int num : numSet)` instead of `for (int num : nums)` is CRITICAL when duplicates are present. This single-line change prevents Time Limit Exceeded.

4. **Amortized O(n) with nested loops:** Not all nested loops are O(n²)! If each element is processed a constant number of times total, it's still O(n). Here, each number is visited at most twice.

5. **Space-time tradeoff:** We use O(n) extra space (HashSet) to achieve O(n) time. This is often necessary to meet aggressive time constraints.

### Mistakes I Made

1. **Initial mistake: Iterating over array instead of HashSet**

   - First implementation: `for (int num : nums)`
   - Result: Time Limit Exceeded on test case 80+
   - Fix: `for (int num : numSet)`
   - Lesson: When you have duplicates and a HashSet, iterate over the set!

2. **Misconception about duplicate processing:**

   - Thought: "Duplicates don't matter because HashSet removes them"
   - Reality: They DO matter if you iterate over the original array!
   - Impact: Processing 100,000 duplicates vs 1,000 unique values = 100x slowdown

3. **Not recognizing the performance edge case:**
   - LeetCode added test cases with heavy duplicates
   - Previous solution was accepted, now it times out
   - Lesson: Always consider worst-case inputs (extreme duplicates, all same value, etc.)

### Pattern Insights

**When to use Hash Table pattern:**

- Need O(1) lookups for existence checks
- Working with unsorted data and can't afford to sort
- Finding relationships between elements (consecutive, pairs, etc.)
- Space-time tradeoff acceptable (O(n) space for O(n) time)

**When NOT to use this pattern:**

- Space is extremely limited (O(1) space requirement)
- Data structure doesn't support hashing (non-hashable types)
- Order matters and must be preserved (use array or LinkedHashMap)
- Data is already sorted (can use two pointers or binary search instead)

**Related patterns:**

- **Two Pointers:** Alternative if data is sorted (but violates O(n) here)
- **Sliding Window:** For subarrays instead of subsequences
- **Union-Find:** For grouping disjoint sets

**Key insight for this specific problem:**
"Only start counting from sequence beginnings" - this transforms a potentially O(n²) problem into O(n).

---

## 🔗 Similar Problems

### Easy

1. **Contains Duplicate** (LC 217) - Use HashSet for existence check
2. **Two Sum** (LC 1) - HashMap for O(1) lookups

### Medium

1. **Longest Consecutive Sequence** (LC 128) - This problem! ✅
2. **Missing Number** (LC 268) - Find missing element in range
3. **Find All Numbers Disappeared in an Array** (LC 448) - Similar pattern
4. **Top K Frequent Elements** (LC 347) - HashMap + frequency counting

### Hard

1. **First Missing Positive** (LC 41) - O(n) time, O(1) space variant
2. **Maximum Gap** (LC 164) - Finding max difference in sorted array

### Problems Using Same Pattern

- **Group Anagrams** (LC 49) - HashMap for grouping
- **Valid Sudoku** (LC 36) - HashSet for duplicate detection
- **Longest Substring Without Repeating Characters** (LC 3) - HashMap + Sliding Window

---

## 🎯 Quick Reference Card

**Pattern:** Hash Table / Set  
**Key Insight:** Only count consecutive sequences from their starting point (where num-1 doesn't exist)  
**Time:** O(n) | **Space:** O(n)

**Template:**

```java
public int longestConsecutive(int[] nums) {
    if (nums.length == 0) return 0;

    // Build HashSet for O(1) lookups
    HashSet<Integer> set = new HashSet<>();
    for (int num : nums) set.add(num);

    int maxLen = 0;

    // CRITICAL: Iterate over set, not array!
    for (int num : set) {
        // Only start from sequence beginning
        if (!set.contains(num - 1)) {
            int len = 1;
            // Extend sequence
            while (set.contains(num + len)) len++;
            maxLen = Math.max(maxLen, len);
        }
    }

    return maxLen;
}
```

**Remember:**

- ✅ Iterate over HashSet (unique values), NOT the original array
- ✅ Only count from sequence starts (num-1 not present)
- ✅ Each number visited at most 2 times = O(n)
- ⚠️ Common pitfall: Iterating over array causes TLE with duplicates!

---

## 🎴 Flashcard Content

**HINTS:**

- How to check if num-1 or num+1 exist quickly?
- How to avoid counting same sequence twice?
- Should we iterate over array or unique values?

**KEY INSIGHT:**
Only count from sequence starts (where num-1 doesn't exist). Iterate over HashSet, not array!

**ALGORITHM:**

1. Build HashSet for O(1) lookups
2. Iterate over HashSet (not array!)
3. If num-1 doesn't exist: sequence start
4. Count consecutive: num→num+1→num+2...
5. Track max length

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#two-pointers)
- LeetCode Discussion: https://leetcode.com/problems/longest-consecutive-sequence/discuss/

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified
- [x] Brute force solution
- [x] Optimized solution
- [x] All test cases pass
- [x] Complexity analyzed
- [x] Code reviewed
- [x] Learnings documented
- [x] Jira ticket updated

---

**Status:** ✅ Completed  
**Last Updated:** 2025-12-01
