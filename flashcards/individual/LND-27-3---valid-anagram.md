---
id: LND-27
leetcode_num: 242
title: Valid Anagram
pattern: Hash Table / Array & Hashing
difficulty: Easy
---

# #242: Valid Anagram

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #242  Valid Anagram  🟢 Easy                        │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given two strings s and t, return true if t is      │
│  an anagram of s, and false otherwise. An Anagram    │
│  is a word or phrase formed by rearranging the       │
│  lette... Ex: In=[s = "anagram", t = "nagaram"]      │
│  Out=[true]                                          │
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
│  #242  Valid Anagram - SOLUTION                      │
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
│  ⏱️  O(n)  💾 O(1)                                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

**Print Instructions:**
- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
