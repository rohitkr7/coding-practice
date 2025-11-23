---
description: Debug a failing solution systematically
---

# Debug Solution Workflow

**Purpose**: Systematically debug a failing solution using a methodical approach

**Trigger**: "debug this", "something's wrong", "help me debug", or when tests fail

**When to Use**:
- Solution fails test cases
- Getting unexpected output
- Code has runtime errors
- Logic seems correct but results are wrong
- Need systematic debugging approach

---

## Workflow Steps

### Step 1: Reproduce the Issue
- What test case is failing?
- What's the expected vs actual output?
- Can we reproduce it consistently?
- Is it ALL cases or specific ones?

**Cascade Action**: 
- Ask user for the failing test case
- Document expected vs actual output
- Identify pattern in failing cases (edge cases? large inputs? specific values?)

**Example**:
```
Failing Test: [1,2,3,4,5], target=9
Expected: [3,4] (indices of 4 and 5)
Actual: [2,3] (incorrect indices)
```

### Step 2: Understand the Code
- Review the solution approach
- Identify the main algorithm/logic
- Spot potential problem areas
- Check variable names and scopes

**Cascade Action**:
- Walk through the code section by section
- Explain what each part SHOULD do
- Highlight complex or tricky sections
- Don't fix yet - just understand!

### Step 3: Add Tracing/Logging
- Insert strategic print statements
- Track variable values at key points
- Monitor loop iterations
- Check conditional branches

**Cascade Action**: Suggest WHERE to add logging:
```python
# Suggest strategic logging points
def two_sum(nums, target):
    print(f"🔍 Starting with nums={nums}, target={target}")  # Initial state
    
    hash_map = {}
    for i, num in enumerate(nums):
        print(f"  Step {i}: num={num}, hash_map={hash_map}")  # Each iteration
        
        complement = target - num
        if complement in hash_map:
            print(f"  ✅ Found! complement={complement} at index {hash_map[complement]}")
            return [hash_map[complement], i]
        
        hash_map[num] = i
    
    print("  ❌ No solution found")
    return []
```

// turbo
### Step 4: Trace Through Failing Case
- Run code with logging enabled
- Follow execution step-by-step
- Compare actual vs expected behavior at each step
- Identify WHEN things go wrong

**Cascade Action**:
- Show expected trace for correct solution
- Compare with actual trace
- Point out the FIRST point where they diverge
- This is likely where the bug is!

### Step 5: Form Hypothesis
- Based on traces, what's the bug?
- Is it off-by-one error?
- Wrong variable used?
- Logic condition incorrect?
- Edge case not handled?

**Cascade Action**:
- List 2-3 most likely hypotheses
- Explain WHY each could cause the observed behavior
- Rank by likelihood
- **Still don't give the fix!**

### Step 6: Test Hypothesis
- Suggest test to confirm hypothesis
- Isolate the suspected bug
- Try minimal fix
- Verify it solves the problem

**Cascade Action**:
- Suggest how to test each hypothesis
- Guide toward the fix with questions:
  - "What happens if we..."
  - "What should this value be when..."
  - "Have we considered..."

### Step 7: Verify Fix
- Does it pass the original failing test?
- Does it still pass other test cases?
- Does it handle edge cases?
- Is the logic sound now?

**Cascade Action**:
- Run through all test cases
- Check edge cases specifically
- Confirm complexity hasn't changed
- Validate the fix is minimal (not overengineered)

### Step 8: Document the Bug
- What was the bug?
- Why did it happen?
- How was it fixed?
- What did we learn?

**Cascade Action**: Create a "Bug Report" section:
```markdown
## 🐛 Bug Report: Off-by-One Error

**Issue**: Returning wrong indices in two_sum solution

**Root Cause**: 
- Used `i-1` instead of `i` when storing indices
- This shifted all indices down by one

**Symptoms**:
- All returned indices were one less than expected
- Failed on test: [1,2,3,4,5], target=9

**Fix**:
- Changed `hash_map[num] = i-1` to `hash_map[num] = i`
- One-line fix, big impact!

**Lesson Learned**:
- Always verify index arithmetic carefully
- Off-by-one errors are subtle and common
- Good logging revealed the issue quickly

**How to Avoid**:
- Use meaningful variable names (not just i,j,k)
- Add assertions: assert 0 <= index < len(nums)
- Test with simple cases first
```

