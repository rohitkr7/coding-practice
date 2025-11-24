# Problem Reorganization Summary

**Date:** 2025-11-24  
**Total Problems Reorganized:** 25 problems  
**Files Moved:** 18 files  
**New Directories Created:** 5 directories

---

## 🎯 Overview

Identified and corrected pattern misclassifications across the problem set. Many problems were incorrectly labeled as "Two Pointers" when they actually belonged to different patterns.

---

## 📁 New Pattern Directories Created

1. **hash-table** (5 problems)
2. **dynamic-programming** (7 problems)
3. **matrix** (3 problems)
4. **trie** (2 problems)
5. **string-manipulation** (1 problem)

---

## 📊 Problems Reorganized by Pattern

### Hash Table / Array & Hashing (5 problems moved)

| Problem | File | Previous | Current |
|---------|------|----------|---------|
| Valid Anagram | `LND-27-3-valid-anagram.md` | Two Pointers | **Hash Table** |
| Group Anagrams | `LND-28-4-group-anagrams.md` | Two Pointers | **Hash Table** |
| Two Sum | `LND-29-1-two-sum.md` | Two Pointers | **Hash Table** |
| Contains Duplicate | `LND-30-2-contains-duplicate.md` | Two Pointers | **Hash Table** |
| Longest Consecutive Sequence | `LND-35-8-longest-consecutive-sequence.md` | Two Pointers | **Hash Table** |

**Why Hash Table?**
- These problems require fast lookup and grouping operations
- Use HashMap/HashSet as primary data structure
- Focus on O(1) average time complexity for lookups
- Keywords: "find", "group", "duplicate", "contains"

---

### Dynamic Programming (7 problems moved)

| Problem | File | Previous | Current |
|---------|------|----------|---------|
| Decode Ways | `LND-45-56-decode-ways.md` | Two Pointers | **Dynamic Programming** |
| House Robber II | `LND-47-53-house-robber-ii.md` | Two Pointers | **Dynamic Programming** |
| House Robber | `LND-56-52-house-robber.md` | Two Pointers | **Dynamic Programming** |
| Word Break | `LND-72-59-word-break.md` | Two Pointers | **Dynamic Programming** |
| Longest Common Subsequence | `LND-73-62-longest-common-subsequence.md` | Two Pointers | **Dynamic Programming** |
| Longest Increasing Subsequence | `LND-76-60-longest-increasing-subsequence.md` | Two Pointers | **Dynamic Programming** |
| Unique Paths | `LND-78-61-unique-paths.md` | Two Pointers | **Dynamic Programming** |

**Why Dynamic Programming?**
- These problems have overlapping subproblems
- Require memoization or tabulation
- Build solutions from smaller subproblems
- Keywords: "longest", "ways", "count", "maximum/minimum"

---

### Matrix / Math & Geometry (3 problems moved)

| Problem | File | Previous | Current |
|---------|------|----------|---------|
| Rotate Image | `LND-89-69-rotate-image.md` | Two Pointers | **Matrix** |
| Spiral Matrix | `LND-90-70-spiral-matrix.md` | Two Pointers | **Matrix** |
| Set Matrix Zeroes | `LND-94-71-set-matrix-zeroes.md` | Two Pointers | **Matrix** |

**Why Matrix?**
- These problems work with 2D arrays/matrices
- Require matrix traversal patterns
- Often involve in-place modifications
- Keywords: "matrix", "rotate", "spiral", "grid"

---

### Trie (2 problems moved)

| Problem | File | Previous | Current |
|---------|------|----------|---------|
| Design Add and Search Words | `LND-34-41-design-add-and-search-words-data-structure.md` | Two Pointers | **Trie** |
| Word Search II | `LND-20-42-word-search-ii.md` | Two Pointers | **Trie** |

**Why Trie?**
- These problems involve prefix-based search
- Require efficient string storage and retrieval
- Use tree-like data structure for words
- Keywords: "search words", "prefix", "dictionary"

---

### String Manipulation (1 problem moved)

| Problem | File | Previous | Current |
|---------|------|----------|---------|
| Encode and Decode Strings | `LND-32-7-encode-and-decode-strings.md` | Two Pointers | **String Manipulation** |

