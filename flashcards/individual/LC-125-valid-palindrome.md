---
id: LND-119
leetcode_num: 125
title: Valid Palindrome
pattern: Two Pointers
difficulty: Easy
---

# #125: Valid Palindrome

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #125  Valid Palindrome  🟢 Easy                   │
├──────────────────────────────────────────────────────┤
│                                                      │
│  **LeetCode #125:** [Valid                         │
│  Palindrome](https://leetcode.com/problems/valid-pa  │
│  Ex: In=[s = "A man, a plan, a canal: Panama"]       │
│  Out=[true]                                          │
│                                                      │
│                                                      │
│                                                      │
│  💡 HINTS:                                           │
│  • Check symmetry without reversing?                 │
│  • What if special chars scattered?                  │
│                                                      │
│  🎯 PATTERN: Two Pointers                            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #125  Valid Palindrome - SOLUTION                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  Use two pointers from edges, skip                   │
│  non-alphanumeric independently with bounds          │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Initialize `left = 0`, `right = length - 1`      │
│  2. Skip non-alphanumeric from left (with `left < r  │
│  3. Skip non-alphanumeric from right (with `left <   │
│  4. Compare `toLowerCase(s[left])` with `toLowerCas  │
│  5. Move both pointers inward; return false on mism  │
│                                                      │
│  ⏱️  O(n)  💾 O(1)                                    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

**Print Instructions:**

- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
