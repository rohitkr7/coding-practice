---
id: LND-32
leetcode_num: 271
title: Encode and Decode Strings
pattern: String Manipulation
difficulty: Medium
---

# #271: Encode and Decode Strings

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #271  Encode and Decode Strings  🟡 Medium          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Design an algorithm to encode a list of strings     │
│  to a string. The encoded string is then sent        │
│  over the network and is decoded back to the         │
│  original l... Ex:                                   │
│  In=[["lint","code","love","you"]]                   │
│  Out=[["lint","code","love","you"]]                  │
│                                                      │
│  💡 HINTS:                                           │
│  • Can delimiters appear in the data itself?         │
│  • How can length information help avoid collisions  │
│                                                      │
│  🎯 PATTERN: String Manipulation                     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #271  Encode and Decode Strings - SOLUTION          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Use length#string format - once we know length,     │
│  we can safely extract exact chars (delimiters       │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Encode: append length + "#" + string             │
│  2. Decode: read length, skip "#", extract chars     │
│  3. Reset pointers: j = i after each extraction      │
│                                                      │
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
