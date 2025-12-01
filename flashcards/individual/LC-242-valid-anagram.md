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
│  • Do both strings need same character frequencies?  │
│  • Can sorting help?                                 │
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
│  Count character frequencies - two strings are       │
│  anagrams if they have identical character counts    │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Check if lengths differ (early return false)     │
│  2. Count frequency of each char in both strings     │
│  3. Compare frequency maps or arrays                 │
│  4. Return true if identical, false otherwise        │
│                                                      │
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