**Why String Manipulation?**
- This problem is about designing encoding/decoding schemes
- Focus on string processing and delimiter handling
- Not a typical pattern problem

---

## ✅ Problems That Remained in Two Pointers (7 problems)

These are correctly classified and stayed in the two-pointers directory:

| Problem | File | Why Two Pointers? |
|---------|------|-------------------|
| First Task | `LND-1-first-task.md` | Original task |
| Container with Most Water | `LND-116-11-container-with-most-water.md` | Two pointers from both ends |
| Best Time to Buy and Sell Stock | `LND-117-12-best-time-to-buy-and-sell-stock.md` | Sliding window/two pointers |
| Valid Palindrome | `LND-119-9-valid-palindrome.md` | Classic two pointers from both ends |
| 3Sum | `LND-121-10-3sum.md` | Sort + fix one + two pointers |
| Remove Nth Node from End | `LND-132-28-remove-nth-node-from-end-of-list.md` | Fast/slow pointers in linked list |
| Reorder List | `LND-141-27-reorder-list.md` | Fast/slow pointers + reversal |

---

## 📈 Pattern Distribution

**Before Reorganization:**
- Two Pointers: 25 problems (incorrect)

**After Reorganization:**
- Two Pointers: 7 problems ✅
- Hash Table: 5 problems ✅
- Dynamic Programming: 7 problems ✅
- Matrix: 3 problems ✅
- Trie: 2 problems ✅
- String Manipulation: 1 problem ✅

**Total Patterns: 20** (was 16, added 4 new patterns)

---

## 🔍 Pattern Recognition Guidelines

### Two Pointers Pattern
**When to use:**
- Working with sorted arrays or linked lists
- Finding pairs/triplets with specific sums
- Palindrome checking
- Removing duplicates in-place
- Merging sorted arrays

**Key characteristics:**
- Two indices moving toward each other or in same direction
- Often works on sorted data
- In-place modifications
- O(n) time complexity typically

### Hash Table Pattern
**When to use:**
- Need fast lookup (O(1))
- Finding duplicates or frequency counting
- Grouping elements
- Complement/pair finding

**Key characteristics:**
- HashMap or HashSet as primary data structure
- Trade space for time
- O(1) average lookup time

### Dynamic Programming Pattern
**When to use:**
- Optimization problems (max/min)
- Counting problems (how many ways)
- Overlapping subproblems
- Optimal substructure

**Key characteristics:**
- Build solution from smaller subproblems
- Use memoization or tabulation
- Often O(n²) or O(n) time complexity

### Matrix Pattern
**When to use:**
- 2D grid/matrix problems
- Traversal patterns (spiral, zigzag)
- In-place matrix modifications

**Key characteristics:**
- Work with rows and columns
- Often involves nested loops
- May require multiple passes

### Trie Pattern
**When to use:**
- Prefix-based searches
- Dictionary/word problems
- Autocomplete features
- Multiple string searches

**Key characteristics:**
- Tree structure for strings
- Efficient prefix operations
- Space-time tradeoff

---

## 🚀 Next Steps

1. ✅ **Reorganization Complete** - All files moved and updated
2. ✅ **Tracker Updated** - README.md now reflects new structure
3. ⏳ **Review Changes** - Verify the new organization makes sense
4. ⏳ **Git Commit** - Commit these changes to version control
5. ⏳ **Update Workflows** - Ensure workflow scripts work with new structure

---

## 📝 Notes

- The `labels` field in each problem file already hinted at the correct pattern (e.g., "Array_Hashing", "1-D_Dynamic_Programming")
- This reorganization aligns the directory structure with the actual problem-solving patterns
- Makes it easier to practice problems by pattern
- Improves learning by grouping similar problem-solving approaches

---

## 🛠️ Script Created

A reusable script `reorganize_problems.py` has been created to:
- Automate problem reorganization
- Update pattern metadata
- Move files to correct directories
- Provide detailed execution logs

Can be used for future reorganizations if needed.

---

**Status:** ✅ COMPLETE  
**Problems Updated:** 25/25  
**Errors:** 0  
**Success Rate:** 100%
