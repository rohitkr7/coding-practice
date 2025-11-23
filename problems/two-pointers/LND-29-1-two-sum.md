# 1 - Two Sum

**Jira Ticket:** [LND-29](https://rohitroy007.atlassian.net/browse/LND-29)  
**LeetCode:** https://leetcode.com/problems/two-sum  
**Pattern:** Two Pointers  
**Difficulty:** Easy  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Easy  
**Created:** 2025-08-21  
**Last Updated:** 2025-11-23

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/two-sum
Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
Difficulty: Medium
Category: Array

---

## 🤔 Initial Thoughts

### Understanding the Problem
- **Goal:** Find indices of TWO numbers that add up to a target value
- **Input:** Array of integers `nums` and integer `target`
- **Output:** Array containing two indices `[i, j]` where `nums[i] + nums[j] = target`
- **Constraints:**
  - Exactly one solution exists (guaranteed)
  - Cannot use the same element twice
  - Can return answer in any order

### Pattern Recognition
**Why Hash Map (not Two Pointers)?**
- While categorized under "Two Pointers", this problem is better solved with **Hash Map**
- Two Pointers works ONLY on sorted arrays, but sorting loses original indices
- Hash Map allows us to find complements in O(1) time while preserving indices

**What clues in the problem point to Hash Map pattern?**
- Need to find pairs that satisfy a condition (sum = target)
- Need to preserve original indices (can't sort)
- Looking for "complement" relationship: if we have `x`, we need `target - x` 

---

## 💡 Approach

### Brute Force Approach
**Idea:**
- Check every possible pair of numbers using nested loops
- For each `nums[i]`, check if any `nums[j]` (where j > i) sums to target

**Pseudocode:**
```
for i from 0 to n-2:
    for j from i+1 to n-1:
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Time Complexity:** O(n²) - nested loops  
**Space Complexity:** O(1) - no extra space needed

**Why not optimal?** Checking all pairs is inefficient for large arrays.

---

### Optimized Approach: Hash Map (Complement Pattern)
**Key Insight: The Complement Concept** 🔑
```
If: nums[i] + nums[j] = target
Then: nums[j] = target - nums[i]
```

For any number we see, we can instantly calculate what its "partner" should be!

**Idea:**
- Use a Hash Map to store numbers we've seen and their indices
- For each number, check if its complement exists in the map
- If found, return both indices immediately
- If not found, add current number to map for future lookups

**Algorithm Steps:**
1. Create empty hash map: `{value → index}`
2. Iterate through array with index `i`:
   - Calculate complement: `complement = target - nums[i]`
   - Check if complement exists in hash map
   - If YES: return `[map.get(complement), i]`
   - If NO: store current number: `map.put(nums[i], i)`
3. Return empty array (should never reach per problem guarantee)

**Why check BEFORE adding?**
- Prevents using the same element twice
- Example: `nums=[3], target=6` would incorrectly return `[0,0]` if we add first

**Time Complexity:** O(n) - single pass through array  
**Space Complexity:** O(n) - hash map stores up to n elements

---

## 🎨 Visual Explanation

### Example Walkthrough: `nums = [2, 7, 11, 15], target = 9`

```
Initial State:
Array:  [2,  7,  11,  15]
Index:   0   1    2    3
Target: 9
Hash Map: {}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 1: i = 0, nums[0] = 2
  ├─ Complement = 9 - 2 = 7
  ├─ Is 7 in hash map? NO
  ├─ Action: Add {2: 0} to hash map
  └─ Hash Map: {2: 0}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 2: i = 1, nums[1] = 7
  ├─ Complement = 9 - 7 = 2
  ├─ Is 2 in hash map? YES! ✓
  ├─ Found at index: map.get(2) = 0
  └─ Return: [0, 1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Result: [0, 1]
Verification: nums[0] + nums[1] = 2 + 7 = 9 ✓
```

### Why This Works:
1. **First number (2):** We don't know its partner yet, so we save it
2. **Second number (7):** We check "do we have a 2?" → YES! → Solution found!
3. **Efficiency:** Found answer in just 2 iterations instead of checking all pairs

---

## 💻 Implementation

### Java Solution (Optimized with Comments)

```java
class Solution {
    /**
     * Finds two indices in the array whose values sum to the target.
     * 
     * Approach: Hash Map (Complement Pattern)
     * - Store seen numbers with their indices
     * - For each number, check if its complement exists
     * 
     * Time Complexity: O(n) - single pass through array
     * Space Complexity: O(n) - hash map stores up to n elements
     * 
     * @param nums   Array of integers
     * @param target Target sum value
     * @return Array of two indices [i, j] where nums[i] + nums[j] = target
     */
    public int[] twoSum(int[] nums, int target) {
        // Hash Map to store: {value → index}
        // Key: number we've seen
        // Value: its index in the array
        Map<Integer, Integer> seenItems = new HashMap<>();
        
        // Iterate through array with index
        for (int i = 0; i < nums.length; i++) {
            // Calculate what number we need to reach target
            // If current number is X, we need (target - X)
            int complement = target - nums[i];
            
            // Check if we've seen the complement before
            if (seenItems.containsKey(complement)) {
                // Found it! Return the complement's index and current index
                // complement's index comes first (it was seen earlier)
                return new int[]{seenItems.get(complement), i};
            }
            
            // Haven't found complement yet
            // Store current number and its index for future lookups
            // This allows future numbers to find THIS number as their complement
            seenItems.put(nums[i], i);
        }
        
        // Should never reach here per problem constraints
        // (problem guarantees exactly one solution exists)
        return new int[]{};
    }
}
```

### Key Implementation Details:

1. **Why `Map<Integer, Integer>` instead of `HashMap<Integer, Integer>`?**
   - Programming to interfaces is best practice
   - More flexible if we want to change implementation later

2. **Why check BEFORE adding to map?**
   ```java
   // WRONG ORDER:
   seenItems.put(nums[i], i);  // Add first
   if (seenItems.containsKey(complement)) { ... }  // Check second
   // Problem: For nums=[3], target=6, would find complement=3 
   // and return [0,0] (using same element twice!)
   
   // CORRECT ORDER:
   if (seenItems.containsKey(complement)) { ... }  // Check first
   seenItems.put(nums[i], i);  // Add second
   // Solution: Only finds complements from PREVIOUS elements
   ```

3. **Why return `new int[]{...}` directly?**
   - No need for intermediate array variable
   - More concise and readable
   - Immediate return when solution found

4. **Edge Cases Handled:**
   - ✓ Duplicate values: `[3, 3], target=6` → Works! Second 3 finds first 3
   - ✓ Negative numbers: `[-1, -2, -3, -5], target=-8` → Works!
   - ✓ Zero: `[0, 4, 3, 0], target=0` → Works! Second 0 finds first 0
   - ✓ Minimum size: `[1, 2], target=3` → Works!

### Code Explanation

**Line-by-line breakdown:**

1. **`Map<Integer, Integer> seenItems = new HashMap<>();`**
   - Creates hash map to store numbers we've encountered
   - Key = the number itself, Value = its index
   - Example: After seeing `2` at index `0`, map contains `{2: 0}`

2. **`for (int i = 0; i < nums.length; i++)`**
   - Single pass through array (O(n) time)
   - Need index `i` for the final answer

3. **`int complement = target - nums[i];`**
   - Calculate what number would complete the pair
   - Example: If target=9 and current=2, complement=7

4. **`if (seenItems.containsKey(complement))`**
   - O(1) lookup in hash map
   - Checks if we've seen the complement in previous iterations

5. **`return new int[]{seenItems.get(complement), i};`**
   - Found the pair! Return both indices
   - Complement's index is retrieved from map
   - Current index is `i`

6. **`seenItems.put(nums[i], i);`**
   - Store current number for future iterations
   - Future numbers can now find THIS number as their complement 

---

## 🧪 Test Cases

### Test Case 1: Basic Example
```
Input: nums = [2, 7, 11, 15], target = 9
Expected Output: [0, 1]
Actual Output: [0, 1]
Status: ✅ Passed
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

### Test Case 2: Multiple Valid Pairs (but only one solution)
```
Input: nums = [3, 2, 4], target = 6
Expected Output: [1, 2]
Actual Output: [1, 2]
Status: ✅ Passed
Explanation: nums[1] + nums[2] = 2 + 4 = 6
Note: [0, 0] would be wrong (can't use same element twice)
```

### Test Case 3: Duplicate Values
```
Input: nums = [3, 3], target = 6
Expected Output: [0, 1]
Actual Output: [0, 1]
Status: ✅ Passed
Explanation: Both elements are 3, and 3 + 3 = 6
```

### Test Case 4: Negative Numbers
```
Input: nums = [-1, -2, -3, -4, -5], target = -8
Expected Output: [2, 4]
Actual Output: [2, 4]
Status: ✅ Passed
Explanation: nums[2] + nums[4] = -3 + (-5) = -8
```

### Test Case 5: With Zero
```
Input: nums = [0, 4, 3, 0], target = 0
Expected Output: [0, 3]
Actual Output: [0, 3]
Status: ✅ Passed
Explanation: nums[0] + nums[3] = 0 + 0 = 0
```

### Test Case 6: Large Numbers
```
Input: nums = [1000000000, -1000000000, 5], target = 5
Expected Output: [0, 1] or [1, 0]
Actual Output: [0, 1]
Status: ✅ Passed
Explanation: 1000000000 + (-1000000000) = 0, then 0 + 5 = 5
```

---

## 📊 Complexity Analysis

### Time Complexity: O(n)
**Breakdown:**
- **Single loop:** We iterate through the array once: O(n)
- **Hash map operations:** Both `containsKey()` and `put()` are O(1) average case
- **Total:** O(n) × O(1) = O(n)

**Best Case:** O(1) - Solution found at index 1 (second element)
**Average Case:** O(n) - Solution found somewhere in middle
**Worst Case:** O(n) - Solution is last two elements, must scan entire array

### Space Complexity: O(n)
**Breakdown:**
- **Hash Map Storage:** In worst case, we store n-1 elements before finding solution
- **Example:** If solution is `[n-2, n-1]`, we store all previous n-2 elements
- **Return Array:** O(1) - always returns array of size 2
- **Total:** O(n) for hash map

### Comparison with Other Approaches:

| Approach | Time | Space | Trade-off |
|----------|------|-------|----------|
| **Brute Force** | O(n²) | O(1) | Slow but no extra space |
| **Hash Map** ✓ | O(n) | O(n) | Fast but uses extra space |
| **Two Pointers** | O(n log n) | O(1) | Requires sorting, loses indices |

**Why Hash Map is optimal for this problem:**
- Need to preserve original indices (can't sort)
- Trading space for time is worth it: O(n²) → O(n)
- Hash map lookup is O(1) average case 

---

## 🎓 Key Learnings

### What I Learned
1. **The Complement Pattern** 🔑
   - For any pair problem (a + b = target), we can rearrange to: b = target - a
   - This transforms "find two numbers" into "find one number's complement"
   - Hash map makes complement lookup O(1)

2. **Hash Map as "Memory"**
   - Hash maps let us "remember" what we've seen in O(1) time
   - Pattern: Check if complement exists, then add current element
   - This pattern appears in many problems!

3. **Order Matters in Implementation**
   - Must check for complement BEFORE adding to map
   - Prevents using same element twice
   - Small detail, big impact on correctness

4. **Time-Space Trade-offs**
   - Brute force: O(n²) time, O(1) space
   - Hash map: O(n) time, O(n) space
   - Often worth using extra space to gain speed

5. **When NOT to Sort**
   - Two pointers works on sorted arrays
   - But sorting loses original indices
   - This problem specifically needs indices, so sorting doesn't help

### Mistakes I Made
1. **Initial thought:** "This is a Two Pointers problem"
   - **Learning:** Pattern name can be misleading. Analyze the requirements!
   - Two Pointers needs sorted data, but we need to preserve indices

2. **Considered sorting first**
   - **Learning:** Always check what the output requires
   - We need original indices, so sorting breaks the solution

3. **Almost added to map before checking**
   - **Learning:** Order of operations matters for correctness
   - Check complement first, add current element second

### Pattern Insights

**When to use Hash Map (Complement Pattern):**
- ✓ Finding pairs/triplets that satisfy a condition
- ✓ Need to check "have I seen X before?"
- ✓ Need O(1) lookup time
- ✓ Need to preserve original order/indices
- ✓ Problems with "sum equals target" or "difference equals k"

**When NOT to use Hash Map:**
- ✗ Array is already sorted AND you don't need indices → Use Two Pointers
- ✗ Need to find ALL pairs (not just one) → May need different approach
- ✗ Extreme space constraints → Consider brute force or two pointers

**Related Patterns This Unlocks:**
- **Two Sum II** (sorted array) → Two Pointers
- **3Sum** → Sort + Two Pointers
- **4Sum II** → Hash map with pair sums
- **Subarray Sum Equals K** → Prefix sum + Hash map
- **Group Anagrams** → Hash map for grouping

---

## 🔗 Similar Problems

### Direct Variations:
1. **Two Sum II - Input Array Is Sorted** (LeetCode 167) - Easy
   - Same problem but array is sorted
   - Use Two Pointers instead of hash map
   - Space: O(1) instead of O(n)

2. **Two Sum III - Data Structure Design** (LeetCode 170) - Easy
   - Design a class with `add()` and `find()` methods
   - Trade-off: optimize add or find?

3. **Two Sum IV - Input is a BST** (LeetCode 653) - Easy
   - Find two nodes in BST that sum to target
   - Can use hash map or two pointers on inorder traversal

### Pattern Extensions:
4. **3Sum** (LeetCode 15) - Medium ⭐
   - Find three numbers that sum to target
   - Pattern: Sort + Fix one element + Two Pointers on rest

5. **4Sum** (LeetCode 18) - Medium
   - Find four numbers that sum to target
   - Extension of 3Sum pattern

6. **Two Sum Less Than K** (LeetCode 1099) - Easy
   - Find pair with sum < K (closest to K)
   - Use Two Pointers on sorted array

### Related Hash Map Problems:
7. **Subarray Sum Equals K** (LeetCode 560) - Medium ⭐
   - Uses prefix sum + hash map
   - Same complement pattern!

8. **4Sum II** (LeetCode 454) - Medium
   - Four arrays, find count of tuples that sum to 0
   - Hash map stores pair sums

9. **Contains Duplicate II** (LeetCode 219) - Easy
   - Hash map to track indices
   - Similar "have I seen this before?" pattern 

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#two-pointers)
- LeetCode Discussion: https://leetcode.com/problems/two-sum/discuss/

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified (Hash Map, not Two Pointers)
- [x] Brute force solution (O(n²) nested loops)
- [x] Optimized solution (O(n) hash map)
- [x] All test cases pass (LeetCode submission successful)
- [x] Complexity analyzed (Time: O(n), Space: O(n))
- [x] Code reviewed (improvements applied)
- [x] Learnings documented
- [x] Jira ticket updated

---

**Status:** ✅ Completed  
**Last Updated:** 2025-11-23

---

## 🎯 Quick Reference Card

**Pattern:** Hash Map (Complement Pattern)  
**Key Insight:** For each number X, look for (target - X)  
**Time:** O(n) | **Space:** O(n)  

**Template:**
```java
Map<Integer, Integer> seen = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (seen.containsKey(complement)) {
        return new int[]{seen.get(complement), i};
    }
    seen.put(nums[i], i);
}
```

**Remember:** Check BEFORE adding to prevent using same element twice!
