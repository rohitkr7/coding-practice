---
id: LND-28
leetcode_num: 49
title: Group Anagrams
pattern: Hash Table / Array & Hashing
difficulty: Medium
---

# #49: Group Anagrams

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #49  Group Anagrams  🟡 Medium                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an array of strings strs, group the           │
│  anagrams together. You can return the answer in     │
│  any order. An Anagram is a word or phrase formed    │
│  by rearr... Ex: In=[strs =                          │
│  ["eat","tea","tan","ate","nat","bat"]]              │
│  Out=[[["bat"],["nat","tan"],["ate","eat","tea"]]]   │
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
│  #49  Group Anagrams - SOLUTION                      │
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
│  ⏱️  O(n × m)  💾 O(n × m)                           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

**Print Instructions:**
- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
