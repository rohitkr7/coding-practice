# 3 - Valid Anagram

**Jira Ticket:** [LND-27](https://rohitroy007.atlassian.net/browse/LND-27)  
**LeetCode:** https://leetcode.com/problems/valid-anagram  
**Pattern:** Hash Table / Frequency Counter  
**Difficulty:** Easy  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Easy  
**Created:** 2025-08-21  
**Last Updated:** 2025-11-24

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/valid-anagram
Problem Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
Difficulty: Medium
Category: Array

---

## 🤔 Initial Thoughts

### Understanding the Problem
- **Goal:** Determine if two strings are anagrams (same characters with same frequencies)
- **Input:** Two strings `s` and `t` containing lowercase English letters
- **Output:** Boolean - true if anagram, false otherwise
- **Key Constraint:** Must use all original letters exactly once

### Pattern Recognition
**Why Hash Table / Frequency Counter?**
- Need to count character occurrences
- Order doesn't matter, only frequencies
- Need fast lookup and comparison
- Perfect use case for frequency counting

**What clues in the problem point to this pattern?**
- "Rearranging letters" → order doesn't matter
- "Same letters exactly once" → need to track counts
- Comparing two collections → frequency map comparison
- "Lowercase English letters" → fixed size (26) allows array optimization 

---

## 💡 Approach

### Approach 1: Sorting
**Idea:**
- If two strings are anagrams, sorting them will produce identical results
- Sort both strings and compare

**Algorithm:**
1. Sort string `s`
2. Sort string `t`
3. Compare sorted strings

**Time Complexity:** O(n log n) - sorting dominates  
**Space Complexity:** O(n) - for character arrays  
**Pros:** Simple, easy to understand  
**Cons:** Not optimal time complexity

---

### Approach 2: Frequency Counter with HashMap
**Idea:**
- Count frequency of each character in both strings
- Compare the frequency maps

**Algorithm:**
1. Build frequency map for string `s`
2. Build frequency map for string `t`
3. Compare both maps

**Time Complexity:** O(n)  
**Space Complexity:** O(k) where k = unique characters (up to 26 for lowercase)  
**Pros:** Better time complexity  
**Cons:** Uses more space than needed for fixed character set

---

### Approach 3: Optimized Frequency Array (IMPLEMENTED) ✅
**Idea:**
- Use fixed-size array for lowercase letters (26 characters)
- Count characters from `s` by incrementing
- Validate characters from `t` by checking availability before decrementing
- Early exit if any character unavailable

**Algorithm Steps:**
1. **Early exit check:** If lengths differ, return false immediately
2. **Build frequency map:** Iterate through `s` and increment counts in array
3. **Validate and consume:** For each character in `t`:
   - Check if count is 0 (character unavailable)
   - If unavailable, return false (not an anagram)
   - Otherwise, decrement the count
4. **Success:** If all characters validated, return true

**Key Insight:** By checking `freqMap[c - 'a'] == 0` before decrementing, we catch both:
- Characters that don't exist in `s`
- Characters that have been used up

**Time Complexity:** O(n) - two passes through strings  
**Space Complexity:** O(1) - fixed array of 26 integers  
**Pros:** Optimal time and space, no extra validation loop needed  
**Cons:** Only works for fixed character sets

---

## 🎨 Visual Explanation

### Example 1: Valid Anagram
**Input:** `s = "anagram"`, `t = "nagaram"`

```
Step 1: Length Check
s.length = 7, t.length = 7 ✅ Continue

Step 2: Build Frequency Map from 's'
Processing "anagram":
  Index: a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
  
  'a' → freqMap[0]++  →  [1, 0, 0, 0, 0, 0, 0, ...]
  'n' → freqMap[13]++ →  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ...]
  'a' → freqMap[0]++  →  [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ...]
  'g' → freqMap[6]++  →  [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, ...]
  'r' → freqMap[17]++ →  [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, ...]
  'a' → freqMap[0]++  →  [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, ...]
  'm' → freqMap[12]++ →  [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, ...]

Final freqMap after 's':
  a=3, n=1, g=1, r=1, m=1, (rest=0)

Step 3: Validate and Consume from 't'
Processing "nagaram":
  
  'n' → freqMap[13] = 1 (✅ available) → decrement → [3, 0, ..., 0, ...]
  'a' → freqMap[0] = 3  (✅ available) → decrement → [2, 0, ..., 0, ...]
  'g' → freqMap[6] = 1  (✅ available) → decrement → [2, 0, ..., 0, ...]
  'a' → freqMap[0] = 2  (✅ available) → decrement → [1, 0, ..., 0, ...]
  'r' → freqMap[17] = 1 (✅ available) → decrement → [1, 0, ..., 0, ...]
  'a' → freqMap[0] = 1  (✅ available) → decrement → [0, 0, ..., 0, ...]
  'm' → freqMap[12] = 1 (✅ available) → decrement → [0, 0, ..., 0, ...]

Step 4: Result
All characters validated successfully!
Return: true ✅
```

---

### Example 2: Not an Anagram
**Input:** `s = "rat"`, `t = "car"`

```
Step 1: Length Check
s.length = 3, t.length = 3 ✅ Continue

Step 2: Build Frequency Map from 's'
Processing "rat":
  'r' → freqMap[17]++ → [0, ..., 1, ...]
  'a' → freqMap[0]++  → [1, ..., 1, ...]
  't' → freqMap[19]++ → [1, ..., 1, 0, 1, ...]

Final freqMap after 's':
  a=1, r=1, t=1, (rest=0)

Step 3: Validate and Consume from 't'
Processing "car":
  
  'c' → freqMap[2] = 0 (❌ NOT available!)
        ↓
        Character 'c' doesn't exist in "rat"
        Return: false immediately ❌

Early exit - no need to process further!
```

---

### Example 3: Different Frequencies
**Input:** `s = "abc"`, `t = "aab"`

```
Step 1: Length Check
s.length = 3, t.length = 3 ✅ Continue

Step 2: Build Frequency Map from 's'
Processing "abc":
  freqMap: a=1, b=1, c=1

Step 3: Validate and Consume from 't'
Processing "aab":
  
  'a' → freqMap[0] = 1 (✅ available) → decrement → a=0, b=1, c=1
  'a' → freqMap[0] = 0 (❌ NOT available!)
        ↓
        Already used up the only 'a' from "abc"
        Return: false immediately ❌
```

---

### Why This Algorithm Works

**Key Invariant:**
```
If |s| = |t| AND every character in t finds a match in s,
then every character in s has been used exactly once.
→ Perfect anagram! No leftover or missing characters possible.
```

**Mathematical Proof:**
- Total characters in s = n
- Total characters in t = n (same length)
- Each character in t consumes exactly 1 from freqMap
- If all n characters successfully consume → all n from s are used
- No characters left unused, no characters over-used
- ∴ They are anagrams!

---

## 💻 Implementation

### Java Solution (Optimized with Comments)

```java
class Solution {
    /**
     * Determines if two strings are anagrams using frequency counting.
     * 
     * An anagram means both strings contain the same characters with
     * the same frequencies, just in different order.
     * 
     * Approach: Use a fixed-size array to count character frequencies.
     * - Build frequency map from first string
     * - Validate availability while processing second string
     * - Early exit on any mismatch
     * 
     * @param s First string (lowercase English letters only)
     * @param t Second string (lowercase English letters only)
     * @return true if t is an anagram of s, false otherwise
     * 
     * Time Complexity: O(n) where n is the length of strings
     * Space Complexity: O(1) - fixed array of 26 integers
     */
    public boolean isAnagram(String s, String t) {
        // Frequency array for 26 lowercase English letters
        // Index 0 = 'a', Index 1 = 'b', ..., Index 25 = 'z'
        int[] freqMap = new int[26];
        
        // Early exit: anagrams must have the same length
        // This optimization prevents unnecessary processing
        if (s.length() != t.length()) {
            return false;
        }
        
        // Step 1: Build frequency map from string s
        // Increment count for each character in s
        for (char c : s.toCharArray()) {
            // Convert character to array index: 'a'->0, 'b'->1, etc.
            freqMap[c - 'a'] += 1;
        }
        
        // Step 2: Validate and consume from string t
        // Check availability BEFORE decrementing (key optimization!)
        for (char c : t.toCharArray()) {
            // Check if character is available
            // freqMap[c - 'a'] == 0 means either:
            //   1. This character doesn't exist in s, OR
            //   2. We've already used all occurrences of this character
            if (freqMap[c - 'a'] == 0) {
                return false;  // Not an anagram!
            }
            
            // Character is available, consume it
            freqMap[c - 'a'] -= 1;
        }
        
        // Step 3: Success!
        // If we reach here, all characters in t found matches in s
        // Combined with same-length check, this guarantees anagram
        return true;
    }
}
```

---

### Alternative Implementation: Using HashMap

```java
class Solution {
    /**
     * Alternative approach using HashMap (more flexible for Unicode)
     */
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> freqMap = new HashMap<>();
        
        // Count characters in s
        for (char c : s.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }
        
        // Validate and consume from t
        for (char c : t.toCharArray()) {
            int count = freqMap.getOrDefault(c, 0);
            if (count == 0) {
                return false;
            }
            freqMap.put(c, count - 1);
        }
        
        return true;
    }
}
```
**Note:** HashMap approach is O(1) space for fixed character sets (26 letters), but O(n) for Unicode characters.

---

### Alternative Implementation: Sorting

```java
class Solution {
    /**
     * Simplest approach using sorting
     * Trade time complexity for code simplicity
     */
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        // Convert to char arrays and sort
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        // Compare sorted arrays
        return Arrays.equals(sArray, tArray);
    }
}
```
**Time:** O(n log n), **Space:** O(n)  
**Pros:** Very simple and readable  
**Cons:** Not optimal for large inputs

---

### Key Implementation Details

#### 1. Character to Index Mapping
```java
freqMap[c - 'a']
```
- ASCII value of 'a' = 97
- ASCII value of 'c' = 99
- `'c' - 'a'` = 99 - 97 = 2 (index for 'c')
- This maps 'a'-'z' to indices 0-25

#### 2. Check Before Decrement (Critical!)
```java
if (freqMap[c - 'a'] == 0) {  // Check FIRST
    return false;
}
freqMap[c - 'a'] -= 1;  // Then modify
```
**Why this order matters:**
- Checking before prevents negative values
- Catches both "doesn't exist" and "already used up" cases
- Eliminates need for a third validation loop

#### 3. Early Exit Optimization
```java
if (s.length() != t.length()) {
    return false;
}
```
- Simple check before expensive operations
- Saves O(n) time for mismatched lengths
- Always validate cheap constraints first!

---

### Code Explanation by Section

**Lines 1-5: Method Setup**
- Fixed-size array for lowercase letters
- O(1) space complexity

**Lines 7-10: Early Exit**
- Anagrams must have equal length
- Quick rejection for invalid inputs

**Lines 12-16: Build Frequency Map**
- Single pass through string s
- Increment count for each character
- O(n) time complexity

**Lines 18-28: Validate and Consume**
- Single pass through string t
- Check availability before consuming
- Early exit on first mismatch
- O(n) time complexity

**Line 30: Success**
- All validations passed
- Guaranteed anagram by invariant 

---

## 🧪 Test Cases

### Test Case 1: Basic Valid Anagram
```
Input: s = "anagram", t = "nagaram"
Expected Output: true
Actual Output: true ✅
Explanation: Both strings contain same characters with same frequencies:
  a=3, n=1, g=1, r=1, m=1
Status: PASSED
```

### Test Case 2: Basic Invalid Anagram
```
Input: s = "rat", t = "car"
Expected Output: false
Actual Output: false ✅
Explanation: Different characters - 't' vs 'c'
Tests: Character mismatch detection
Status: PASSED
```

### Test Case 3: Different Lengths
```
Input: s = "a", t = "ab"
Expected Output: false
Actual Output: false ✅
Explanation: Different lengths (1 vs 2)
Tests: Early exit optimization
Status: PASSED
```

### Test Case 4: Empty Strings
```
Input: s = "", t = ""
Expected Output: true
Actual Output: true ✅
Explanation: Two empty strings are anagrams (vacuously true)
Tests: Edge case - minimum input
Status: PASSED
```

### Test Case 5: Single Character Match
```
Input: s = "a", t = "a"
Expected Output: true
Actual Output: true ✅
Explanation: Identical single characters
Tests: Minimum valid input
Status: PASSED
```

### Test Case 6: Single Character Mismatch
```
Input: s = "a", t = "b"
Expected Output: false
Actual Output: false ✅
Explanation: Different single characters
Tests: Minimum invalid input
Status: PASSED
```

### Test Case 7: Same Length, Different Frequencies
```
Input: s = "aab", t = "aba"
Expected Output: true
Actual Output: true ✅
Explanation: Same characters with same frequencies (a=2, b=1)
Tests: Frequency matching with duplicates
Status: PASSED
```

### Test Case 8: Same Length, Wrong Frequencies
```
Input: s = "abc", t = "aab"
Expected Output: false
Actual Output: false ✅
Explanation: Different frequencies (s has 'c', t has extra 'a')
Tests: Catches frequency mismatch
Status: PASSED
```

### Test Case 9: All Same Characters
```
Input: s = "aaaa", t = "aaaa"
Expected Output: true
Actual Output: true ✅
Explanation: Identical strings with repeating characters
Tests: Duplicate character handling
Status: PASSED
```

### Test Case 10: All Different Characters
```
Input: s = "abcdefghij", t = "jihgfedcba"
Expected Output: true
Actual Output: true ✅
Explanation: All unique characters, just reordered
Tests: Handles maximum unique characters well
Status: PASSED
```

### Test Case 11: Maximum Length (Performance Test)
```
Input: s = "a" * 50000, t = "a" * 50000
Expected Output: true
Actual Output: true ✅
Explanation: Maximum constraint (5 * 10^4 characters)
Tests: Performance at upper bound
Status: PASSED
```

### Test Case 12: Long String Not Anagram
```
Input: s = "a" * 25000 + "b" * 25000, t = "a" * 50000
Expected Output: false
Actual Output: false ✅
Explanation: Same length but different character distribution
Tests: Early detection in long strings
Status: PASSED
```

---

### Edge Cases Summary

| Category | Test Cases | Purpose |
|----------|------------|----------|
| **Empty/Minimal** | Empty strings, single char | Boundary conditions |
| **Length Mismatch** | Different lengths | Early exit validation |
| **Character Mismatch** | Different chars | Character validation |
| **Frequency Mismatch** | Same chars, wrong counts | Frequency validation |
| **Duplicates** | Repeated characters | Frequency counting accuracy |
| **Performance** | Maximum length strings | Scalability testing |
| **All Unique** | No duplicate chars | Sparse frequency map |
| **All Same** | Single char repeated | Dense frequency map |

---

## 📊 Complexity Analysis

### Time Complexity: O(n)
**Breakdown:**
```
Operation                    | Time      | Count
-----------------------------|-----------|-------
Length comparison            | O(1)      | 1 time
Iterate through string s     | O(n)      | n characters
  └─ Array access & increment | O(1)      | per character
Iterate through string t     | O(n)      | n characters
  └─ Array access & check     | O(1)      | per character
  └─ Array decrement          | O(1)      | per character
-----------------------------|-----------|-------
Total                        | O(1 + n + n) = O(n)
```

**Detailed Analysis:**
- **Best Case:** O(n) - Even if strings are anagrams, we check all characters
- **Average Case:** O(n) - Same as best case
- **Worst Case:** O(n) - In case of early exit, we might process less than n, but still O(n)

**Why O(n) and not O(2n)?**
- We make two passes: one through `s` (n chars) and one through `t` (n chars)
- O(n + n) = O(2n) = O(n) - constants are dropped in Big O notation

---

### Space Complexity: O(1)
**Breakdown:**
```
Data Structure               | Size      | Scales with Input?
-----------------------------|-----------|-------------------
int[] freqMap                | 26 ints   | No (fixed size)
Loop variable 'c'            | 1 char    | No (reused)
Method parameters (s, t)     | n chars   | Yes (but input, doesn't count)
-----------------------------|-----------|-------------------
Auxiliary Space              | O(26 + 1) = O(1)
```

**Important Note on Auxiliary vs Total Space:**
- **Auxiliary Space:** O(1) - only the `freqMap` array (26 integers) regardless of input size
- **Total Space:** Technically O(n) if counting `toCharArray()` temporary arrays, but these are just for iteration
- **In interviews, we report:** O(1) auxiliary space ✅

**Why O(1)?**
- The `int[26]` array size is **constant** (always 26 for lowercase letters)
- It doesn't grow with input size (n = 10 or n = 50,000, still 26 integers)
- Constants are expressed as O(1) in Big O notation

---

### Comparison with Alternative Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Frequency Array (Ours)** | O(n) | O(1) | Fastest, optimal space | Only works for fixed char sets |
| **HashMap** | O(n) | O(1) for lowercase, O(n) for Unicode | Flexible for any characters | Slightly more overhead |
| **Sorting** | O(n log n) | O(n) | Very simple code | Slower than O(n) |
| **Brute Force (count each)** | O(n²) | O(1) | No extra structure | Too slow, impractical |

**Our solution is optimal** for the given constraints (lowercase English letters)! 🎯

---

## 🎓 Key Learnings

### What I Learned

1. **Frequency Counter Pattern Recognition**
   - Problems involving "count occurrences" or "same frequencies" often use frequency counters
   - Order doesn't matter → strong signal for frequency-based approach
   - Pattern signature: comparing character/element distributions

2. **Array vs HashMap Trade-offs**
   - For fixed character sets (26 letters, 52 with case, 128 ASCII), arrays are faster and use O(1) space
   - For dynamic or large character sets (Unicode), HashMap is more appropriate
   - Arrays: Direct indexing O(1), no hashing overhead, cache-friendly
   - HashMap: Flexible but has hashing overhead and potential collisions

3. **Character Arithmetic (`c - 'a'`)**
   - Converting characters to indices is a powerful technique
   - Works for any contiguous range: 'a'-'z' (26), 'A'-'Z' (26), '0'-'9' (10)
   - Formula: `index = currentChar - firstChar`
   - Example: 'm' - 'a' = 109 - 97 = 12

4. **Check Before Modify Pattern**
   - Checking `freqMap[c - 'a'] == 0` BEFORE decrementing is crucial
   - Catches both "doesn't exist" and "already used up" cases
   - Eliminates need for a third validation loop
   - This optimization reduced algorithm from 3 loops to 2 loops

5. **Early Exit Optimizations**
   - Always check cheapest constraints first (length comparison is O(1))
   - Can save significant time: if lengths differ, no need to process characters
   - Exit as soon as a violation is detected (fail-fast principle)

6. **Mathematical Invariants**
   - Understanding WHY an algorithm works helps optimize it
   - Invariant: "Same length + all chars in t match s → perfect anagram"
   - This mathematical reasoning eliminated the need for checking leftover characters

7. **Auxiliary vs Total Space Complexity**
   - Auxiliary space = extra space beyond input/output
   - Total space = all space including input
   - In interviews, usually discuss auxiliary space
   - Important to clarify with interviewer which one they want

---

### Mistakes I Made

1. **Initial Bug: Wrong Final Check**
   - **Mistake:** First checked only `if (val < 0)` in validation loop
   - **Problem:** Missed case where characters remain unused (e.g., s="abc", t="aab")
   - **Lesson:** When using bidirectional operations (increment AND decrement), validate both directions
   - **Fix:** Check `if (val != 0)` OR better yet, check before decrementing

2. **Pattern Misidentification**
   - **Mistake:** Problem file initially labeled this as "Two Pointers" pattern
   - **Reality:** This is a "Frequency Counter / Hash Table" pattern
   - **Lesson:** Don't rely on labels—analyze the problem requirements
   - **Key difference:** Two Pointers needs positional relationships; this needs frequency comparison

3. **Overcomplicated First Approach**
   - **Initial thought:** Maybe need two separate frequency maps and compare them
   - **Optimization:** Single map with increment/decrement is more elegant
   - **Lesson:** Look for ways to combine operations rather than duplicate work

---

### Pattern Insights

**When to Use Frequency Counter Pattern:**
- ✅ Need to count occurrences of elements
- ✅ Order doesn't matter, only counts/frequencies
- ✅ Comparing distributions between two collections
- ✅ Questions about "same elements" or "permutation"
- ✅ Fixed or small character/element set (arrays work great)
- ✅ Keywords: "anagram", "permutation", "frequency", "count"

**When NOT to Use This Pattern:**
- ❌ Order or sequence matters (use sliding window, two pointers)
- ❌ Need to find relationships between positions (use two pointers)
- ❌ Need to track indices or ranges (use hash map with indices)
- ❌ Need sorted order (use sorting or heap)
- ❌ Need to find subsequences (use DP or two pointers)

**Pattern Variations:**
- **Single frequency map:** Count and validate in one map (our approach)
- **Two frequency maps:** Build two maps and compare (simpler but less efficient)
- **Sliding window + frequency:** For substring problems (anagram in string)
- **Frequency with sorting:** When grouping anagrams (sort as key)

**Related Patterns:**
- Hash Table for fast lookups
- Sliding Window for substrings
- Two Pointers for ordered/sorted data

---

## 🔗 Similar Problems

### Easy Level (Start Here)
1. **Contains Duplicate** (LeetCode 217)
   - Pattern: Hash Table
   - Same concept: Frequency checking
   - Simpler: Just need to detect, not compare

2. **Ransom Note** (LeetCode 383)
   - Pattern: Frequency Counter
   - Very similar: Check if one string's chars can build another
   - Same technique: Count availability and consume

3. **Word Pattern** (LeetCode 290)
   - Pattern: Hash Table mapping
   - Similar: Character/word mapping validation
   - Twist: Bidirectional mapping needed

---

### Medium Level (Next Challenge)
4. **Group Anagrams** (LeetCode 49) ⭐ **Highly Recommended Next**
   - Pattern: Frequency Counter + Hash Table
   - Extension: Group multiple anagrams together
   - Key insight: Use sorted string or frequency array as hash key

5. **Find All Anagrams in a String** (LeetCode 438) ⭐ **Great Practice**
   - Pattern: Sliding Window + Frequency Counter
   - Combines: This problem + sliding window technique
   - Challenge: Find all anagram substrings efficiently

6. **Permutation in String** (LeetCode 567)
   - Pattern: Sliding Window + Frequency Counter
   - Very similar to Find All Anagrams
   - Focus: Check if permutation exists as substring

7. **Longest Repeating Character Replacement** (LeetCode 424)
   - Pattern: Sliding Window + Frequency Counter
   - Advanced: Frequency counting with optimization

---

### Hard Level (Future Goals)
8. **Minimum Window Substring** (LeetCode 76)
   - Pattern: Sliding Window + Frequency Counter
   - Advanced version of anagram detection
   - Challenge: Find minimum window containing all characters

9. **Substring with Concatenation of All Words** (LeetCode 30)
   - Pattern: Sliding Window + Frequency Counter
   - Complex: Multiple words, exact concatenation

---

### By Pattern Family

**Frequency Counter Core:**
- Valid Anagram (this problem) ✅
- Ransom Note
- Group Anagrams

**Frequency + Sliding Window:**
- Find All Anagrams in a String
- Permutation in String
- Minimum Window Substring

**Frequency + Sorting:**
- Top K Frequent Elements (LeetCode 347)
- Sort Characters By Frequency (LeetCode 451)

---

## 🎯 Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║           VALID ANAGRAM - QUICK REFERENCE                   ║
╠══════════════════════════════════════════════════════════════╣
║ Pattern: Frequency Counter / Hash Table                     ║
║ Difficulty: Easy                                             ║
║ Time: O(n) | Space: O(1)                                     ║
╠══════════════════════════════════════════════════════════════╣
║ KEY INSIGHT:                                                 ║
║ Anagrams = Same characters with same frequencies            ║
║ Use array for fixed charset (faster than HashMap)           ║
║ Check availability BEFORE consuming (eliminates 3rd loop)   ║
╠══════════════════════════════════════════════════════════════╣
║ ALGORITHM TEMPLATE:                                          ║
║                                                              ║
║ 1. Early exit: if (s.length != t.length) return false       ║
║ 2. Build frequency: for char in s → freqMap[char]++         ║
║ 3. Validate & consume:                                       ║
║      for char in t:                                          ║
║        if freqMap[char] == 0 → return false                 ║
║        freqMap[char]--                                       ║
║ 4. Return true                                               ║
╠══════════════════════════════════════════════════════════════╣
║ CRITICAL CODE PATTERNS:                                      ║
║                                                              ║
║ • Character to index: freqMap[c - 'a']                      ║
║ • Check before modify: if (count == 0) before decrement     ║
║ • Fixed array size: int[26] for lowercase letters           ║
╠══════════════════════════════════════════════════════════════╣
║ COMMON VARIATIONS:                                           ║
║                                                              ║
║ • Case-insensitive: s.toLowerCase() first                   ║
║ • With spaces: filter or include in counting                ║
║ • Unicode chars: use HashMap instead of array               ║
║ • Uppercase + lowercase: int[52] array                      ║
╠══════════════════════════════════════════════════════════════╣
║ WATCH OUT FOR:                                               ║
║                                                              ║
║ ⚠️  Different lengths → immediate false                     ║
║ ⚠️  Check BEFORE decrement, not after                       ║
║ ⚠️  Off-by-one in char arithmetic ('a' = 97)               ║
║ ⚠️  Negative counts → bug in logic                          ║
╠══════════════════════════════════════════════════════════════╣
║ RELATED PATTERNS:                                            ║
║                                                              ║
║ → Group Anagrams (use this as building block)               ║
║ → Find All Anagrams (add sliding window)                    ║
║ → Ransom Note (similar validation logic)                    ║
╠══════════════════════════════════════════════════════════════╣
║ OPTIMIZATION NOTES:                                          ║
║                                                              ║
║ • Array > HashMap for fixed charset (no hashing overhead)   ║
║ • Early exit saves O(n) operations                          ║
║ • Check-before-modify eliminates validation loop            ║
║ • Use charAt(i) instead of toCharArray() to save O(n) space ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📚 Resources

- **Pattern Guide:** [Frequency Counter Pattern](../../PATTERNS_GUIDE.md#hash-table-frequency-counter)
- **LeetCode:** https://leetcode.com/problems/valid-anagram/
- **LeetCode Discussion:** https://leetcode.com/problems/valid-anagram/discuss/
- **16 Patterns Repository:** https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews
- **Jira Ticket:** [LND-27](https://rohitroy007.atlassian.net/browse/LND-27)

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified (Frequency Counter, not Two Pointers)
- [x] Brute force solution analyzed (sorting approach)
- [x] Optimized solution implemented (frequency array)
- [x] All test cases pass (12 comprehensive tests)
- [x] Complexity analyzed (O(n) time, O(1) space)
- [x] Code reviewed and optimized (check-before-decrement)
- [x] Learnings documented
- [x] Similar problems identified
- [x] Quick reference created
- [x] Jira ticket updated (update status to Done)

---

**Status:** ✅ Completed  
**Last Updated:** 2025-11-24  
**Submission:** Accepted ✅
