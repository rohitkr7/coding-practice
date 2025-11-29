# 5 - Top K Frequent Elements

**Jira Ticket:** [LND-36](https://rohitroy007.atlassian.net/browse/LND-36)  
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements  
**Pattern:** Top K Elements  
**Difficulty:** Medium  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-11-29

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/top-k-frequent-elements
Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem
- **Goal:** Find the k elements that appear most frequently in the array
- **Input:** Array of integers `nums` and integer `k`
- **Output:** Array of k integers (the most frequent elements)
- **Key Points:**
  - Return the actual elements, NOT their frequencies
  - Order of output doesn't matter
  - Guaranteed to have exactly one valid answer
  - k is always valid (≤ number of unique elements)

### Pattern Recognition
**Why Top K Elements?**
- Problem explicitly asks for "k most frequent" - classic Top K pattern
- Need to rank elements by a criterion (frequency) and select top k
- Don't need full sorting, just the top k

**What clues in the problem point to this pattern?**
- Keywords: "top k", "most frequent"
- Need partial ordering, not full sort
- k is typically much smaller than n (k << n)
- Pattern applies when you need top/bottom k by some metric 

---

## 💡 Approach

### Brute Force
**Idea:**
- Count frequency of each element using a HashMap
- Convert HashMap to a list of (element, frequency) pairs
- Sort the list by frequency in descending order
- Take the first k elements from sorted list

**Algorithm:**
```java
1. Build frequency map: {element -> count}
2. Convert to List<Entry>
3. Sort by frequency: O(n log n)
4. Return first k elements
```

**Time Complexity:** O(n log n) - dominated by sorting  
**Space Complexity:** O(n) - for frequency map and list

**Why not optimal?** Sorting all elements is overkill when we only need top k  

### Optimized Approach: Bucket Sort
**Key Insight:** 🔑
- Maximum frequency any element can have = n (array length)
- Frequencies are bounded: [1, n]
- Use frequency as array index for O(1) access!

**Idea:**
- Create buckets array where `buckets[i]` contains all elements with frequency `i`
- Traverse buckets from high to low frequency
- Collect first k elements encountered

**Algorithm Steps:**
1. Build frequency map: {element -> count} - O(n)
2. Create buckets array of size n+1 - O(n)
3. Place each element into `buckets[its_frequency]` - O(n)
4. Traverse buckets from index n down to 0, collect k elements - O(n)

**Why Bucket Sort Works Here:**
- Frequency range is small and known: [1, n]
- Can use frequency directly as index
- Avoids comparison-based sorting
- Natural ordering by traversing high→low

**Time Complexity:** O(n) - Linear time! ⚡  
**Space Complexity:** O(n) - for frequency map and buckets

---

## 🎨 Visual Explanation

### Example: `nums = [1,1,1,1,7,7,3,3,3]`, `k = 2`

```
STEP 1: Count Frequencies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Array: [1, 1, 1, 1, 7, 7, 3, 3, 3]

Frequency Map:
┌─────────┬───────────┐
│ Element │ Frequency │
├─────────┼───────────┤
│    1    │     4     │ ← Most frequent
│    7    │     2     │
│    3    │     3     │
└─────────┴───────────┘


STEP 2: Create Buckets (size = n+1 = 10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buckets array where index = frequency:

Index:  0   1   2   3   4   5   6   7   8   9
       ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
       │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │
       └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘


STEP 3: Fill Buckets
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Place each element at index = its frequency:

Element 1 (freq=4) → buckets[4]
Element 7 (freq=2) → buckets[2]
Element 3 (freq=3) → buckets[3]

Index:  0   1   2   3   4   5   6   7   8   9
       ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
       │   │   │[7]│[3]│[1]│   │   │   │   │   │
       └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                 │   │   │
              freq=2  3   4


STEP 4: Collect Top k=2 (High → Low frequency)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Traverse from index 9 down to 0:

i=9: buckets[9] = []     → skip
i=8: buckets[8] = []     → skip
...
i=4: buckets[4] = [1]    → add 1 to result  ✓ (count=1)
i=3: buckets[3] = [3]    → add 3 to result  ✓ (count=2)
STOP! count == k

Result: [1, 3]  ✅
```

### Why This Works:
- **Frequency as Index:** Direct mapping, O(1) access
- **High→Low Traversal:** Most frequent elements first
- **Early Stop:** Once we have k elements, we're done
- **No Sorting Needed:** Natural order from bucket traversal

---

## 💻 Implementation

### Java Solution (Bucket Sort - O(n) Time)

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // PHASE 1: Build frequency map to count occurrences of each element
        // Using LinkedHashMap (though HashMap would also work fine here)
        LinkedHashMap<Integer, Integer> freq = new LinkedHashMap();

        // Count frequency of each number
        // Time: O(n) - single pass through array
        for (int num : nums) {
            if (freq.containsKey(num))
                freq.put(num, freq.get(num) + 1);
            else
                freq.put(num, 1);
        }

        // PHASE 2: Create buckets where index = frequency
        // Key insight: max frequency = nums.length (if all elements are same)
        // So we need buckets[0] to buckets[nums.length] → size = nums.length + 1
        int count = 0;
        int[] result = new int[k];
        List<Integer>[] buckets = new List[nums.length + 1];  // +1 is crucial!

        // Initialize each bucket as empty ArrayList
        // Each bucket will hold all elements with that frequency
        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        // Fill buckets: place each element into bucket[its frequency]
        // Example: if element 5 appears 3 times, add 5 to buckets[3]
        // Time: O(n) - iterate through unique elements
        for (int key : freq.keySet()) {
            buckets[freq.get(key)].add(key);
        }

        // PHASE 3: Collect top k elements by traversing buckets from high to low frequency
        // Start from highest possible frequency (nums.length) down to 0
        // This ensures we get the MOST frequent elements first
        for (int i = nums.length; i >= 0; i--) {
            // Only continue if we haven't collected k elements yet
            if (count < k) {
                // Add all elements from current frequency bucket
                // Stop early if we reach k elements (count < k check in loop)
                for (int j = 0; j < buckets[i].size() && count < k; j++, count++) {
                    result[count] = buckets[i].get(j);
                }
            } else {
                break;  // Early exit once we have k elements
            }
        }
        
        return result;
    }
}
```

### Alternative: Cleaner Version with `getOrDefault()`

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);  // Cleaner!
        }

        // Step 2: Create and fill buckets
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }
        
        for (int key : freq.keySet()) {
            buckets[freq.get(key)].add(key);
        }

        // Step 3: Collect top k
        int[] result = new int[k];
        int count = 0;
        for (int i = nums.length; i >= 0 && count < k; i--) {
            for (int num : buckets[i]) {
                result[count++] = num;
                if (count == k) return result;
            }
        }
        
        return result;
    }
}
```

