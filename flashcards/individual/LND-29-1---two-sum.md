---
id: LND-29
title: Two Sum
pattern: Hash Table / Array & Hashing
difficulty: Easy
---

# LND-29: Two Sum

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  LND-29  Two Sum  🟢 Easy                            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an array of integers nums and an integer      │
│  target, return indices of the two numbers such      │
│  that they add up to target. You may assume that     │
│  each ... Ex: In=[nums = [2,7,11,15], target = 9]    │
│  Out=[[0,1]]                                         │
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
│  Two Sum - SOLUTION                                  │
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
