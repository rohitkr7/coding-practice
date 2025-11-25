---
id: LND-30
title: Contains Duplicate
pattern: Hash Table / Array & Hashing
difficulty: Easy
---

# LND-30: Contains Duplicate

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  LND-30  Contains Duplicate  🟢 Easy                 │
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
│  • What gives O(1) lookup/insert?                    │
│                                                      │
│  🎯 PATTERN: Hash Table / Array & Hashing            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  Contains Duplicate - SOLUTION                       │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Use HashMap to store seen elements for O(1)         │
│  lookup                                              │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Create HashMap to store value→index              │
│  2. For each element:                                │
│  - Check if complement exists in map                 │
│  - If yes: return indices                            │
│  - If no: add current to map                         │
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
