---
description: Validate solution against test cases and trigger debug if failing
---

# Validate Solution Workflow

## Purpose

Systematically validate a solution by running it against all test cases, verifying correctness, and automatically triggering the debug workflow if issues are found.

## When to Use

- After implementing a solution
- Before submitting to LeetCode
- When you want to verify all test cases pass
- As a final check before documentation

---

## Workflow Steps

### 1. Extract Solution and Test Cases

- Read the problem file provided by the user
- Extract the implemented solution code
- Identify all test cases from the problem file:
  - Basic examples from problem statement
  - Edge cases defined in the file
  - Custom test cases added by user
- Note expected vs actual output fields

### 2. Prepare Test Environment

- Identify the programming language
- Check for required imports/dependencies
- Set up the test runner code
- Prepare to capture output and errors

### 3. Run Test Cases Systematically

For each test case:

1. **Execute the solution** with the test input
2. **Capture the output**
3. **Compare** actual vs expected output
4. **Record the result** (✅ Pass / ❌ Fail)
5. **Note any errors** (runtime errors, exceptions, timeouts)

### 4. Analyze Results

Categorize outcomes:

- **All Passing ✅**: Solution is correct
- **Some Failing ❌**: Identify which tests fail
- **Runtime Errors 💥**: Code has bugs or edge case issues
- **Timeout ⏱️**: Performance issues (complexity problem)

### 5. Generate Validation Report

Present results in a structured format:

```markdown
## 🧪 Validation Report: [Problem Name]

**Status**: [✅ All Passing / ❌ Failing / ⚠️ Partial]
**Tests Run**: [X/Y]
**Success Rate**: [XX%]

---

### Test Results

#### ✅ Passing Tests (X)

1. **Test Case 1**: [Description]
   - Input: [input]
   - Expected: [output]
   - Actual: [output]
   - Status: ✅ Pass

[... more passing tests ...]

---

#### ❌ Failing Tests (Y)

1. **Test Case N**: [Description]
   - Input: [input]
   - Expected: [output]
   - Actual: [output] OR Error: [error message]
   - Status: ❌ Fail
   - Issue: [Brief description of what went wrong]

[... more failing tests ...]

---

### 📊 Analysis

**What's Working**:

- [List of test categories that pass]

**What's Failing**:

- [Pattern in failures: edge cases? specific inputs? all tests?]

**Potential Issues**:

- [Hypothesis about what might be wrong]
```

### 6. Decision Point 🔀

**If ALL tests pass ✅**:

- Congratulate the user
- Suggest next steps:
  - Run `/refine` to add inline comments
  - Run `/document` to document the solution
  - Submit to LeetCode
- Update test status in problem file (if requested)

**If ANY tests fail ❌**:

- **AUTOMATICALLY TRIGGER** `/debug` workflow
- Transition message:

  ```
  ⚠️ Found [X] failing test case(s). Let's debug this systematically.

  Triggering /debug workflow to help you fix the issues...
  ```

- Pass the failing test cases to the debug workflow
- Follow debug workflow steps starting from Step 1 (Reproduce the Issue)

### 7. Run Validation Tests

Execute the solution with all test cases:

**For Python:**

```python
# Auto-generate test runner
def run_tests(solution_func):
    test_cases = [
        # (input, expected_output, description)
        ([1,2,3,4], [24,12,8,6], "Basic example"),
        ([-1,1,0,-3,3], [0,0,9,0,0], "With zeros"),
        # ... more test cases
    ]

    passed = 0
    failed = 0
    results = []

    for inputs, expected, desc in test_cases:
        try:
            actual = solution_func(*inputs) if isinstance(inputs, tuple) else solution_func(inputs)
            status = "✅ Pass" if actual == expected else "❌ Fail"

            if actual == expected:
                passed += 1
            else:
                failed += 1

            results.append({
                'description': desc,
                'input': inputs,
                'expected': expected,
                'actual': actual,
                'status': status
            })
        except Exception as e:
            failed += 1
            results.append({
                'description': desc,
                'input': inputs,
                'expected': expected,
                'actual': None,
                'error': str(e),
                'status': '💥 Error'
            })

    return passed, failed, results
```

**For Java:**

```java
// Auto-generate test class
public class SolutionTest {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int passed = 0, failed = 0;

        // Test 1
        int[] input1 = {1,2,3,4};
        int[] expected1 = {24,12,8,6};
        int[] actual1 = sol.productExceptSelf(input1);
        if (Arrays.equals(actual1, expected1)) {
            System.out.println("✅ Test 1: Pass");
            passed++;
        } else {
            System.out.println("❌ Test 1: Fail");
            System.out.println("  Expected: " + Arrays.toString(expected1));
            System.out.println("  Actual: " + Arrays.toString(actual1));
            failed++;
        }

        // ... more tests

        System.out.println("\n📊 Results: " + passed + "/" + (passed+failed) + " passed");
    }
}
```