### Code Explanation

**Phase 1: Frequency Counting (Lines 7-13)**
- Use HashMap to count occurrences of each element
- `freq.getOrDefault(num, 0) + 1` is cleaner than if-else
- Time: O(n) for single pass

**Phase 2: Bucket Creation (Lines 16-27)**
- **Critical:** Array size must be `nums.length + 1` to handle max frequency
- Each bucket is a `List<Integer>` to hold multiple elements with same frequency
- Fill buckets by using frequency as index: `buckets[freq]`

**Phase 3: Collection (Lines 30-40)**
- **Start from highest index** (nums.length) to get most frequent first
- Loop condition: `i >= 0` not `i > 0` (don't skip bucket[0])
- Inner loop: add elements until count reaches k
- Early exit optimization once k elements collected 

---

## 🧪 Test Cases

### Test Case 1: Basic Example (LeetCode Example)
```java
Input: nums = [1,1,1,2,2,3], k = 2
Expected Output: [1,2] or [2,1]
Actual Output: [1,2]
Status: ✅ Passed
Explanation: Elements 1 and 2 are most frequent (3 and 2 times respectively)
```

### Test Case 2: Single Element Array
```java
Input: nums = [1], k = 1
Expected Output: [1]
Actual Output: [1]
Status: ✅ Passed
Explanation: Only one unique element, must be in top k
```

### Test Case 3: All Elements Same Frequency
```java
Input: nums = [1,2,3], k = 2
Expected Output: Any 2 of [1,2,3]
Actual Output: [3,2] (or any valid combo)
Status: ✅ Passed
Explanation: All have frequency=1, any k elements are valid
```

### Test Case 4: All Elements Identical
```java
Input: nums = [5,5,5,5,5], k = 1
Expected Output: [5]
Actual Output: [5]
Status: ✅ Passed
Explanation: Maximum frequency scenario (freq = n)
Note: This tests buckets[nums.length] - crucial edge case!
```

### Test Case 5: k Equals Unique Count
```java
Input: nums = [1,1,2,2,3,3], k = 3
Expected Output: [1,2,3] (any order)
Actual Output: [1,2,3]
Status: ✅ Passed
Explanation: Return all unique elements when k = unique count
```

### Test Case 6: Complex Frequencies
```java
Input: nums = [1,1,1,1,7,7,3,3,3], k = 2
Expected Output: [1,3] or [3,1]
Actual Output: [1,3]
Status: ✅ Passed
Explanation: freq(1)=4, freq(3)=3, freq(7)=2 → top 2 are 1 and 3
```

### Test Case 7: Negative Numbers
```java
Input: nums = [-1,-1,-1,2,2,3], k = 2
Expected Output: [-1,2] or [2,-1]
Actual Output: [-1,2]
Status: ✅ Passed
Explanation: Negative numbers work same as positive
```

---

## 📊 Complexity Analysis

### Time Complexity: O(n)
**Breakdown:**
- **Phase 1 - Frequency counting:** O(n)
  - Single pass through array to build HashMap
  - Each put/get operation is O(1) average
- **Phase 2 - Bucket creation:** O(n)
  - Initialize buckets array: O(n)
  - Fill buckets: O(n) for iterating unique elements
- **Phase 3 - Collection:** O(n) worst case
  - Traverse buckets: at most n iterations
  - Inner loop processes each element once across all buckets
- **Total:** O(n) + O(n) + O(n) = **O(n)** linear time! ⚡

**Note:** This beats sorting-based approaches which are O(n log n)

### Space Complexity: O(n)
**Breakdown:**
- **Frequency HashMap:** O(n) in worst case (all unique elements)
- **Buckets array:** O(n) - array of size n+1
- **Lists in buckets:** O(n) total across all buckets (stores each unique element once)
- **Result array:** O(k) where k ≤ n
- **Total:** O(n) + O(n) + O(k) = **O(n)** space

### Comparison with Alternative Approaches

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| **Bucket Sort** | **O(n)** | O(n) | ✅ **Best overall** - optimal time |
| Sorting | O(n log n) | O(n) | ❌ Slower, but simpler to code |
| Min Heap | O(n log k) | O(n + k) | ✅ When k << n (k very small) |
| Max Heap | O(n log n) | O(n) | ❌ Same as sorting, no advantage |
| QuickSelect | O(n) avg | O(n) | ⚠️ O(n) average but O(n²) worst |

### Why Bucket Sort Wins Here:
1. **Frequency is bounded:** Range [1, n] allows index-based access
2. **No comparisons needed:** Direct placement by frequency
3. **Natural ordering:** Traverse high→low gives sorted result
4. **Early termination:** Stop at k elements, don't process rest
5. **Simple implementation:** No complex data structures needed 

---

## 🎓 Key Learnings

### What I Learned
1. **Frequency as Index Technique:** When values are bounded, use them as array indices for O(1) access
2. **Bucket Sort Application:** Not just for sorting numbers, works great for "top k" problems
3. **Array Size Matters:** Must be n+1 to handle maximum frequency = n (all elements same)
4. **Traversal Direction:** High→low frequency naturally gives most frequent first
5. **Off-by-One Prevention:** 
   - Loop: `i <= nums.length` not `i < nums.length` for initialization
   - Start: `i = nums.length` not `nums.length - 1` for collection
   - Condition: `i >= 0` not `i > 0` to include bucket[0]

### Mistakes I Made
1. **❌ Wrong Array Size:** Initially used `new List[nums.length]` instead of `nums.length + 1`
   - **Why wrong:** Can't store frequency = n
   - **Impact:** `ArrayIndexOutOfBoundsException`
   - **Lesson:** When max_value = n, array needs size n+1

2. **❌ Double Increment:** Used `j++, j++` in inner loop
   - **Why wrong:** Comma operator increments twice, skipping elements
   - **Impact:** Only processed every other element
   - **Lesson:** Be careful with comma operator in for loops

3. **❌ Forgot Counter Increment:** Didn't increment `count` when adding to result
   - **Why wrong:** Kept overwriting result[0]
   - **Impact:** Only first element stored
   - **Lesson:** Always increment index/counter when filling arrays

4. **❌ Wrong Loop Start:** Started from `nums.length - 1` instead of `nums.length`
   - **Why wrong:** Skipped the highest frequency bucket
   - **Impact:** Failed test cases with max frequency
   - **Lesson:** When array is [0..n], traverse [n..0] not [n-1..0]

5. **❌ Initially Thought LinkedHashMap Ordering Mattered:** 
   - **Why wrong:** Insertion order doesn't help with frequency ordering
   - **Lesson:** HashMap is fine; we use buckets for ordering, not map

### Pattern Insights

**When to use Top K Elements pattern:**
- ✅ Problem asks for "top k", "k largest", "k smallest", "k most/least frequent"
- ✅ Don't need full sorting, just k elements
- ✅ k is much smaller than n (k << n)
- ✅ Have a clear ranking criterion (frequency, value, distance, etc.)
- ✅ Output order doesn't matter

**When NOT to use this pattern:**
- ❌ Need all elements sorted (use sorting instead)
- ❌ k equals n (just return/process all elements)
- ❌ Need exact kth element only (use QuickSelect)
- ❌ Need streaming/online algorithm (different approach)

**Top K Pattern Variations:**
- **Heap approach:** O(n log k) - better when k is very small
- **Bucket Sort:** O(n) - best when metric is bounded (like frequency)
- **QuickSelect:** O(n) average - for kth element, not top k
- **Sorting:** O(n log n) - simplest but not optimal

**Related Patterns:**
- Two Heaps (for median finding)
- K-way Merge (for merging k sorted structures)
- Binary Search (for kth in sorted/rotated arrays)

---

## 🔗 Similar Problems

### Same Pattern (Top K Elements)

**Easy:**
1. [LC 347 • Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - This problem! ✅
2. [LC 692 • Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) - Similar but with strings
3. [LC 414 • Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) - Find kth largest (k=3)

**Medium:**
4. [LC 973 • K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Top k by distance
5. [LC 215 • Kth Largest Element in Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Single kth element
6. [LC 658 • Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) - k closest to target
7. [LC 767 • Reorganize String](https://leetcode.com/problems/reorganize-string/) - Uses frequency + heap

**Hard:**
8. [LC 23 • Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - K-way merge pattern
9. [LC 295 • Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) - Two heaps

### Related Concepts

**Frequency Counting:**
- [LC 451 • Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
- [LC 1636 • Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/)

**Bucket Sort Technique:**
- [LC 164 • Maximum Gap](https://leetcode.com/problems/maximum-gap/) - Bucket sort application
- [LC 220 • Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) - Bucketing by value range

**Heap/Priority Queue:**
- [LC 703 • Kth Largest Element in Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [LC 378 • Kth Smallest Element in Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) 

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#top-k-elements)
- LeetCode Discussion: https://leetcode.com/problems/top-k-frequent-elements/discuss/

---

## 🎯 Quick Reference Card

**Pattern:** Top K Elements (Bucket Sort)

**Key Insight:** When metric is bounded [0, n], use it as array index for O(1) access

**Template:**
```java
// 1. Count frequencies
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}

// 2. Create buckets (size = max_metric + 1)
List<Integer>[] buckets = new List[nums.length + 1];
for (int i = 0; i <= nums.length; i++) {
    buckets[i] = new ArrayList<>();
}

// 3. Fill buckets using metric as index
for (int key : freq.keySet()) {
    buckets[freq.get(key)].add(key);
}

// 4. Collect top k from high to low
int[] result = new int[k];
int count = 0;
for (int i = nums.length; i >= 0 && count < k; i--) {
    for (int num : buckets[i]) {
        result[count++] = num;
        if (count == k) return result;
    }
}
```

**Time:** O(n) | **Space:** O(n)

**Remember:** 
- ⚠️ Array size = max + 1 (not max)
- ⚠️ Traverse high → low for top k
- ⚠️ Use List[] not int[] for buckets (multiple elements per frequency)
- ✅ Works when metric is bounded and small range

**When to Use:**
- Top k by frequency, rank, or bounded metric
- k << n (k much smaller than n)
- Don't need full sort

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
**Date Completed:** 2025-11-29  
**Time Spent:** ~1.5 hours (learning + debugging + documentation)
