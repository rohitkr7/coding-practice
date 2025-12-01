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
│  • What do anagrams have in common when sorted?      │
│  • Can sorted string be a key?                       │
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
│  Use sorted string as HashMap key - all anagrams     │
│  will have the same sorted representation and map    │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Create HashMap<String, List<String>>             │
│  2. For each string: sort it                         │
│  3. Use sorted string as key                         │
│  4. Add original string to list at that key          │
│  5. Return all values from HashMap                   │
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
