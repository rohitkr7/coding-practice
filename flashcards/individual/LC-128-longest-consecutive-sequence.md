---
id: LND-35
leetcode_num: 128
title: Longest Consecutive Sequence
pattern: Hash Table / Array & Hashing
difficulty: Medium
---

# #128: Longest Consecutive Sequence

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #128  Longest Consecutive Sequence  🟡 Medium       │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an unsorted array of integers nums, return    │
│  the length of the longest consecutive elements      │
│  sequence. You must write an algorithm that runs     │
│  in ... Ex: In=[nums = [100,4,200,1,3,2]] Out=[4]    │
│                                                      │
│                                                      │
│                                                      │
│  💡 HINTS:                                           │
│  • How to check if num-1 or num+1 exist quickly?     │
│  • How to avoid counting same sequence twice?        │
│                                                      │
│  🎯 PATTERN: Hash Table / Array & Hashing            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #128  Longest Consecutive Seque - SOLUTION          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Only count from sequence starts (where num-1        │
│  doesn't exist). Iterate over HashSet, not array!    │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Build HashSet for O(1) lookups                   │
│  2. Iterate over HashSet (not array!)                │
│  3. If num-1 doesn't exist: sequence start           │
│  4. Count consecutive: num→num+1→num+2...            │
│  5. Track max length                                 │
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
