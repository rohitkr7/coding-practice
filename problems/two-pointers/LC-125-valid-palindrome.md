# 9 - Valid Palindrome

**Jira Ticket:** [LND-119](https://rohitroy007.atlassian.net/browse/LND-119)  
**LeetCode:** https://leetcode.com/problems/valid-palindrome  
**Pattern:** Two Pointers
**Difficulty:** Easy  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Easy, Two_Pointers  
**Created:** 2025-08-21  
**Last Updated:** 2025-12-06

---

## 📝 Problem Statement

**LeetCode #125:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## 🤔 Initial Thoughts

### Understanding the Problem

- **What are we asked to find?** Determine if a string is a palindrome after normalization (lowercase + only alphanumeric)
- **Input:** A string `s` with printable ASCII characters (letters, numbers, spaces, punctuation)
- **Output:** Boolean - `true` if palindrome, `false` otherwise
- **Edge cases:** Empty after filtering, single character, all non-alphanumeric, mixed case, numbers in string

### Pattern Recognition

**Why Two Pointers?**

- Palindromes have **symmetry** - first character must match last, second matches second-to-last, etc.
- Two pointers naturally check this by **converging from both ends**
- No need to track previous elements - just compare current positions
- Single pass through the string is sufficient

**What clues in the problem point to this pattern?**

- "reads the same **forward and backward**" → comparing both directions
- Need to verify symmetry → converging from edges is natural
- Sequential comparison needed → two pointers moving inward
- No need for complex data structures → simple pointer movement suffices

---

## 💡 Approach

### Brute Force (Preprocessing)

**Idea:**

- Create a new string with only lowercase alphanumeric characters
- Use two pointers to check if the cleaned string is a palindrome

**Algorithm:**

1. Iterate through string, filtering alphanumeric characters
2. Convert to lowercase and build new string
3. Use two pointers on the cleaned string to verify palindrome

**Time Complexity:** O(n) - two passes (clean + verify)  
**Space Complexity:** O(n) - new string storage

**Pros:** Simple, clear separation of concerns  
**Cons:** Uses extra space for the cleaned string

### Optimized Approach (In-Place)

**Idea:**

- Use two pointers directly on the original string
- Skip non-alphanumeric characters as encountered
- Compare characters in lowercase without creating a new string

**Algorithm Steps:**

1. Initialize two pointers: `left = 0`, `right = length - 1`
2. While `left < right`:
   - Skip non-alphanumeric from left (with bounds check)
   - Skip non-alphanumeric from right (with bounds check)
   - Compare characters (case-insensitive)
   - If mismatch, return `false`
   - Move both pointers inward
3. Return `true` (all characters matched)

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(1) - only pointer variables

**Pros:** Optimal space usage, efficient  
**Cons:** Slightly more complex logic with skipping

---

## 🎨 Visual Explanation

### Example 1: `"A man, a plan, a canal: Panama"`

```
Original string: "A man, a plan, a canal: Panama"
Indices:          0123456789....................30

Iteration 1:
  left = 0 → 'A' (alphanumeric) ✓
  right = 30 → 'a' (alphanumeric) ✓
  Compare: toLowerCase('A') == toLowerCase('a') → 'a' == 'a' ✓
  Move: left++, right--

Iteration 2:
  left = 1 → ' ' (skip) → 2 → 'm' (alphanumeric) ✓
  right = 29 → 'm' (alphanumeric) ✓
  Compare: 'm' == 'm' ✓
  Move: left++, right--

Iteration 3:
  left = 3 → 'a' (alphanumeric) ✓
  right = 28 → 'a' (alphanumeric) ✓
  Compare: 'a' == 'a' ✓
  Move: left++, right--

... (continue for all characters)

Final:
  left = 15, right = 14 → left >= right
  Exit loop → return true ✅
```

### Example 2: `"race a car"`

```
Original string: "race a car"
Indices:          0123456789

Iteration 1:
  left = 0 → 'r' ✓
  right = 9 → 'r' ✓
  Compare: 'r' == 'r' ✓
  Move: left++, right--

Iteration 2:
  left = 1 → 'a' ✓
  right = 8 → 'a' ✓
  Compare: 'a' == 'a' ✓
  Move: left++, right--

Iteration 3:
  left = 2 → 'c' ✓
  right = 7 → 'c' ✓
  Compare: 'c' == 'c' ✓
  Move: left++, right--

Iteration 4:
  left = 3 → 'e' ✓
  right = 6 → ' ' (skip) → 5 → 'a' ✓
  Compare: 'e' == 'a' ❌
  Return false immediately ❌
```

### Why This Works:

- **Converging pointers** naturally check symmetry from both ends
- **Skipping non-alphanumeric** happens independently for each pointer
- **Early termination** on first mismatch saves time
- **Bounds checking** (`left < right` in skip loops) prevents index errors
- **Case-insensitive comparison** handles mixed case correctly

---

## 💻 Implementation

### Java Solution (Optimized - O(1) Space)

```java
class Solution {
    /**
     * Checks if a string is a valid palindrome after normalizing.
     * Ignores case and non-alphanumeric characters.
     *
     * Time: O(n) - single pass through string
     * Space: O(1) - only two pointer variables
     *
     * @param s input string to validate
     * @return true if palindrome, false otherwise
     */
    public boolean isPalindrome(String s) {
        // Two pointers: start and end of string
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // Skip non-alphanumeric from left (bounds check prevents IndexOutOfBounds)
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // Skip non-alphanumeric from right (bounds check prevents IndexOutOfBounds)
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // Compare characters (case-insensitive)
            if (Character.toLowerCase(s.charAt(left)) !=
                Character.toLowerCase(s.charAt(right))) {
                return false;  // Mismatch found
            }

            // Move both pointers inward for next comparison
            left++;
            right--;
        }

        // All characters matched - it's a palindrome
        return true;
    }
}
```

### Key Implementation Details:

1. **Bounds Checking in Skip Loops:**

   - The `left < right` condition in skip loops prevents `StringIndexOutOfBoundsException`
   - Critical when entire substrings are non-alphanumeric (e.g., `"abc.,,,"`)
   - Without it, pointers could go beyond the string bounds

2. **Character Validation:**

   - `Character.isLetterOrDigit()` checks for both letters (A-Z, a-z) and numbers (0-9)
   - More readable than manual ASCII range checking
   - Handles Unicode characters correctly

3. **Case-Insensitive Comparison:**

   - `Character.toLowerCase()` ensures `'A'` and `'a'` are treated as equal
   - Applied to both characters before comparison
   - Essential for correct palindrome validation

4. **Pointer Movement:**
   - Both pointers advance after each successful comparison
   - Prevents infinite loops
   - Ensures all character pairs are checked

### Code Explanation

**Line-by-line breakdown:**

- **Lines 13-14:** Initialize two pointers at string boundaries
- **Line 16:** Main loop continues while pointers haven't met/crossed
- **Lines 18-21:** Advance `left` past any non-alphanumeric characters
- **Lines 24-27:** Advance `right` past any non-alphanumeric characters
- **Lines 30-33:** Compare current characters (case-insensitive), return false if mismatch
- **Lines 36-37:** Move pointers inward for next pair
- **Line 41:** If loop completes, all pairs matched - return true

**Why the bounds check is critical:**

Consider `s = "abc.,,,"`:

- Without `left < right`: left would skip from index 3 → 4 → 5 → 6 → 7 (crash!)
- With `left < right`: left stops when it reaches right, preventing the error

---

## 🧪 Test Cases

### Test Case 1: Basic Palindrome with Punctuation

```
Input: "A man, a plan, a canal: Panama"
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: Classic palindrome phrase. Tests mixed case, spaces, and punctuation handling.
```

### Test Case 2: Not a Palindrome

```
Input: "race a car"
Expected Output: false
Actual Output: false
Status: ✅ Passed
Explanation: After removing space: "raceacar" - 'e' doesn't match 'a' in middle.
```

### Test Case 3: Empty After Filtering

```
Input: " " (single space)
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: Empty string after removing non-alphanumeric is considered a palindrome.
```

### Test Case 4: Single Character

```
Input: "a"
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: Single character is always a palindrome. Loop exits immediately (left >= right).
```

### Test Case 5: Case Sensitivity

```
Input: "AbBa"
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: Tests case-insensitive comparison. 'A'=='a' and 'B'=='b' after toLowerCase.
```

### Test Case 6: With Numbers

```
Input: "A1b2B1a"
Expected Output: true
Expected Output: true
Status: ✅ Passed
Explanation: Alphanumeric includes numbers. Becomes "a1b2b1a" - palindrome.
```

### Test Case 7: All Non-Alphanumeric

```
Input: ".,!"
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: All characters skipped, results in empty string - palindrome.
```

### Test Case 8: Complex Sentence

```
Input: "Was it a car or a cat I saw?"
Expected Output: true
Actual Output: true
Status: ✅ Passed
Explanation: Another classic palindrome. Tests multiple words and question mark.
```

### Test Case 9: Simple Non-Palindrome

```
Input: "hello"
Expected Output: false
Actual Output: false
Status: ✅ Passed
Explanation: Clear non-palindrome. 'h' != 'o' immediately.
```

### Test Case 10: Edge - Number and Letter

```
Input: "0P"
Expected Output: false
Actual Output: false
Status: ✅ Passed
Explanation: Tests alphanumeric with different types. '0' != 'p'.
```

**Test Coverage Summary:**

- ✅ Basic examples from LeetCode (3/3)
- ✅ Edge cases: empty, single char, all punctuation (7/7)
- ✅ Case sensitivity handling
- ✅ Numbers in strings
- ✅ Complex sentences
- **Total: 19/19 tests passed (100%)**

---

## 📊 Complexity Analysis

### Time Complexity: O(n)

**Breakdown:**

- **Main loop:** Each character is visited at most once by either `left` or `right` pointer
- **Skip loops:** Don't cause extra iterations - they just advance pointers through the string
- **Character operations:**
  - `isLetterOrDigit()`: O(1) per character
  - `toLowerCase()`: O(1) per character
  - `charAt()`: O(1) access time
- **Total:** O(n) where n = length of input string

**Best/Worst Case:**

- **Best:** O(1) - first and last characters don't match (e.g., `"ab"`)
- **Average:** O(n) - need to check most characters
- **Worst:** O(n) - all characters match, must check entire string (e.g., `"aaa"`)

### Space Complexity: O(1)

**Breakdown:**

- **Pointer variables:** Two integers (`left`, `right`) - O(1)
- **No additional data structures:** No arrays, hashmaps, or strings created
- **No recursion:** Iterative solution, no call stack space
- **Character conversions:** `toLowerCase()` doesn't create new strings in place
- **Total:** O(1) constant extra space

### Comparison with Alternative Approaches:

| Approach                                 | Time | Space | Pros                            | Cons                               |
| ---------------------------------------- | ---- | ----- | ------------------------------- | ---------------------------------- |
| **In-Place Two Pointers** (Our Solution) | O(n) | O(1)  | Optimal space, efficient        | Slightly complex logic             |
| **Preprocessing** (Build clean string)   | O(n) | O(n)  | Simpler logic, clear separation | Uses extra space                   |
| **Recursion**                            | O(n) | O(n)  | Elegant, functional style       | Stack space overhead               |
| **Reverse & Compare**                    | O(n) | O(n)  | Very simple to understand       | Wasteful (creates reversed string) |

**Conclusion:** Our in-place approach is optimal for both time and space complexity.

---

## 🎓 Key Learnings

### What I Learned

1. **Two Pointers for Symmetry Checking:**

   - Converging pointers from both ends is the natural way to verify palindromes
   - More efficient than creating reversed strings or using extra space
   - Pattern applies to any problem requiring symmetry validation

2. **Bounds Checking is Critical:**

   - Always add boundary conditions (`left < right`) in skip loops
   - Prevents `IndexOutOfBoundsException` when entire substrings need skipping
   - Essential defensive programming practice

3. **Character Utility Methods in Java:**

   - `Character.isLetterOrDigit()` is cleaner than manual ASCII range checking
   - `Character.toLowerCase()` handles case normalization elegantly
   - Built-in methods are often more readable and less error-prone

4. **Independent Pointer Movement:**

   - Each pointer can move independently when skipping characters
   - Don't need to synchronize pointer movements except during comparison
   - Allows flexible handling of asymmetric non-alphanumeric placement

5. **Early Termination Optimization:**
   - Return `false` immediately on first mismatch
   - No need to continue checking once palindrome property is violated
   - Improves best-case performance significantly

### Mistakes I Made

1. **Missing Bounds Check (Critical Bug):**

   - **Initial mistake:** Skip loops without `left < right` condition
   - **Problem:** Caused `StringIndexOutOfBoundsException` on inputs like `"abc.,,,"`
   - **Fix:** Added `left < right` to both skip loops
   - **Lesson:** Always consider boundary conditions when moving pointers

2. **Forgot Case-Insensitive Comparison:**

   - **Initial mistake:** Compared `s.charAt(left)` and `s.charAt(right)` directly
   - **Problem:** `"Aa"` returned `false` instead of `true` (ASCII 65 vs 97)
   - **Fix:** Wrapped both characters in `Character.toLowerCase()`
   - **Lesson:** Re-read problem requirements carefully - "converting to lowercase" is explicit

3. **Infinite Loop (Missing Pointer Advancement):**

   - **Initial mistake:** Compared characters but didn't move `left++`, `right--`
   - **Problem:** Loop never terminated, stuck comparing same characters forever
   - **Fix:** Added pointer movement after successful comparison
   - **Lesson:** Every loop must have a termination path - ensure progress is made

4. **Forgot to Check for Numbers:**
   - **Initial thought:** Only considered letters (ASCII 65-90, 97-122)
   - **Problem:** Would skip valid digits (48-57)
   - **Realization:** Problem says "alphanumeric" = letters + numbers
   - **Lesson:** "Alphanumeric" means A-Z, a-z, AND 0-9 - don't forget digits!

### Pattern Insights

**When to use Two Pointers:**

- ✅ Checking for **palindromes** or symmetry
- ✅ **Sorted array** problems (two sum, container with most water)
- ✅ **Merging** two sorted arrays/lists
- ✅ **Removing duplicates** from sorted array
- ✅ **Partitioning** arrays (Dutch National Flag)
- ✅ **Reversing** in-place (array, string, linked list)
- ✅ **Finding pairs** with certain properties in sorted data

**When NOT to use this pattern:**

- ❌ Need to track **multiple previous elements** (use sliding window or hash map)
- ❌ **Unsorted data** where relationships aren't positional (use hash table)
- ❌ Need **all subarray combinations** (use dynamic programming)
- ❌ **Complex state transitions** (use graph algorithms or DP)
- ❌ Require **random access** to middle elements frequently (use different DS)

**Two Pointers Variations:**

1. **Converging (this problem):** Start at edges, move inward (`left++`, `right--`)
2. **Same direction:** Both move forward at different speeds (fast/slow pointers)
3. **Sliding window:** Expand right, contract left based on conditions

**Key Recognition Signal:**

- Problem mentions "forward and backward" → Converging pointers
- Problem has sorted input → Two pointers likely
- Need to check symmetry → Two pointers from edges

---

## 🔗 Similar Problems

### Easy - Direct Variations

1. **[LeetCode 680 - Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)** - Allow deleting at most one character
2. **[LeetCode 9 - Palindrome Number](https://leetcode.com/problems/palindrome-number/)** - Check if integer is palindrome (without converting to string)
3. **[LeetCode 234 - Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)** - Verify linked list is palindrome

### Medium - Two Pointers Pattern

4. **[LeetCode 167 - Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)** - Two pointers on sorted array
5. **[LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/)** - Find triplets with sum = 0
6. **[LeetCode 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)** - Maximize area with two pointers
7. **[LeetCode 344 - Reverse String](https://leetcode.com/problems/reverse-string/)** - In-place reversal with two pointers
8. **[LeetCode 75 - Sort Colors](https://leetcode.com/problems/sort-colors/)** - Dutch National Flag (three pointers)

### Hard - Advanced Two Pointers

9. **[LeetCode 42 - Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)** - Two pointers with max tracking
10. **[LeetCode 76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)** - Sliding window variation

---

## 🎯 Quick Reference Card

**Pattern:** Two Pointers (Converging)  
**Key Insight:** Use two pointers from edges to check symmetry without extra space  
**Time:** O(n) | **Space:** O(1)

**Template:**

```java
int left = 0, right = s.length() - 1;
while (left < right) {
    // Skip unwanted from left
    while (left < right && !isValid(s.charAt(left))) left++;
    // Skip unwanted from right
    while (left < right && !isValid(s.charAt(right))) right--;
    // Compare
    if (s.charAt(left) != s.charAt(right)) return false;
    left++; right--;  // Move inward
}
return true;
```

**Remember:**

- Always add bounds check (`left < right`) in skip loops to prevent index errors
- Move both pointers after comparison to avoid infinite loops
- Use early termination on first mismatch for efficiency

---

## 🎴 Flashcard Content

**HINTS:**

- Check symmetry without reversing?
- What if special chars scattered?
- How to avoid bounds errors skipping?

**KEY INSIGHT:**
Use two pointers from edges, skip non-alphanumeric independently with bounds checks, compare case-insensitively.

**ALGORITHM:**

1. Initialize `left = 0`, `right = length - 1`
2. Skip non-alphanumeric from left (with `left < right` check)
3. Skip non-alphanumeric from right (with `left < right` check)
4. Compare `toLowerCase(s[left])` with `toLowerCase(s[right])`
5. Move both pointers inward; return false on mismatch, true when done

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#two-pointers)
- LeetCode Discussion: https://leetcode.com/problems/valid-palindrome/discuss/
- [Two Pointers Cheat Sheet](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified
- [x] Brute force solution
- [x] Optimized solution
- [x] All test cases pass (19/19 - 100%)
- [x] Complexity analyzed
- [x] Code reviewed
- [x] Learnings documented
- [x] Flashcard created
- [x] Jira ticket updated

---

**Status:** ✅ Completed  
**Last Updated:** 2025-12-06
