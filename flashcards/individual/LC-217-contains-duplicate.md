---
id: LND-30
leetcode_num: 217
title: Contains Duplicate
pattern: Hash Table / Array & Hashing
difficulty: Easy
---

# #217: Contains Duplicate

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #217  Contains Duplicate  🟢 Easy                   │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an integer array nums, return true if any     │
│  value appears at least twice in the array, and      │
│  return false if every element is distinct. Ex:      │
│  In=[nums = [1,2,3,1]] Out=[true]                    │
│                                                      │
│                                                      │
│                                                      │
│  💡 HINTS:                                           │
│  • Have we seen this element before?                 │
│  • What data structure gives O(1) lookup?            │
│                                                      │
│  🎯 PATTERN: Hash Table / Array & Hashing            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #217  Contains Duplicate - SOLUTION                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Use HashSet to track seen elements - if we see      │
│  an element that's already in the set, we found a    │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Create empty HashSet                             │
│  2. For each number in array                         │
│  3. If number exists in set: return true             │
│  4. Add number to set                                │
│  5. Return false (no duplicates found)               │
│                                                      │
│  ⏱️  O(n)  💾 O(n)                                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

**Print Instructions:**
- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
