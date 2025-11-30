# 7 - Encode and Decode Strings

**Jira Ticket:** [LND-32](https://rohitroy007.atlassian.net/browse/LND-32)  
**LeetCode:** https://leetcode.com/problems/encode-and-decode-strings
**NeetCode:** https://neetcode.io/problems/string-encode-and-decode/question
**Pattern:** String Manipulation
**Difficulty:** Medium  
**Status:** ✅ Completed  
**Priority:** Medium

**Labels:** Array_Hashing, Medium  
**Created:** 2025-08-21  
**Last Updated:** 2025-11-30

---

## 📝 Problem Statement

Problem URL: https://leetcode.com/problems/encode-and-decode-strings
Problem Description:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Example:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Note:
The string may contain any possible characters out of 256 valid ASCII characters.
Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
Difficulty: Medium
Category: Array & Hashing

---

## 🤔 Initial Thoughts

### Understanding the Problem

- **Task:** Design two functions - `encode()` to combine multiple strings into one, and `decode()` to reverse the process
- **Input (encode):** List of strings (can contain ANY ASCII characters including delimiters)
- **Output (encode):** Single encoded string
- **Input (decode):** Single encoded string
- **Output (decode):** Original list of strings
- **Key Challenge:** Strings can contain ANY character, including common delimiters like `,`, `;`, `#`, etc.
- **Edge Cases:** Empty strings `""`, empty list `[]`, delimiter characters within strings, single string

### Pattern Recognition

**Why String Manipulation with Length-Prefix Encoding?**

- The core challenge is marking boundaries between strings when any character can appear in the data
- Simple delimiter approach fails: if we use `,` as delimiter, what if a string contains `,`?
- Escape sequences work but are complex (must escape the escape character itself)
- **Length-prefix encoding** solves this elegantly: `length + delimiter + string`

**What clues in the problem point to this pattern?**

- "String may contain ANY possible characters" → rules out simple delimiters
- Need reversible encoding → suggests structured format
- Must be stateless → can't rely on external state tracking
- This is a classic serialization problem (similar to network protocols, file formats)
- ***

## 💡 Approach

### Brute Force (Delimiter-Based with Escaping)

**Idea:**

- Use a delimiter like `#` to separate strings
- Escape any occurrence of `#` in the original strings (e.g., `#` → `##`)
- Must also handle the escape sequence itself

**Algorithm:**

1. For each string, replace all `#` with `##` (escape)
2. Join strings with `#` as delimiter
3. To decode, split by single `#`, then replace `##` back to `#`

**Problems:**

- Complicated escape logic (need to escape the escape character)
- More processing overhead
- Error-prone with multiple levels of escaping

**Time Complexity:** O(n) - still need to process all characters  
**Space Complexity:** O(n) - for escaped string

### Optimized Approach: Length-Prefix Encoding ✅

**Idea:**

- Format: `length + delimiter + string` (e.g., `"abc"` → `"3#abc"`)
- When decoding, read the length first, then extract exactly that many characters
- **Key Insight:** Once we know the length, delimiters inside the string don't matter!

**Algorithm Steps:**

**Encode:**

1. Create a StringBuilder to build result
2. For each string in the list:
   - Append the string's length
   - Append a delimiter `#`
   - Append the actual string
3. Return the concatenated result

**Decode:**

1. Initialize result list and pointer `i = 0`
2. While `i < encoded_string.length`:
   - Find the next `#` delimiter (scan with pointer `j`)
   - Extract length: `substring(i, j)` and convert to integer
   - Skip the delimiter: `i = j + 1`
   - Extract exactly `length` characters: `substring(i, i + length)`
   - Add extracted string to result
   - Move pointer: `i = i + length`, reset `j = i`
3. Return result list

**Why This Works:**

- The length tells us exactly how many characters to read
- We can safely ignore any delimiters within those characters
- Simple, elegant, and used in real-world protocols (HTTP, Protocol Buffins)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 🎨 Visual Explanation

### Example Walkthrough: `["ab", "c:#d"]`

**ENCODING:**

```
Input: ["ab", "c:#d"]

Step 1: Process "ab"
  length = 2
  encoded = "2#ab"

Step 2: Process "c:#d"
  length = 4
  encoded = "2#ab4#c:#d"

Final Encoded String: "2#ab4#c:#d"
```

**DECODING:**

```
Input: "2#ab4#c:#d"

Initial State:
  i = 0, j = 0
  encoded = "2#ab4#c:#d"
             ↑
             i,j

Iteration 1:
  Find delimiter:
    j=0: '2' != '#', j++ → j=1
    j=1: '#' == '#', break!

  Extract length: substring(0, 1) = "2" → length = 2
  Skip delimiter: i = 1 + 1 = 2

  encoded = "2#ab4#c:#d"
               ↑
               i

  Extract word: substring(2, 4) = "ab"
  Result = ["ab"]
  Move pointers: i = 4, j = 4

Iteration 2:
  Find delimiter:
    j=4: '4' != '#', j++ → j=5
    j=5: '#' == '#', break!

  Extract length: substring(4, 5) = "4" → length = 4
  Skip delimiter: i = 5 + 1 = 6

  encoded = "2#ab4#c:#d"
                   ↑
                   i

  Extract word: substring(6, 10) = "c:#d"
  ⚠️ Note: The '#' and ':' inside are just characters!
  Result = ["ab", "c:#d"]
  Move pointers: i = 10, j = 10

Loop ends (j >= length)

Final Result: ["ab", "c:#d"] ✅
```

### Why This Works:

**The Magic of Length-Prefix Encoding:**

1. **Delimiter Protection:** Once we read the length (e.g., `4`), we extract exactly 4 characters
2. **Character Blindness:** During extraction, we don't care what those 4 characters are - they could be anything!
3. **No Ambiguity:** `4#c:#d` is unambiguous - read 4 chars after `#`
4. **Self-Describing:** The encoded string contains all information needed to decode

**Real-World Usage:**

- HTTP Chunked Transfer Encoding
- Protocol Buffers (protobuf)
- Network protocols (length-value pairs)
- Binary file formats

---

## 💻 Implementation

### Java Solution (Optimized with Comments)

```java
class Solution {

    /**
     * Encodes a list of strings to a single string.
     * Format: length + delimiter + string (e.g., "3#abc")
     * Time: O(n), Space: O(n) where n = total chars
     */
    public String encode(List<String> strs) {
        StringBuilder encodedSb = new StringBuilder();

        for (String str : strs) {
            // Append: length + delimiter + actual string
            encodedSb.append(str.length());
            encodedSb.append("#");  // Safe delimiter (length-prefix protects it)
            encodedSb.append(str);
        }

        return encodedSb.toString();
    }

    /**
     * Decodes a single string to a list of strings.
     * Reads length, then extracts exactly that many chars.
     * Time: O(n), Space: O(n) where n = encoded string length
     */
    public List<String> decode(String str) {
        List<String> decodedString = new ArrayList<>();

        // i: start of current segment, j: scanner for delimiter
        for (int i = 0, j = 0; j < str.length(); ) {

            // Find delimiter to extract length
            while (j < str.length()) {
                if (str.charAt(j) == '#')
                    break;
                j++;
            }

            // Parse length from [i, j)
            int wordLen = Integer.parseInt(str.substring(i, j));

            // Skip delimiter, extract exactly wordLen chars
            i = j + 1;
            String word = str.substring(i, i + wordLen);
            decodedString.add(word);

            // Move both pointers to next segment
            i = i + wordLen;
            j = i;  // ⚠️ CRITICAL: Reset j to start of next length prefix
        }

        return decodedString;
    }
}
```

### Key Implementation Details:

1. **StringBuilder for Efficiency:** String concatenation with `+` is O(n²) in Java. StringBuilder is O(n).

2. **Two-Pointer Technique in Decode:**

   - `i` marks the start of the current segment (length or string data)
   - `j` scans forward to find the delimiter
   - **Critical:** `j = i` resets the scanner after each word - this was the bug we fixed!

3. **Delimiter Choice:** Any single character works. `#` is chosen by convention, but `:`, `|`, or even a space would work identically.

4. **Why Delimiter is Safe:** The delimiter can appear inside strings because we extract based on length, not by searching for delimiters during extraction.

### Code Explanation

**Encode Function:**

- **Line 8-13:** For each string, append three things: its length, delimiter, and the string itself
- **Line 15:** StringBuilder efficiently builds the result in O(n) time

**Decode Function:**

- **Line 27-32:** Inner while loop finds the next `#` delimiter by scanning with `j`
- **Line 35:** Extract the length as an integer (handles multi-digit lengths like "12")
- **Line 38-39:** Skip delimiter and extract exactly `wordLen` characters
- **Line 43:** **Critical line!** Reset `j = i` so next iteration starts from the correct position
- ***

## 🧪 Test Cases

### Test Case 1: Basic Example

```
Input: ["lint", "code", "love", "you"]
Expected Output: ["lint", "code", "love", "you"]
Encoded: "4#lint4#code4#love3#you"
Status: ✅ Passed
Explanation: Tests basic encoding/decoding with no special characters
```

### Test Case 2: Edge Case - Empty Strings

```
Input: ["", "a", ""]
Expected Output: ["", "a", ""]
Encoded: "0#1#a0#"
Status: ✅ Passed
Explanation: Empty strings are encoded as "0#" (zero length, delimiter, zero chars)
Key insight: Length-prefix correctly handles empty strings
```

### Test Case 3: Edge Case - Delimiter in String

```
Input: ["a#b", "c:d"]
Expected Output: ["a#b", "c:d"]
Encoded: "3#a#b3#c:d"
Status: ✅ Passed
Explanation: The '#' inside "a#b" doesn't break decoding because we extract exactly 3 chars
This demonstrates why length-prefix encoding works!
```

### Test Case 4: Edge Case - Empty List

```
Input: []
Expected Output: []
Encoded: ""
Status: ✅ Passed
Explanation: Empty list encodes to empty string, decodes back to empty list
```

### Test Case 5: Single String

```
Input: ["hello"]
Expected Output: ["hello"]
Encoded: "5#hello"
Status: ✅ Passed
Explanation: Single element should work correctly
```

### Test Case 6: Multi-Digit Length

```
Input: ["aaaaaaaaaa"]  // 10 a's
Expected Output: ["aaaaaaaaaa"]
Encoded: "10#aaaaaaaaaa"
Status: ✅ Passed
Explanation: Length can be multi-digit. Parser reads until '#' to get full length "10"
```

### Test Case 7: Special Characters

```
Input: ["a,b;c:d"]
Expected Output: ["a,b;c:d"]
Encoded: "7#a,b;c:d"
Status: ✅ Passed
Explanation: All special characters are safely handled
```

---

## 📊 Complexity Analysis

### Time Complexity: O(n)

**Where n = total number of characters across all strings**

**Encode - O(n):**

- Single pass through all strings: O(n)
- For each string, we append 3 things (length, delimiter, string): O(1) per append with StringBuilder
- Total: O(n)

**Decode - O(n):**

- Single scan through the encoded string: O(n)
- For each encoded segment:
  - Find delimiter: O(k) where k = digits in length (typically small, < 10)
  - Extract length: O(k) for parsing integer
  - Extract string: O(m) where m = length of that string
- Total characters processed: n
- Overall: O(n)

**Best/Average/Worst Case:** All O(n) - always process entire input

### Space Complexity: O(n)

**Encode - O(n):**

- StringBuilder to build encoded string: O(n + k) where k = overhead for lengths and delimiters
- k ≈ O(m log₁₀L) where m = number of strings, L = average length
- For practical purposes: O(n)

**Decode - O(n):**

- Result list holding original strings: O(n)
- No additional data structures needed
- Total: O(n)

### Comparison with Other Approaches:

| Approach                         | Time | Space | Pros                                                               | Cons                                                                    |
| -------------------------------- | ---- | ----- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Length-Prefix** (Our Solution) | O(n) | O(n)  | ✅ Simple<br>✅ Handles any character<br>✅ Used in real protocols | ❌ Slight overhead for lengths                                          |
| **Delimiter + Escaping**         | O(n) | O(n)  | ✅ Intuitive                                                       | ❌ Complex escape logic<br>❌ Error-prone<br>❌ Must escape escape char |
| **Fixed-Length**                 | O(n) | O(n)  | ✅ Very simple                                                     | ❌ Only works for fixed-length strings<br>❌ Not applicable here        |
| **JSON Serialization**           | O(n) | O(n)  | ✅ Built-in library                                                | ❌ Not allowed (problem constraint)<br>❌ "Cheating"                    |

- ***

## 🎓 Key Learnings

### What I Learned

1. **Length-Prefix Encoding Pattern:**

   - Elegant solution to the "delimiter collision" problem
   - Used in real-world: HTTP chunked encoding, Protocol Buffers, network protocols
   - Format: `length + delimiter + data` makes data self-describing

2. **Why Length-Prefix Works:**

   - The key insight: once you know the length, you can extract exactly that many characters
   - Delimiters inside the data become irrelevant during extraction
   - This "character blindness" during extraction is the magic!

3. **Two-Pointer Technique for Parsing:**

   - `i` tracks the start of the current segment
   - `j` scans ahead to find delimiters
   - **Critical:** Must reset `j = i` after each segment to avoid bugs!

4. **StringBuilder Efficiency:**

   - String concatenation with `+` is O(n²) in Java due to immutability
   - StringBuilder provides O(n) construction
   - Always use StringBuilder for building strings in loops

5. **Serialization Concepts:**
   - Encoding/decoding is fundamental in computer science
   - Trade-offs: simplicity vs. efficiency vs. generality
   - Self-describing formats are more robust but have overhead

### Mistakes I Made

1. **Forgot to Reset Pointer `j`:**

   - Initial bug: After processing each word, `j` remained at old delimiter position
   - Caused `StringIndexOutOfBoundsException` or incorrect parsing
   - **Fix:** Add `j = i` after each iteration
   - **Lesson:** When using multiple loop variables, ensure all are synchronized

2. **Initially Considered Simple Delimiters:**

   - Thought using `:;` as in the example would work
   - Didn't fully appreciate "ANY ASCII character" constraint
   - **Lesson:** Always read constraints carefully - "any character" rules out simple delimiters

3. **Considered URL Encoding:**
   - Valid approach but overly complex
   - Would need to escape `%` first, then other characters
   - **Lesson:** Simpler elegant solution exists (length-prefix) - don't over-engineer

### Pattern Insights

**When to use Length-Prefix Encoding:**

- ✅ Need to serialize/deserialize variable-length data
- ✅ Data can contain any characters (no "forbidden" characters)
- ✅ Need a simple, stateless encoding scheme
- ✅ Want a self-describing format
- ✅ Implementing network protocols or file formats

**When NOT to use this pattern:**

- ❌ Fixed-length data (simpler to just concatenate)
- ❌ Can guarantee delimiter won't appear in data
- ❌ Need human-readable encoding (CSV, JSON better)
- ❌ Have access to built-in serialization libraries and they're allowed

**Related Patterns:**

- **Type-Length-Value (TLV):** Adds type field before length
- **Varint Encoding:** Variable-length integer encoding (Protocol Buffers)
- **Escape Sequences:** Alternative way to handle special characters
- **Chunked Transfer Encoding:** HTTP uses similar technique

**Common Pitfalls:**

- ⚠️ Forgetting to reset scanning pointers
- ⚠️ Not handling multi-digit lengths correctly
- ⚠️ Off-by-one errors in substring extraction
- ⚠️ Forgetting edge cases (empty strings, empty list)

---

## 🔗 Similar Problems

### Direct Variations:

1. **[LeetCode 297] Serialize and Deserialize Binary Tree** (Hard)

   - Uses similar encoding concept for tree structures
   - Must encode structure + values

2. **[LeetCode 535] Encode and Decode TinyURL** (Medium)
   - Different type of encoding (URL shortening)
   - Focus on bijective mapping

### Same Pattern (String Manipulation/Serialization):

3. **[LeetCode 443] String Compression** (Medium)

   - Encode strings with run-length encoding
   - Similar concept of compact representation

4. **[LeetCode 394] Decode String** (Medium)

   - Parse encoded string format `k[string]`
   - Similar parsing with number prefix

5. **[LeetCode 385] Mini Parser** (Medium)
   - Parse nested list structure from string
   - Similar concept of serialization/deserialization

### Related Concepts:

6. **Design Problems:** Serialization is common in system design
7. **Protocol Design:** Understand how data is transmitted over networks

---

## 🎯 Quick Reference Card

**Pattern:** String Manipulation - Length-Prefix Encoding  
**Key Insight:** Using `length#string` format allows delimiters to appear safely in data  
**Time:** O(n) | **Space:** O(n)

**Template:**

```java
// ENCODE: length + delimiter + string
public String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();
    for (String s : strs) {
        sb.append(s.length()).append("#").append(s);
    }
    return sb.toString();
}

// DECODE: parse length, extract exact chars
public List<String> decode(String s) {
    List<String> result = new ArrayList<>();
    int i = 0, j = 0;
    while (j < s.length()) {
        // Find delimiter
        while (s.charAt(j) != '#') j++;
        // Parse length
        int len = Integer.parseInt(s.substring(i, j));
        // Extract string
        i = j + 1;
        result.add(s.substring(i, i + len));
        // Reset pointers
        i += len;
        j = i;  // ⚠️ Don't forget this!
    }
    return result;
}
```

**Remember:**

- ✅ Length-prefix makes delimiters safe
- ✅ Reset scanning pointer after each extraction
- ✅ Works for ANY characters in data
- ⚠️ Common bug: forgetting to reset `j = i`

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#string-manipulation)
- **LeetCode:** https://leetcode.com/problems/encode-and-decode-strings (Premium)
- **LintCode:** https://www.lintcode.com/problem/659/ (Free!)
- **Protocol Buffers Encoding:** https://developers.google.com/protocol-buffers/docs/encoding
- **HTTP Chunked Transfer:** https://en.wikipedia.org/wiki/Chunked_transfer_encoding

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
**Last Updated:** 2025-11-30

```

```
