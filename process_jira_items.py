#!/usr/bin/env python3
"""
Process Jira work items and create problem files in appropriate pattern folders.
"""

import json
import os
import re
from pathlib import Path

# Pattern mapping based on problem categories/labels
PATTERN_MAPPING = {
    # Arrays & Strings
    'array': 'two-pointers',
    'string': 'sliding-window',
    'two-pointers': 'two-pointers',
    'sliding-window': 'sliding-window',
    
    # Linked Lists
    'linked-list': 'linkedlist-reversal',
    'linkedlist': 'linkedlist-reversal',
    
    # Trees
    'tree': 'tree-dfs',
    'binary-tree': 'tree-dfs',
    'bfs': 'tree-bfs',
    'dfs': 'tree-dfs',
    
    # Stack & Queue
    'stack': 'tree-dfs',  # Often uses DFS-like thinking
    'queue': 'tree-bfs',
    
    # Dynamic Programming
    'dp': 'knapsack-dp',
    'dynamic-programming': 'knapsack-dp',
    'dynamic_programming': 'knapsack-dp',
    
    # Graphs
    'graph': 'topological-sort',
    
    # Heaps
    'heap': 'two-heaps',
    'priority-queue': 'top-k-elements',
    
    # Binary Search
    'binary-search': 'binary-search',
    'binary_search': 'binary-search',
    
    # Intervals
    'interval': 'merge-intervals',
    'intervals': 'merge-intervals',
    
    # Backtracking
    'backtracking': 'subsets',
    
    # Bit Manipulation
    'bit-manipulation': 'bitwise-xor',
    'bit_manipulation': 'bitwise-xor',
    
    # Greedy
    'greedy': 'top-k-elements',
    
    # Sorting
    'sorting': 'cyclic-sort',
    'sort': 'cyclic-sort',
}

def sanitize_filename(name):
    """Convert problem name to valid filename."""
    # Remove special characters and convert to lowercase
    name = re.sub(r'[^\w\s-]', '', name.lower())
    # Replace spaces with hyphens
    name = re.sub(r'[-\s]+', '-', name)
    return name.strip('-')

def determine_pattern(labels, summary, description):
    """Determine which pattern folder this problem belongs to."""
    # Check labels first
    for label in labels:
        label_lower = label.lower().replace(' ', '-')
        if label_lower in PATTERN_MAPPING:
            return PATTERN_MAPPING[label_lower]
    
    # Check summary and description for keywords
    text = (summary + ' ' + str(description)).lower()
    
    # Specific problem type detection
    if 'parenthes' in text or 'bracket' in text:
        return 'tree-dfs'  # Stack-based problems
    if 'reverse' in text and 'linked' in text:
        return 'linkedlist-reversal'
    if 'cycle' in text and 'linked' in text:
        return 'fast-slow-pointers'
    if 'substring' in text or 'subarray' in text:
        return 'sliding-window'
    if 'interval' in text:
        return 'merge-intervals'
    if 'tree' in text or 'binary tree' in text:
        if 'level' in text or 'breadth' in text:
            return 'tree-bfs'
        return 'tree-dfs'
    if 'graph' in text:
        return 'topological-sort'
    if 'heap' in text or 'median' in text:
        return 'two-heaps'
    if 'subset' in text or 'combination' in text or 'permutation' in text:
        return 'subsets'
    if 'search' in text and 'sorted' in text:
        return 'binary-search'
    if 'xor' in text or 'bit' in text:
        return 'bitwise-xor'
    if 'top' in text and 'k' in text:
        return 'top-k-elements'
    if 'merge' in text and ('list' in text or 'array' in text):
        return 'k-way-merge'
    if 'knapsack' in text or 'coin' in text or 'climb' in text:
        return 'knapsack-dp'
    
    # Default to two-pointers for general array problems
    return 'two-pointers'

def extract_leetcode_url(description):
    """Extract LeetCode URL from description."""
    if not description:
        return None
    
    desc_str = json.dumps(description)
    match = re.search(r'https://leetcode\.com/problems/[\w-]+', desc_str)
    return match.group(0) if match else None

def get_description_text(description):
    """Extract plain text from Jira description object."""
    if not description or 'content' not in description:
        return ""
    
    text_parts = []
    for block in description.get('content', []):
        if block.get('type') == 'paragraph':
            for content in block.get('content', []):
                if content.get('type') == 'text':
                    text_parts.append(content.get('text', ''))
    
    return '\n'.join(text_parts)

