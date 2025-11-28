---
id: LND-36
leetcode_num: 347
title: Top K Frequent Elements
pattern: Top K Elements
difficulty: Medium
---

# #347: Top K Frequent Elements

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #347  Top K Frequent Elements  🟡 Medium            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an integer array nums and an integer k,       │
│  return the k most frequent elements. You may        │
│  return the answer in any order. Ex: In=[nums =      │
│  [1,1,1,2,2,3], k = 2] Out=[[1,2]]                   │
│                                                      │
│                                                      │
│                                                      │
│  💡 HINTS:                                           │
│  • Need all sorted or just top k?                    │
│  • Can frequency be used as index?                   │
│                                                      │
│  🎯 PATTERN: Top K Elements                          │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #347  Top K Frequent Elements - SOLUTION            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Use frequency as array index for O(n) bucket        │
│  sort                                                │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Count frequencies with HashMap                   │
│  2. Create buckets[n+1] or use heap                  │
│  3. Place elements in bucket[frequency]              │
│  4. Traverse high→low, collect k items               │
│                                                      │
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
