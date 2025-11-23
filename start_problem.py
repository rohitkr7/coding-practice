#!/usr/bin/env python3
"""
Problem Learning Workflow Script
Automatically analyzes a problem file and generates guided learning prompts
for use with Cascade AI assistant.

Usage:
    python start_problem.py <problem_file_path>
    
Example:
    python start_problem.py problems/two-pointers/LND-30-2-contains-duplicate.md
"""

import sys
import os
import re
from pathlib import Path


def extract_problem_info(file_path):
    """Extract key information from the problem markdown file."""
    
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata using regex
    info = {
        'file_path': file_path,
        'title': '',
        'jira_ticket': '',
        'leetcode_url': '',
        'pattern': '',
        'difficulty': '',
        'status': '',
        'problem_description': '',
        'examples': []
    }
    
    # Extract title (first heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        info['title'] = title_match.group(1).strip()
    
    # Extract Jira ticket
    jira_match = re.search(r'\*\*Jira Ticket:\*\*\s*\[([^\]]+)\]', content)
    if jira_match:
        info['jira_ticket'] = jira_match.group(1)
    
    # Extract LeetCode URL
    leetcode_match = re.search(r'\*\*LeetCode:\*\*\s*(https?://[^\s]+)', content)
    if leetcode_match:
        info['leetcode_url'] = leetcode_match.group(1)
    
    # Extract Pattern
    pattern_match = re.search(r'\*\*Pattern:\*\*\s*(.+)$', content, re.MULTILINE)
    if pattern_match:
        info['pattern'] = pattern_match.group(1).strip()
    
    # Extract Difficulty
    difficulty_match = re.search(r'\*\*Difficulty:\*\*\s*(.+)$', content, re.MULTILINE)
    if difficulty_match:
        info['difficulty'] = difficulty_match.group(1).strip()
    
    # Extract Status
    status_match = re.search(r'\*\*Status:\*\*\s*(.+)$', content, re.MULTILINE)
    if status_match:
        info['status'] = status_match.group(1).strip()
    
    # Extract problem description (between Problem Statement and next section)
    desc_match = re.search(
        r'##\s+📝\s+Problem Statement\s*\n+(.*?)(?=\n##|\Z)', 
        content, 
        re.DOTALL
    )
    if desc_match:
        info['problem_description'] = desc_match.group(1).strip()
    
    return info


def generate_learning_prompt(info):
    """Generate a comprehensive learning prompt based on problem info."""
    
    prompt = f"""
🎯 **Starting New Problem: {info['title']}**

📋 **Problem Details:**
- **Pattern:** {info['pattern']}
- **Difficulty:** {info['difficulty']}
- **Status:** {info['status']}
- **LeetCode:** {info['leetcode_url']}
- **Jira:** {info['jira_ticket']}

---

🎓 **Learning Request:**

I want to learn how to solve this problem step-by-step. Please provide:

1. **Core Concepts** - What fundamental concepts do I need to understand?
2. **Pattern Recognition** - Why is this problem categorized under "{info['pattern']}"? What clues point to this pattern?
3. **Approach Analysis** - Walk me through different approaches (brute force → optimized)
4. **Key Insights** - What's the "aha!" moment or key insight that unlocks this problem?
5. **Implementation Guidance** - Guide me with hints, not complete solutions
6. **Edge Cases** - What edge cases should I consider?
7. **Complexity Analysis** - Help me understand time/space trade-offs

Remember: I want HINTS and GUIDANCE, not complete solutions. Help me learn the problem-solving patterns!

---

📄 **Problem File:** `{info['file_path']}`

Let's start! What are the core concepts I need to understand for this problem?
"""
    
    return prompt.strip()


def generate_completion_prompt(info):
    """Generate a prompt for documenting a completed solution."""
    
    prompt = f"""
✅ **Problem Completed: {info['title']}**

I've solved this problem! Can you help me document my solution with:

1. **Well-commented code** - Add comprehensive comments explaining the logic
2. **Visual walkthrough** - Step-by-step example with my solution
3. **Complexity analysis** - Detailed time/space complexity breakdown
4. **Key learnings** - What I learned and mistakes I made
5. **Test cases** - Comprehensive test cases with explanations
6. **Similar problems** - Related problems to practice this pattern
7. **Quick reference** - Template code for future reference

Please update the problem file with all this documentation so I can easily reference it later!

---

📄 **Problem File:** `{info['file_path']}`
"""
    
    return prompt.strip()


def main():
    """Main function to run the workflow."""
    
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a problem file path")
        print("\nUsage:")
        print("  python start_problem.py <problem_file_path>")
        print("\nExample:")
        print("  python start_problem.py problems/two-pointers/LND-30-2-contains-duplicate.md")
        print("\nOptions:")
        print("  --complete    Generate completion prompt (for documenting solved problems)")
        sys.exit(1)
    
    # Check for completion flag
    is_completion = '--complete' in sys.argv
    
    # Get file path (last argument that's not a flag)
    file_path = [arg for arg in sys.argv[1:] if not arg.startswith('--')][-1]
    
    # Convert to absolute path if relative
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
    
    # Extract problem information
    print(f"📖 Reading problem file: {file_path}")
    info = extract_problem_info(file_path)
    
    if not info:
        print(f"❌ Error: Could not read file: {file_path}")
        sys.exit(1)
    
    print(f"✅ Found problem: {info['title']}")
    print()
    
    # Generate appropriate prompt
    if is_completion:
        prompt = generate_completion_prompt(info)
        print("📝 **COMPLETION PROMPT** (Copy and paste to Cascade):")
    else:
        prompt = generate_learning_prompt(info)
        print("🎓 **LEARNING PROMPT** (Copy and paste to Cascade):")
    
    print()
    print("=" * 80)
    print(prompt)
    print("=" * 80)
    print()
    print("💡 Tip: Copy the above prompt and paste it into Cascade to start learning!")
    
    # Optionally copy to clipboard (if pyperclip is available)
    try:
        import pyperclip
        pyperclip.copy(prompt)
        print("✅ Prompt copied to clipboard!")
    except ImportError:
        print("💡 Install 'pyperclip' to auto-copy prompts: pip install pyperclip")


if __name__ == "__main__":
    main()