### 8. Edge Case Validation

Specifically verify edge cases:

- **Empty input**: [] or null
- **Single element**: [5]
- **Two elements**: [1, 2]
- **All same values**: [3, 3, 3, 3]
- **Negative numbers**: [-1, -2, -3]
- **With zeros**: [0, 1, 2] or [1, 0, 2, 0]
- **Maximum constraints**: Large arrays at upper bounds
- **Minimum constraints**: Small values at lower bounds

### 9. Performance Validation

If complexity requirements are specified:

- **Time Complexity Check**:

  - Run with large input (near max constraint)
  - Measure execution time
  - Verify it completes within reasonable time
  - Flag if timeout occurs

- **Space Complexity Check**:
  - Verify auxiliary space usage
  - Check if within constraints (e.g., O(1) extra space)

### 10. Update Problem File (Optional)

If user confirms, update test case results in problem file:

```markdown
### Test Case 1: Basic Example
```

Input: [1,2,3,4]
Expected Output: [24,12,8,6]
Actual Output: [24,12,8,6]
Status: ✅ Passed

```

```

---

## Validation Checklist

- [ ] All test cases extracted
- [ ] Solution code is executable
- [ ] Each test case run individually
- [ ] Results compared accurately
- [ ] Edge cases tested
- [ ] Error handling verified
- [ ] Performance validated (if applicable)
- [ ] Report generated
- [ ] Debug workflow triggered (if failures)

---

## Integration with Other Workflows

### Success Path (All Tests Pass) ✅

```
/validate → All Pass → Suggest /refine or /document
```

### Failure Path (Tests Fail) ❌

```
/validate → Failures Detected → Auto-trigger /debug → Fix → Re-validate
```

### Complete Cycle

```
/learn → Implement → /validate → /debug (if needed) → /refine → /document
```

---

## Output Format

### Successful Validation ✅

```markdown
🎉 **Validation Successful!**

✅ All [X] test cases passed!

**Test Coverage**:

- ✅ Basic examples
- ✅ Edge cases
- ✅ Boundary conditions
- ✅ Special values

**Complexity Verification**:

- Time: O(n) ✓
- Space: O(1) ✓

**Next Steps**:

1. Run `/refine` to add inline comments
2. Run `/document` to create full documentation
3. Submit to LeetCode with confidence!

Great work! 🚀
```

### Failed Validation ❌

```markdown
⚠️ **Validation Failed**

**Summary**:

- ✅ Passed: [X] test cases
- ❌ Failed: [Y] test cases
- Success Rate: [Z%]

**Failing Tests**:
[List of failing tests with details]

**Analysis**:
[Hypothesis about the issue]

---

🔧 **Triggering Debug Workflow**

Let's systematically debug these failures...

[Proceed with /debug workflow]
```

---

## Best Practices

### When Validating:

1. **Run ALL test cases** - Don't skip any
2. **Test edge cases explicitly** - They often reveal bugs
3. **Capture full error messages** - Helps with debugging
4. **Compare carefully** - Watch for type mismatches (e.g., [1, 2] vs "1, 2")
5. **Test performance** - Ensure it meets complexity requirements
6. **Don't modify solution** - Only validate, don't fix yet

### When Triggering Debug:

1. **Pass failing test details** to debug workflow
2. **Provide context** about what tests pass vs fail
3. **Include error messages** if runtime errors occur
4. **Note patterns** in failures (all edge cases? specific inputs?)

---

## Principles

### DO:

- ✅ Test all cases systematically
- ✅ Provide clear pass/fail status
- ✅ Generate comprehensive reports
- ✅ Auto-trigger debug on failures
- ✅ Verify edge cases thoroughly
- ✅ Check complexity requirements
- ✅ Give actionable next steps

### DON'T:

- ❌ Skip test cases
- ❌ Assume passing without running
- ❌ Fix bugs immediately (document first)
- ❌ Ignore edge case failures
- ❌ Modify code during validation
- ❌ Give up if tests fail (debug instead!)

---

## Success Criteria

- All test cases executed and results captured
- Clear validation report generated
- Passing tests clearly identified
- Failing tests detailed with context
- Debug workflow triggered if needed
- User knows exact next steps
- Confidence in solution correctness

---

**Remember**: Validation isn't just about passing tests—it's about building confidence that your solution handles all cases correctly!