---

## Debug Strategies by Issue Type

### Strategy 1: Wrong Output (Logic Error)
1. Trace execution manually
2. Check conditional logic
3. Verify loop boundaries
4. Validate edge cases

### Strategy 2: Runtime Error
1. Check array bounds
2. Verify null/None handling
3. Check division by zero
4. Validate input assumptions

### Strategy 3: Timeout (Performance Issue)
1. Analyze time complexity
2. Check for nested loops
3. Look for redundant operations
4. Consider data structure changes

### Strategy 4: Edge Case Failure
1. List all edge cases
2. Trace specific edge case
3. Add missing condition
4. Test systematically

---

## Example Debugging Session

### Problem: Contains Duplicate
```python
# Buggy Solution
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return False  # 🐛 BUG! Should be True
        seen.add(num)
    return True  # 🐛 BUG! Should be False
```

### Debug Process:

**Step 1**: Reproduce
```
Input: [1,2,3,1]
Expected: True (1 is duplicate)
Actual: False (wrong!)
```

**Step 2**: Add Logging
```python
def contains_duplicate(nums):
    print(f"🔍 Input: {nums}")
    seen = set()
    for num in nums:
        print(f"  Checking {num}, seen: {seen}")
        if num in seen:
            print(f"  ✅ Found duplicate: {num}")
            return False  # Returns False when finding duplicate
        seen.add(num)
    print("  ❌ No duplicates")
    return True  # Returns True when no duplicates
```

**Step 3**: Trace
```
🔍 Input: [1,2,3,1]
  Checking 1, seen: set()
  Checking 2, seen: {1}
  Checking 3, seen: {1, 2}
  Checking 1, seen: {1, 2, 3}
  ✅ Found duplicate: 1
  → Returns False ← WRONG! Should return True
```

**Step 4**: Hypothesis
- **Hypothesis**: Return values are swapped
- **Evidence**: Returns False when finding duplicate, True when not

**Step 5**: Fix
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True  # ✅ Fixed!
        seen.add(num)
    return False  # ✅ Fixed!
```

**Step 6**: Verify
```
[1,2,3,1] → True ✓
[1,2,3,4] → False ✓
[] → False ✓
[1] → False ✓
```

---

## Debugging Checklist

Before asking for help, have you:
- [ ] Identified the failing test case?
- [ ] Added print/logging statements?
- [ ] Traced through execution manually?
- [ ] Checked for off-by-one errors?
- [ ] Validated edge cases?
- [ ] Reviewed variable names and scopes?
- [ ] Checked return values?
- [ ] Tested with simple inputs?

---

## Tips for Cascade

When executing this workflow:

1. **Be Socratic**: Ask questions rather than giving answers
2. **Be Patient**: Debug step-by-step, don't jump to solutions
3. **Be Thorough**: Check each hypothesis systematically
4. **Be Encouraging**: Debugging is a skill - celebrate the learning
5. **Be Specific**: Point to exact lines, not vague areas

**Good Cascade Response**:
```
I see the issue is in the loop. Let's trace what happens when we 
reach the duplicate. On line 5, when num=1 for the second time,
what does the condition `if num in seen` evaluate to? And what 
do we return in that case? Is that the correct return value?
```

**Bad Cascade Response**:
```
The bug is on line 5, change return False to return True.
```

---

## Integration with Learning

After debugging:
1. Document the bug in problem file
2. Add to "Common Mistakes" section
3. Create similar test case for future problems
4. Update pattern understanding
5. Share learning with weekly review

---

**Remember**: Bugs are learning opportunities! Each bug you debug makes you a better problem solver.
