---
id: LND-37
leetcode_num: 238
title: Product of Array Except Self
pattern: Array Manipulation / Prefix-Suffix Products
difficulty: Medium
---

# #238: Product of Array Except Self

## 🎴 FRONT (Problem)

```
┌──────────────────────────────────────────────────────┐
│  #238  Product of Array Except Self  🟡 Medium       │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Given an integer array nums, return an array        │
│  answer such that answer[i] is equal to the          │
│  product of all the elements of nums except          │
│  nums[i]. The pro... Ex: In=[nums = [1,2,3,4]]       │
│  Out=[[24,12,8,6]]                                   │
│                                                      │
│                                                      │
│  💡 HINTS:                                           │
│  • Can we split into left × right products?          │
│  • What's the product BEFORE and AFTER each index?   │
│  • Can we reuse the output array for storage?        │
│                                                      │
│  🎯 PATTERN: Array Manipulation / Prefix-Suffix      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎴 BACK (Solution)

```
┌──────────────────────────────────────────────────────┐
│  #238  Product of Array Except S - SOLUTION          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  💡 KEY INSIGHT:                                     │
│  result[i] = (product of all left) × (all right)     │
│  Use two passes: prefix forward, suffix backward     │
│                                                      │
│                                                      │
│  🔢 ALGORITHM:                                       │
│  1. Build prefix products in result array            │
│     result[i] = product of nums[0..i-1]              │
│  2. Multiply by suffix products (right-to-left)      │
│     Use single variable, update as you go            │
│  3. Return result (no extra arrays needed!)          │
│                                                      │
│                                                      │
│  ⏱️  O(n)  💾 O(1) [except output]                  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

**Print Instructions:**

- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
