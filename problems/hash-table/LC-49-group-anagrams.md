# 4 - Group Anagrams

**Jira Ticket:** [LND-28](https://rohitroy007.atlassian.net/browse/LND-28)  
**LeetCode:** https://leetcode.com/problems/group-anagrams  
**Pattern:** Hash Table / Array & Hashing
**Difficulty:** Medium  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-08-22

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/group-anagrams
Problem Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem
- **Input:** Array of strings
- **Output:** Grouped anagrams (list of lists)
- **Key insight:** Anagrams have the same letters with the same frequencies
- **Edge cases:** Empty string, single character, all unique, all anagrams

### Pattern Recognition
**Why Hash Table?**
- Need to **group** strings by a shared property
- Require fast O(1) lookup to check if we've seen a signature before
- Perfect use case for HashMap: signature → list of strings

**What clues in the problem point to this pattern?**
- Keyword: "group" - indicates categorization
- Need to identify equivalent items (anagrams)
- No mention of sorting or adjacency
- Hash Table excels at grouping by key

---

## 💡 Approach

### Brute Force
**Idea:**
- Compare every string with every other string to check if they're anagrams
- For each string, create a new group or find existing group

**Time Complexity:** O(n² × m) - Too slow!  
**Space Complexity:** O(n × m)

### Optimized Approach 1: Sorted String as Key
**Idea:**
- Sort each string alphabetically
- Sorted strings are identical for anagrams
- Use sorted string as HashMap key

**Algorithm Steps:**
1. Create HashMap<String, List<String>>
2. For each string: sort it, use sorted version as key
3. Add original string to the list for that key
4. Return all values from the map

**Time Complexity:** O(n × m log m)
**Space Complexity:** O(n × m)

### Optimized Approach 2: Character Frequency as Key ⭐ (Best!)
**Idea:**
- Count frequency of each character (a-z)
- Convert frequency array to a unique string key
- Anagrams have identical frequency patterns

**Algorithm Steps:**
1. Create HashMap<String, List<String>>
2. For each string:
   - Count character frequencies in int[26]
   - Convert frequency array to string key using StringBuilder
   - Add string to the list for that key
3. Return all values from the map

**Time Complexity:** O(n × m) ⚡ Optimal!
**Space Complexity:** O(n × m)

---

## 🎨 Visual Explanation

### Example: ["eat","tea","tan","ate","nat","bat"]

```
Initial State:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
HashMap: {}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Process "eat"
  Character frequencies:
  a=1, b=0, c=0, d=0, e=1, f=0, g=0, h=0, i=0, j=0, k=0, l=0, m=0,
  n=0, o=0, p=0, q=0, r=0, s=0, t=1, u=0, v=0, w=0, x=0, y=0, z=0
  
  Key generated: "#1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0"
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat"]
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 2: Process "tea"
  Character frequencies:
  a=1, e=1, t=1 (same as "eat"!)
  
  Key generated: "#1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0"
  ⭐ Same key as "eat"!
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat", "tea"]  ← Grouped!
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 3: Process "tan"
  Character frequencies:
  a=1, n=1, t=1 (different pattern!)
  
  Key generated: "#1#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#1#0#0#0#0#0#0"
  ⭐ New key!
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat", "tea"],
    "#1#0#0#0#0#...#1#...#1#0": ["tan"]
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 4: Process "ate"
  Character frequencies:
  a=1, e=1, t=1 (same as "eat" and "tea"!)
  
  Key: "#1#0#0#0#1#...#1#0" ← Matches "eat" group
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat", "tea", "ate"],
    "#1#0#0#0#0#...#1#...#1#0": ["tan"]
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 5: Process "nat"
  Character frequencies:
  a=1, n=1, t=1 (same as "tan"!)
  
  Key: "#1#0#0#0#0#...#1#...#1#0" ← Matches "tan" group
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat", "tea", "ate"],
    "#1#0#0#0#0#...#1#...#1#0": ["tan", "nat"]
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 6: Process "bat"
  Character frequencies:
  a=1, b=1, t=1 (new pattern!)
  
  Key: "#1#1#0#0#0#...#1#0" ← New key!
  
  HashMap: {
    "#1#0#0#0#1#...#1#0": ["eat", "tea", "ate"],
    "#1#0#0#0#0#...#1#...#1#0": ["tan", "nat"],
    "#1#1#0#0#0#...#1#0": ["bat"]
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final Result:
Return all values from HashMap:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
```

### Why This Works:
- ✅ Anagrams have **identical character frequencies**
- ✅ Frequency array creates a **unique signature** for each anagram group
- ✅ HashMap provides **O(1) lookup** to find or create groups
- ✅ StringBuilder creates **efficient string keys** from frequency arrays

---

## 💻 Implementation

### Java Solution (Optimized with Character Frequency)

```java
import java.util.*;

class Solution {
    /**
     * Groups anagrams from an array of strings.
     * 
     * Approach: Use character frequency as HashMap key
     * - Count frequency of each character (a-z) in each string
     * - Convert frequency array to unique string key
     * - Group strings with same frequency pattern
     * 
     * Time: O(n × m) where n = number of strings, m = average string length
     * Space: O(n × m) for storing all strings in HashMap
     * 
     * @param strs Array of strings to group
     * @return List of grouped anagrams
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        // HashMap to store: frequency_key -> list of anagrams
        Map<String, List<String>> map = new HashMap<>();
        
        // Process each string
        for (String str : strs) {
            // Step 1: Count character frequencies
            // Array of size 26 for lowercase letters a-z
            int[] freq = new int[26];
            
            // Count each character
            // 'a' - 'a' = 0, 'b' - 'a' = 1, ..., 'z' - 'a' = 25
            for (char c : str.toCharArray()) {
                freq[c - 'a']++;
            }
            
            // Step 2: Create unique key from frequency array
            // Using StringBuilder for efficient string building
            // Format: "#1#0#0#0#1#..." (# as delimiter, prevents collisions)
            StringBuilder keyBuilder = new StringBuilder();
            for (int count : freq) {
                keyBuilder.append('#').append(count);
            }
            String key = keyBuilder.toString();
            
            // Step 3: Add string to appropriate group
            // If key doesn't exist, create new ArrayList
            // Then add current string to the list
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(str);
            
            // Alternative one-liner (Java 8+):
            // map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
        
        // Step 4: Return all grouped anagrams
        // Convert HashMap values (lists of anagrams) to ArrayList
        return new ArrayList<>(map.values());
    }
}
```

### Key Implementation Details

1. **Character Frequency Array:**
   - Size 26 for lowercase English letters
   - Index calculation: `c - 'a'` maps 'a'→0, 'b'→1, ..., 'z'→25
   - O(1) space per string (fixed size)

2. **StringBuilder for Key Generation:**
   - Efficient string building (O(26) = O(1))
   - Delimiter `#` prevents collisions: "#1#11" ≠ "#11#1"
   - Creates unique, reproducible keys

3. **HashMap Operations:**
   - `containsKey()` + `put()` + `get()`: O(1) average
   - Groups strings with identical frequency patterns
   - Automatically handles duplicate keys

### Code Explanation

**Line-by-line breakdown:**

```java
Map<String, List<String>> map = new HashMap<>();
```
- Key: String representation of character frequencies
- Value: List of all strings with that frequency pattern

```java
int[] freq = new int[26];
```
- Array to count occurrences of each letter a-z
- Initialized to all zeros

```java
for (char c : str.toCharArray()) {
    freq[c - 'a']++;
}
```
- Convert string to character array
- For each char, increment corresponding index
- Example: 'e' → index 4, so freq[4]++

```java
StringBuilder keyBuilder = new StringBuilder();
for (int count : freq) {
    keyBuilder.append('#').append(count);
}
```
- Build key string from frequency array
- Format: "#count0#count1#count2..."
- Delimiter ensures uniqueness

```java
if (!map.containsKey(key)) {
    map.put(key, new ArrayList<>());
}
map.get(key).add(str);
```
- Check if this frequency pattern seen before
- If new, create empty list
- Add current string to the list

### Alternative Approach: Sorted String

```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String str : strs) {
        // Sort the string to create key
        char[] chars = str.toCharArray();
        Arrays.sort(chars);  // O(m log m)
        String key = new String(chars);
        
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
    }
    
    return new ArrayList<>(map.values());
}
```

**Time:** O(n × m log m) - Slower due to sorting  
**Space:** O(n × m)  
**Pros:** Simpler code, shorter keys  
**Cons:** Slower for longer strings 

---

## 🧪 Test Cases

### Test Case 1: Multiple Anagram Groups
```
Input: ["eat","tea","tan","ate","nat","bat"]
Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Actual Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Status: ✅ Passed
Explanation: Tests basic anagram grouping with 3 groups
  - "eat", "tea", "ate" all have same letters
  - "tan", "nat" form another group
  - "bat" is alone
  Order of groups and strings within groups doesn't matter
```

### Test Case 2: Empty String
```
Input: [""]
Expected Output: [[""]]
Actual Output: [[""]]
Status: ✅ Passed
Explanation: Empty string forms its own group
  - Frequency array: all zeros
  - Key: "#0#0#0...#0"
  - Edge case: empty input handled correctly
```

### Test Case 3: Single Character
```
Input: ["a"]
Expected Output: [["a"]]
Actual Output: [["a"]]
Status: ✅ Passed
Explanation: Single string forms single group
  - Simplest valid test case
  - Tests HashMap initialization
```

### Test Case 4: All Unique Strings
```
Input: ["abc","def","ghi"]
Expected Output: [["abc"],["def"],["ghi"]]
Actual Output: [["abc"],["def"],["ghi"]]
Status: ✅ Passed
Explanation: No anagrams - each string in its own group
  - Tests worst case: n groups for n strings
  - Each gets unique frequency key
```

### Test Case 5: All Same Anagrams
```
Input: ["abc","bca","cab","bac","cba","acb"]
Expected Output: [["abc","bca","cab","bac","cba","acb"]]
Actual Output: [["abc","bca","cab","bac","cba","acb"]]
Status: ✅ Passed
Explanation: All strings are anagrams - single group
  - Best case: 1 group for n strings
  - All have same frequency key: "#1#1#1#0#0...#0"
```

### Test Case 6: Different Length Strings
```
Input: ["a","ab","abc"]
Expected Output: [["a"],["ab"],["abc"]]
Actual Output: [["a"],["ab"],["abc"]]
Status: ✅ Passed
Explanation: Different lengths can't be anagrams
  - Each has unique frequency pattern
  - Tests that length difference creates different keys
```

### Test Case 7: Duplicate Strings
```
Input: ["abc","abc","abc"]
Expected Output: [["abc","abc","abc"]]
Actual Output: [["abc","abc","abc"]]
Status: ✅ Passed
Explanation: Duplicates grouped together (same letters)
  - All map to same key
  - Tests ArrayList add multiple times
```

---

## 📊 Complexity Analysis

### Time Complexity: O(n × m)
**Where:**
- n = number of strings in the input array
- m = average length of each string

**Breakdown:**
1. **Outer loop**: Iterate through all n strings → O(n)
2. **For each string**:
   - Create frequency array: O(1) - fixed size 26
   - Count characters: O(m) - scan through string
   - Build key with StringBuilder: O(26) = O(1) - fixed 26 iterations
   - HashMap put/get: O(1) average case
   - ArrayList add: O(1) amortized
3. **Return values**: O(1) - just returns reference

**Total**: O(n) × O(m) = **O(n × m)** ⭐ Optimal!

**Why this is optimal:**
- Must examine every character at least once: Ω(n × m) lower bound
- Our solution achieves this lower bound
- Cannot do better asymptotically

---

### Space Complexity: O(n × m)
**Breakdown:**
1. **HashMap storage**: O(n × m)
   - Keys: Up to n different frequency keys (worst case all unique)
   - Each key: O(1) - "#1#2#..." fixed length ~52 chars
   - Values: Lists containing all n strings
   - Total string storage: n strings × m avg length = O(n × m)

2. **Frequency array**: O(1)
   - int[26] created per iteration
   - Reused/garbage collected
   - Fixed size, not dependent on input

3. **StringBuilder**: O(1)
   - Fixed size ~52 chars for frequency key
   - Temporary, created per iteration

4. **Output list**: O(n × m)
   - Returns ArrayList of Lists
   - Contains references to all input strings
   - Not extra space (required for output)

**Total**: O(n × m) for HashMap + O(n × m) for output = **O(n × m)**

---

### Comparison with Other Approaches

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **Character Frequency (Ours)** | O(n × m) | O(n × m) | ⭐ Optimal! |
| Sorted String as Key | O(n × m log m) | O(n × m) | Slower due to sorting |
| Brute Force (compare all) | O(n² × m) | O(n × m) | Too slow! |
| Prime Number Product | O(n × m) | O(n × m) | Risk of overflow |

**Our Approach Wins Because:**
- ✅ Best time complexity: O(n × m)
- ✅ Same space as alternatives
- ✅ No risk of overflow (unlike prime product)
- ✅ Clear and maintainable code

---

### Complexity in Different Scenarios

**Best Case**: O(n × m)
- All strings are anagrams → 1 group
- Still need to process each character
- HashMap operations still O(1)

**Average Case**: O(n × m)
- Mix of anagram groups
- HashMap performance stays O(1) on average

**Worst Case**: O(n × m)
- All strings unique → n groups
- HashMap may resize, but amortized O(1)
- Still linear in total characters 

---

## 🎓 Key Learnings

### What I Learned

1. **Character Frequency as Signature**
   - Anagrams have identical character frequency patterns
   - Frequency array creates a unique, reproducible identifier
   - This signature concept applies to many grouping problems

2. **StringBuilder Optimization**
   - `Arrays.toString()` adds unnecessary overhead (brackets, spaces, commas)
   - Custom StringBuilder with delimiters is faster
   - Pre-sizing StringBuilder can improve performance further
   - Simple optimization yielded 38% speed improvement!

3. **HashMap for Grouping Pattern**
   - Perfect data structure for "group by property" problems
   - Key = shared property, Value = list of items
   - `computeIfAbsent()` elegantly handles initialization
   - Average O(1) for put/get operations

4. **Trade-offs in Algorithm Design**
   - Sorted string: simpler code, O(n × m log m)
   - Frequency count: optimal time O(n × m), slightly more complex
   - Sometimes simpler isn't always better performance-wise

5. **Index Mapping Technique**
   - `c - 'a'` maps characters to array indices
   - Works for any contiguous character range
   - Common pattern in string problems with limited character set

### Mistakes I Made

1. **Initial Performance Issue**
   - **Mistake**: Used `Arrays.toString(freq)` for key generation
   - **Impact**: Only 19.37% runtime performance
   - **Lesson**: Built-in methods may have hidden overhead
   - **Fix**: Custom StringBuilder approach → 26.77% performance

2. **Pattern Misidentification**
   - **Mistake**: Problem initially labeled as "Two Pointers"
   - **Reality**: This is a Hash Table problem
   - **Lesson**: Look for keywords - "group", "categorize" suggest HashMap
   - **Fix**: Corrected pattern classification during project reorganization

3. **Not Considering Alternatives First**
   - Initially jumped to frequency approach
   - Should have discussed sorted string approach too
   - Both are valid; understanding trade-offs is important

4. **Overlooking Delimiter Importance**
   - Almost forgot why `#` delimiter is needed
   - Without it: [1,11] and [11,1] both become "111"
   - With it: "#1#11" vs "#11#1" - unique!
   - Small details matter for correctness

### Pattern Insights

**When to use Hash Table / Grouping Pattern:**
- ✅ Keywords: "group", "categorize", "organize"
- ✅ Need to identify equivalent items by shared property
- ✅ Require fast O(1) lookup
- ✅ Output is groups/categories of items
- ✅ Items can be compared by a signature/key

**When NOT to use this pattern:**
- ❌ Need to maintain sorted order (use TreeMap or sort after)
- ❌ Need to find pairs/sequences (Two Pointers might be better)
- ❌ Memory is extremely constrained (O(n) space required)
- ❌ Need to track relative positions (indexing matters)

**Related Hash Table Patterns:**
- **Frequency Counter**: Count occurrences (Valid Anagram)
- **Fast Lookup**: Find complement/pair (Two Sum)
- **Duplicate Detection**: Check if seen before (Contains Duplicate)
- **Grouping by Property**: This problem!
- **Set Operations**: Union, intersection (Longest Consecutive Sequence)

**Hash Table Best Practices:**
- Choose efficient key representation
- Consider memory overhead of keys
- Use `computeIfAbsent()` for cleaner code
- Pre-size HashMap if you know approximate size
- Remember HashMap can have O(n) worst case (rare with good hash)

### Transferable Concepts

1. **Signature/Fingerprint Technique**: Used in many problems
   - Isomorphic Strings
   - Word Pattern
   - Find Duplicate Subtrees

2. **Character Counting**: Fundamental string technique
   - Permutation problems
   - Sliding window with character constraints
   - Substring problems

3. **HashMap Initialization Pattern**:
   ```java
   if (!map.containsKey(key)) {
       map.put(key, new ArrayList<>());
   }
   map.get(key).add(value);
   // OR
   map.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
   ```

---

## 🔗 Similar Problems

### Same Pattern (Hash Table / Grouping)

**Easy:**
1. **Valid Anagram** (LND-27) ✅ Completed
   - Same frequency counting technique
   - Foundation for this problem
   - LeetCode: https://leetcode.com/problems/valid-anagram

2. **Isomorphic Strings** (LeetCode 205)
   - Map characters between two strings
   - Use HashMap for character mapping
   - Similar grouping concept

**Medium:**
3. **Sort Characters By Frequency** (LeetCode 451)
   - Count character frequencies
   - Group by frequency, sort
   - Combines frequency counter + sorting

4. **Find All Anagrams in a String** (LeetCode 438)
   - Sliding window + frequency matching
   - Uses same anagram detection technique
   - Adds window sliding complexity

5. **Encode and Decode Strings** (LND-32)
   - Design custom encoding scheme
   - Related: creating unique string representations
   - LeetCode Premium problem

**Hard:**
6. **Substring with Concatenation of All Words** (LeetCode 30)
   - Advanced anagram/permutation matching
   - HashMap + sliding window
   - Much more complex variation

### Other Hash Table Problems in Your List

7. **Two Sum** (LND-29) ✅ Completed
   - HashMap for complement lookup
   - Different use case: finding pairs

8. **Contains Duplicate** (LND-30) ✅ Completed
   - HashSet for duplicate detection
   - Simpler: just checking existence

9. **Longest Consecutive Sequence** (LND-35) ⏳ To Do
   - HashSet for O(1) lookup
   - More advanced: sequence building
   - Next challenge in Hash Table pattern!

### Problems Using Character Frequency

10. **Minimum Window Substring** (LeetCode 76) - Hard
    - Frequency matching in sliding window
    - Advanced version of frequency counting

11. **Longest Substring Without Repeating Characters** (LeetCode 3)
    - Track character positions
    - Sliding window + HashMap

12. **Permutation in String** (LeetCode 567)
    - Check if one string is permutation of substring
    - Uses frequency matching

### Progression Path

```
You Are Here! ⭐
│
├─ Hash Table Pattern Progress: 4/5 Complete
│  ✅ Valid Anagram (Easy)
│  ✅ Two Sum (Easy) 
│  ✅ Contains Duplicate (Easy)
│  ✅ Group Anagrams (Medium) ← Current!
│  ⏳ Longest Consecutive Sequence (Medium)
│
├─ Next Steps:
│  1. Complete Longest Consecutive Sequence
│  2. Master Hash Table pattern (5/5)
│  3. Move to Two Pointers pattern
│  4. Try: Valid Palindrome (Easy)
│
└─ Advanced Challenges (After mastering basics):
   → Find All Anagrams in a String
   → Minimum Window Substring
   → Substring with Concatenation of All Words
``` 

---

## 🎯 Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║                   GROUP ANAGRAMS PATTERN                     ║
║                  Hash Table / Grouping                       ║
╠══════════════════════════════════════════════════════════════╣
║ PATTERN: Hash Table - Group by Property                     ║
║ KEY INSIGHT: Anagrams have identical character frequencies   ║
╠══════════════════════════════════════════════════════════════╣
║ TIME:  O(n × m) where n=strings, m=avg length              ║
║ SPACE: O(n × m) for HashMap storage                         ║
╠══════════════════════════════════════════════════════════════╣
║ ALGORITHM:                                                   ║
║ 1. Create HashMap<String, List<String>>                     ║
║ 2. For each string:                                          ║
║    → Count character frequencies in int[26]                  ║
║    → Convert to unique string key with StringBuilder         ║
║    → Add string to HashMap list for that key                 ║
║ 3. Return all HashMap values                                 ║
╠══════════════════════════════════════════════════════════════╣
║ TEMPLATE:                                                    ║
║   Map<String, List<String>> map = new HashMap<>();          ║
║   for (String str : strs) {                                  ║
║       int[] freq = new int[26];                              ║
║       for (char c : str.toCharArray())                       ║
║           freq[c - 'a']++;                                   ║
║       StringBuilder key = new StringBuilder();               ║
║       for (int count : freq)                                 ║
║           key.append('#').append(count);                     ║
║       map.computeIfAbsent(key.toString(),                    ║
║           k -> new ArrayList<>()).add(str);                  ║
║   }                                                          ║
║   return new ArrayList<>(map.values());                      ║
╠══════════════════════════════════════════════════════════════╣
║ KEY TECHNIQUES:                                              ║
║ • c - 'a' maps 'a'→0, 'b'→1, ..., 'z'→25                  ║
║ • StringBuilder with '#' delimiter prevents collisions       ║
║ • computeIfAbsent() for clean initialization                ║
║ • Fixed-size frequency array for O(1) counting              ║
╠══════════════════════════════════════════════════════════════╣
║ WATCH OUT FOR:                                               ║
║ ⚠ Need delimiter in key ("#1#11" ≠ "#11#1")               ║
║ ⚠ Don't use Arrays.toString() - performance overhead        ║
║ ⚠ Order in output groups doesn't matter                     ║
║ ⚠ Empty string is valid input                               ║
╠══════════════════════════════════════════════════════════════╣
║ WHEN TO USE:                                                 ║
║ ✓ Keywords: "group", "categorize", "organize"              ║
║ ✓ Need to identify equivalent items                         ║
║ ✓ Items share a common property/signature                   ║
║ ✓ Require O(1) lookup for grouping                          ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🎴 Flashcard Content

**HINTS:**
- What do anagrams have in common when sorted?
- Can sorted string be a key?
- What data structure groups things?

**KEY INSIGHT:**
Use sorted string as HashMap key - all anagrams will have the same sorted representation and map to the same key.

**ALGORITHM:**
1. Create HashMap<String, List<String>>
2. For each string: sort it
3. Use sorted string as key
4. Add original string to list at that key
5. Return all values from HashMap

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#hash-table)
- [Hash Table Problems](../hash-table/)
- LeetCode Discussion: https://leetcode.com/problems/group-anagrams/discuss/
- Jira Ticket: [LND-28](https://rohitroy007.atlassian.net/browse/LND-28)

---

## ✅ Progress Checklist

- [x] Problem understood
- [x] Pattern identified (Hash Table, not Two Pointers!)
- [x] Brute force solution considered
- [x] Optimized solution implemented
- [x] All test cases pass (7/7 ✅)
- [x] Complexity analyzed (O(n × m) time, O(n × m) space)
- [x] Code reviewed and optimized
- [x] Learnings documented
- [x] Performance improved (19% → 27%)
- [x] Solution documented with comments
- [x] Visual walkthrough created
- [x] Similar problems identified
- [x] Jira ticket updated
- [x] Weekly progress tracker updated (README.md Problem Tracker)

---

**Status:** ✅ Completed  
**Completion Date:** 2025-11-24  
**LeetCode Performance:** Runtime 17ms (26.77%), Memory 50.27MB  
**Key Achievement:** Identified and fixed performance bottleneck, achieved optimal O(n×m) time complexity
