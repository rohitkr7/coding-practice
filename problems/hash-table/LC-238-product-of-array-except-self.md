# 6 - Product of Array Except Self

**Jira Ticket:** [LND-37](https://rohitroy007.atlassian.net/browse/LND-37)  
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self  
**Pattern:** Array Manipulation / Prefix-Suffix Products  
**Difficulty:** Medium  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-11-30

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/product-of-array-except-self
Problem Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm running in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem

- What are we asked to find/compute?
- What are the inputs and outputs?
- What are the edge cases?

### Pattern Recognition

**Why Array Manipulation / Prefix-Suffix Products?**

- Need to compute products from both left and right directions
- Cannot use division operator (eliminates simple total/current approach)
- Requires O(n) time complexity

**What clues in the problem point to this pattern?**

- "Product of all elements EXCEPT self" → need left × right products
- "Without division" constraint → must use prefix/suffix approach
- "O(n) time" requirement → single or double pass solution

---

## 💡 Approach

### Brute Force Approach

**Idea:** For each position i, multiply all other elements (nested loops)

**Algorithm:**

- For each index i:
  - Initialize product = 1
  - For each index j (where j ≠ i):
    - Multiply product by nums[j]
  - Store product in result[i]

**Time Complexity:** O(n²) - nested loops  
**Space Complexity:** O(1) - excluding output array

**Why it fails:** Too slow for n = 10⁵ (would need 10 billion operations!)

---

### Division-Based Approach (Not Allowed)

**Idea:** Calculate total product, then divide by current element

**Algorithm:**

- Calculate total = product of all numbers
- For each index i: result[i] = total / nums[i]

**Time Complexity:** O(n) ✅  
**Space Complexity:** O(1) ✅

**Why we can't use it:**

- Division is forbidden by problem constraints
- Doesn't handle zeros properly (division by zero!)

---

### Optimized Approach: Prefix-Suffix Products

**Idea:** For each position i, calculate (product of all left) × (product of all right)

**Key Insight:**

```
result[i] = (nums[0] × ... × nums[i-1]) × (nums[i+1] × ... × nums[n-1])
          = prefix[i] × suffix[i]
```

**Algorithm Steps:**

1. **Build prefix products in result array:**
   - result[0] = 1 (no elements before index 0)
   - For i from 1 to n-1: result[i] = result[i-1] × nums[i-1]
2. **Build suffix products on-the-fly and multiply:**

   - Initialize suffix = 1
   - For i from n-1 to 0:
     - result[i] \*= suffix (multiply prefix by suffix)
     - suffix \*= nums[i] (update suffix for next iteration)

3. **Return result array**

**Time Complexity:** O(n) - two passes through array  
**Space Complexity:** O(1) - only one variable (not counting output)

---

## 🎨 Visual Explanation

### Example Walkthrough: nums = [1, 2, 3, 4]

**Step 1: Build Prefix Products in Result Array**

```
Index:        0    1    2    3
nums:       [ 1,   2,   3,   4 ]

Initialize:
result[0] = 1 (no elements before index 0)

Iteration i=1:
result[1] = result[0] × nums[0] = 1 × 1 = 1

Iteration i=2:
result[2] = result[1] × nums[1] = 1 × 2 = 2

Iteration i=3:
result[3] = result[2] × nums[2] = 2 × 3 = 6

After Step 1:
result:     [ 1,   1,   2,   6 ]
             ↑    ↑    ↑    ↑
            (1)  (1) (1×2) (1×2×3)
```

**Step 2: Build Suffix Products and Multiply**

```
Initialize: suffix = 1

Iteration i=3:
result[3] = result[3] × suffix = 6 × 1 = 6
suffix = suffix × nums[3] = 1 × 4 = 4

Iteration i=2:
result[2] = result[2] × suffix = 2 × 4 = 8
suffix = suffix × nums[2] = 4 × 3 = 12

Iteration i=1:
result[1] = result[1] × suffix = 1 × 12 = 12
suffix = suffix × nums[1] = 12 × 2 = 24

Iteration i=0:
result[0] = result[0] × suffix = 1 × 24 = 24
suffix = suffix × nums[0] = 24 × 1 = 24

Final Result:
result:     [ 24,  12,   8,   6 ]
```

**Step 3: Verification**

```
Index 0: 2 × 3 × 4 = 24 ✓
Index 1: 1 × 3 × 4 = 12 ✓
Index 2: 1 × 2 × 4 = 8 ✓
Index 3: 1 × 2 × 3 = 6 ✓
```

### Why This Works:

**Key Observation:** For any index i:

- `result[i]` (after step 1) contains product of all elements **before** i
- `suffix` (in step 2) contains product of all elements **after** i
- Multiplying them gives product of all elements **except** i

**Visual Representation:**

```
For index 2 in [1, 2, 3, 4]:

         LEFT SIDE  |  i  | RIGHT SIDE
         (1 × 2)    |  3  |    (4)
            ↓              ↓
         prefix = 2    suffix = 4
                  ↓
         result[2] = 2 × 4 = 8 ✓
```

**Mathematical Formula:**

```
result[i] = (nums[0] × ... × nums[i-1]) × (nums[i+1] × ... × nums[n-1])
          =        prefix[i]            ×         suffix[i]
```

---

## 💻 Implementation

### Java Solution (Space-Optimized - O(1))

```java
class Solution {
    /**
     * Calculate product of all elements except self using prefix-suffix approach.
     * Time: O(n) - two passes through array
     * Space: O(1) - only uses result array (output) and one variable
     */
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] result = new int[len];

        // Step 1: Build prefix products directly in result array
        result[0] = 1;  // No elements before index 0
        for (int i = 1; i < len; i++) {
            // Store cumulative product of all elements before i
            result[i] = result[i - 1] * nums[i - 1];
        }

        // Step 2: Build suffix products on-the-fly and multiply into result
        int suffix = 1;  // Running product from right
        for (int i = len - 1; i >= 0; i--) {
            // Multiply prefix (in result) by suffix
            result[i] *= suffix;
            // Update suffix for next iteration
            suffix *= nums[i];
        }

        return result;
    }
}
```

### Key Implementation Details:

1. **Reusing Output Array**: Instead of creating separate prefix and suffix arrays, we:

   - Use `result[]` to store prefix products in first pass
   - Multiply suffix products directly into `result[]` in second pass
   - This achieves O(1) extra space (not counting output)

2. **Running Suffix Variable**: Using a single `int suffix` instead of an array:

   - Starts at 1 (no elements after last index)
   - Accumulates products as we iterate backwards
   - Updates after each multiplication

3. **Two-Pass Strategy**:
   - **Pass 1 (Forward)**: Build prefix products left-to-right
   - **Pass 2 (Backward)**: Multiply by suffix products right-to-left

### Code Explanation:

**First Loop (Lines 13-16) - Prefix Products:**

```java
result[0] = 1              // Nothing to multiply before index 0
result[1] = 1 × nums[0]    // Product of elements before index 1
result[2] = (1×nums[0]) × nums[1]  // Product before index 2
result[3] = (1×nums[0]×nums[1]) × nums[2]  // Product before index 3
```

**Second Loop (Lines 19-24) - Suffix Multiplication:**

```java
// Start from right, multiply prefix by suffix
i=3: result[3] = prefix[3] × 1 (no elements after)
     suffix = 1 × nums[3] (update for next)

i=2: result[2] = prefix[2] × suffix (elements after index 2)
     suffix = suffix × nums[2] (update for next)

// Continue backwards, building suffix and multiplying
```

**Example Execution for [1,2,3,4]:**

````
After Pass 1 (prefix):   result = [1, 1, 2, 6]
After Pass 2 (suffix):   result = [24, 12, 8, 6]
``` ***

## 🧪 Test Cases

### Test Case 1: Basic Example

```
Input: [1, 2, 3, 4]
Expected Output: [24, 12, 8, 6]
Actual Output: [24, 12, 8, 6]
Status: ✅ Passed
```

**Explanation:** Standard case with all positive numbers. Tests basic algorithm correctness.

---

### Test Case 2: Array with Zero

```
Input: [-1, 1, 0, -3, 3]
Expected Output: [0, 0, 9, 0, 0]
Actual Output: [0, 0, 9, 0, 0]
Status: ✅ Passed
```

**Explanation:**
- Tests zero handling - critical edge case
- Only index 2 (the zero position) has non-zero result
- All other positions multiply with the zero → result is 0
- Result at index 2: (-1) × 1 × (-3) × 3 = 9

---

### Test Case 3: Two Elements (Minimum)

```
Input: [1, 2]
Expected Output: [2, 1]
Actual Output: [2, 1]
Status: ✅ Passed
```

**Explanation:**
- Minimum array size (constraint: 2 ≤ length)
- Tests edge case handling
- Index 0: product except self = 2
- Index 1: product except self = 1

---

### Test Case 4: All Negative Numbers

```
Input: [-1, -2, -3]
Expected Output: [6, 3, 2]
Actual Output: [6, 3, 2]
Status: ✅ Passed
```

**Explanation:**
- Tests negative number handling
- Index 0: (-2) × (-3) = 6
- Index 1: (-1) × (-3) = 3
- Index 2: (-1) × (-2) = 2

---

### Test Case 5: Multiple Zeros

```
Input: [0, 0, 1, 2]
Expected Output: [0, 0, 0, 0]
Actual Output: [0, 0, 0, 0]
Status: ✅ Passed
```

**Explanation:**
- Multiple zeros mean ALL positions will be 0
- Any position includes at least one zero in its product
- Critical edge case for zero handling`

---

## 📊 Complexity Analysis

### Time Complexity: O(n)

**Breakdown:**
- **Pass 1 (Prefix products)**: O(n) - iterate through array once left-to-right
- **Pass 2 (Suffix products)**: O(n) - iterate through array once right-to-left
- **Total**: O(n) + O(n) = O(2n) = **O(n)**

**No nested loops!** Each element is visited exactly twice (constant factor).

### Space Complexity: O(1)

**Breakdown:**
- **result array**: O(n) - required for output, doesn't count as extra space
- **suffix variable**: O(1) - single integer  variable
- **Other variables (len, i)**: O(1) - constant space
- **Total auxiliary space**: **O(1)**

### Comparison with Other Approaches:

| Approach | Time | Space | Division Used | Notes |
|----------|------|-------|---------------|-------|
| Brute Force | O(n²) | O(1) | No | Too slow - nested loops |
| Division-Based | O(n) | O(1) | Yes ❌ | Not allowed by problem |
| Prefix-Suffix (2 arrays) | O(n) | O(n) | No | Works but uses extra space |
| **Optimized Prefix-Suffix** | **O(n)** | **O(1)** | **No** | **Optimal solution!** |

**Trade-offs:**
- ✅ Meets O(n) time requirement
- ✅ Meets "no division" constraint
- ✅ Achieves O(1) extra space (optimal)
- ✅ Easy to understand and implement ***

## 🎓 Key Learnings

### What I Learned

1. **Prefix-Suffix Pattern**: Powerful technique for "all except self" problems
   - Build cumulative information from left (prefix)
   - Build cumulative information from right (sufficient)
   - Combine them for the answer

2. **Space Optimization**: Can reuse output array for intermediate calculations
   - First pass stores prefix products in result array
   - Second pass multiplies suffix on-the-fly
   - Avoids need for separate prefix/suffix arrays

3. **Zero Handling**: Algorithm naturally handles zeros without special cases
   - Single zero: only that position can have non-zero result
   - Multiple zeros: all positions will be zero
   - No explicit if-else needed!

4. **Two-Pass Strategy**: Sometimes two passes are better than one complicated pass
   - First pass: simple prefix calculation
   - Second pass: suffix calculation and combination
   - Cleaner logic, easier to debug

### Mistakes I Made

1. **Initial Bug**: Added redundant array initializations outside loops
   - `prefixProduct[1] = nums[0]` was unnecessary and error-prone
   - Loop already handles this - don't duplicate logic!
   - **Lesson**: Let loops do their job, avoid premature initialization

2. **Not Testing Minimum Case**: Didn't initially test with len=2 array
   - Could have caught the initialization bug earlier
   - **Lesson**: Always test with minimum constraint values

3. **Overlooked Space Optimization**: First implementation used O(n) extra space
   - Used separate arrays for prefix and suffix
   - Didn't realize result array could serve double duty
   - **Lesson**: Look for opportunities to reuse existing arrays

### Pattern Insights

**When to use Prefix-Suffix Products:**
- ✅ Need information from both directions (left AND right)
- ✅ "All except current" type problems
- ✅ Division is not allowed or impractical
- ✅ Need O(n) time without nested loops
- ✅ Problems involving cumulative operations (product, sum, XOR)

**When NOT to use this pattern:**
- ❌ Division is allowed and no zeros (simpler approach: total product / current)
- ❌ Only need information from one direction (use simple prefix or suffix)
- ❌ Need to maintain actual subsequences (not just aggregated values)
- ❌ Problem requires O(log n) time (consider divide-and-conquer instead)

**Related Patterns:**
- Prefix Sum (for range sum queries)
- Running Product/XOR (same concept, different operation)
- Trapping Rain Water (similar two-pointer + prefix/suffix idea)

---

## 🔗 Similar Problems

### Same Pattern (Prefix-Suffix)
1. **[LC-42] Trapping Rain Water** (Hard)
   - Uses prefix max from left, suffix max from right
   - Similar two-pass strategy

2. **[LC-offers] Construct Array** (Easy)
   - Direct variation of this problem
   - Same algorithm applies

### Related Concepts
3. **[LC-560] Subarray Sum Equals K** (Medium)
   - Uses prefix sum pattern
   - HashMap + cumulative sum

4. **[LC-325] Maximum Size Subarray Sum Equals k** (Medium)
   - Prefix sum with hash table
   - Similar cumulative approach

5. **[LC-1588] Sum of All Odd Length Subarrays** (Easy)
   - Prefix sum application
   - Good for pattern practice

### Array Manipulation
6. **[LC-41] First Missing Positive** (Hard)
   - In-place array manipulation
   - O(n) time, O(1) space pattern

7. **[LC-73] Set Matrix Zeroes** (Medium)
   - O(1) space optimization challenge
   - Clever use of input for storage

---

## 🎴 Flashcard Content

**HINTS:**
- Can we use prefix and suffix products?
- How to avoid division?
- Can we reuse the output array to save space?

**KEY INSIGHT:**
Use two passes - prefix products left→right, then multiply by suffix products right→left, storing in result array to achieve O(1) space.

**ALGORITHM:**
1. Create result array
2. Forward pass: Store prefix products in result
3. Backward pass: Multiply by suffix products
4. Each result[i] = (product of all left) × (product of all right)
5. Return result array

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#array-manipulation)
- LeetCode Discussion: https://leetcode.com/problems/product-of-array-except-self/discuss/

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
- [ ] Jira ticket updated

---

**Status:** ✅ **Completed**
**Last Updated:** 2025-11-30
```
````