def create_problem_file(issue, base_path):
    """Create a problem file for the given issue."""
    key = issue['key']
    fields = issue['fields']
    summary = fields['summary']
    description = fields.get('description', {})
    status = fields['status']['name']
    priority = fields['priority']['name']
    labels = fields.get('labels', [])
    created = fields['created']
    updated = fields['updated']
    
    # Determine pattern
    desc_text = get_description_text(description)
    pattern = determine_pattern(labels, summary, desc_text)
    
    # Create filename
    problem_name = summary.replace(f'{key} - ', '').replace('Rohit - ', '').strip()
    filename = f"{key}-{sanitize_filename(problem_name)}.md"
    
    # Get LeetCode URL
    leetcode_url = extract_leetcode_url(description)
    
    # Determine difficulty from labels or description
    difficulty = 'Medium'  # default
    for label in labels:
        if label.lower() in ['easy', 'medium', 'hard']:
            difficulty = label.capitalize()
            break
    
    # Create file content
    content = f"""# {problem_name}

**Jira Ticket:** [{key}](https://rohitroy007.atlassian.net/browse/{key})  
**LeetCode:** {leetcode_url if leetcode_url else 'N/A'}  
**Pattern:** {pattern.replace('-', ' ').title()}  
**Difficulty:** {difficulty}  
**Status:** {status}  
**Priority:** {priority}

**Labels:** {', '.join(labels) if labels else 'None'}  
**Created:** {created[:10]}  
**Last Updated:** {updated[:10]}

---

## 📝 Problem Statement

{desc_text}

---

## 🤔 Initial Thoughts

### Understanding the Problem
- What are we asked to find/compute?
- What are the inputs and outputs?
- What are the edge cases?

### Pattern Recognition
**Why {pattern.replace('-', ' ').title()}?**
- 

**What clues in the problem point to this pattern?**
- 

---

## 💡 Approach

### Brute Force (if applicable)
**Idea:**
- 

**Time Complexity:** O(?)  
**Space Complexity:** O(?)  

### Optimized Approach
**Idea:**
- 

**Algorithm Steps:**
1. 
2. 
3. 

**Time Complexity:** O(?)  
**Space Complexity:** O(?)

---

## 🎨 Visual Explanation

```
Example: 

Step 1: 
Step 2: 
Step 3: 
```

---

## 💻 Implementation

```python
# Your solution here
def solution():
    pass
```

### Code Explanation
- 

---

## 🧪 Test Cases

### Test Case 1: Basic Example
```
Input: 
Expected Output: 
Actual Output: 
Status: ⏳ Not Tested
```

### Test Case 2: Edge Case - Empty Input
```
Input: 
Expected Output: 
Actual Output: 
Status: ⏳ Not Tested
```

### Test Case 3: Edge Case - Single Element
```
Input: 
Expected Output: 
Actual Output: 
Status: ⏳ Not Tested
```

---

## 📊 Complexity Analysis

### Time Complexity: O(?)
**Breakdown:**
- 

### Space Complexity: O(?)
**Breakdown:**
- 

---

## 🎓 Key Learnings

### What I Learned
1. 
2. 
3. 

### Mistakes I Made
1. 
2. 

### Pattern Insights
- When to use {pattern.replace('-', ' ')}:
- When NOT to use this pattern:

---

## 🔗 Similar Problems

1. 
2. 
3. 

---

## 📚 Resources

- [Pattern Guide](../../PATTERNS_GUIDE.md#{pattern})
- LeetCode Discussion: {leetcode_url + '/discuss/' if leetcode_url else 'N/A'}

---

## ✅ Progress Checklist

- [ ] Problem understood
- [ ] Pattern identified
- [ ] Brute force solution
- [ ] Optimized solution
- [ ] All test cases pass
- [ ] Complexity analyzed
- [ ] Code reviewed
- [ ] Learnings documented
- [ ] Jira ticket updated

---

**Status:** 🔴 Not Started  
**Last Updated:** {updated[:10]}
"""
    
    # Create pattern directory if it doesn't exist
    pattern_dir = base_path / 'problems' / pattern
    pattern_dir.mkdir(parents=True, exist_ok=True)
    
    # Write file
    file_path = pattern_dir / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return pattern, filename

def main():
    """Main function to process all Jira items."""
    base_path = Path(__file__).parent
    jira_file = base_path / 'jira-sync' / 'work-items-detailed.json'
    
    if not jira_file.exists():
        print(f"Error: {jira_file} not found!")
        return
    
    # Load Jira data
    with open(jira_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    issues = data.get('issues', [])
    print(f"Found {len(issues)} work items")
    
    # Track statistics
    pattern_counts = {}
    created_files = []
    
    # Process each issue
    for issue in issues:
        try:
            pattern, filename = create_problem_file(issue, base_path)
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
            created_files.append((issue['key'], pattern, filename))
            print(f"✓ Created: {issue['key']} -> {pattern}/{filename}")
        except Exception as e:
            print(f"✗ Error processing {issue.get('key', 'unknown')}: {e}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total problems: {len(created_files)}")
    print(f"\nProblems by pattern:")
    for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {pattern:25} {count:3} problems")
    
    # Create index file
    create_index_file(base_path, created_files, pattern_counts)
    
    print(f"\n✅ All problem files created successfully!")
    print(f"📁 Check the 'problems/' directory")

def create_index_file(base_path, created_files, pattern_counts):
    """Create an index file listing all problems."""
    content = """# Problem Index

This file lists all problems organized by pattern.

## Statistics

"""
    content += f"**Total Problems:** {len(created_files)}\n\n"
    content += "**Problems by Pattern:**\n\n"
    
    for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
        content += f"- **{pattern.replace('-', ' ').title()}:** {count} problems\n"
    
    content += "\n---\n\n"
    
    # Group by pattern
    by_pattern = {}
    for key, pattern, filename in created_files:
        if pattern not in by_pattern:
            by_pattern[pattern] = []
        by_pattern[pattern].append((key, filename))
    
    # Write each pattern section
    for pattern in sorted(by_pattern.keys()):
        content += f"## {pattern.replace('-', ' ').title()}\n\n"
        for key, filename in sorted(by_pattern[pattern]):
            problem_name = filename.replace('.md', '').replace(f'{key}-', '')
            content += f"- [{key}](problems/{pattern}/{filename}) - {problem_name.replace('-', ' ').title()}\n"
        content += "\n"
    
    # Write index file
    index_path = base_path / 'PROBLEM_INDEX.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n📋 Created PROBLEM_INDEX.md")

if __name__ == '__main__':
    main()
