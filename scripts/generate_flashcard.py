#!/usr/bin/env python3
"""
Generate printable flashcards from problem files.
Creates front (problem + hints) and back (solution + complexity) cards.
"""

import os
import re
from pathlib import Path
import sys

def extract_problem_info(file_path):
    """Extract all necessary info from a problem file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract basic info
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"
        
        jira_match = re.search(r'\[([^\]]+)\]', content)
        jira_id = jira_match.group(1) if jira_match else "LND-??"
        
        difficulty_match = re.search(r'\*\*Difficulty:\*\*\s*(\w+)', content)
        difficulty = difficulty_match.group(1).strip() if difficulty_match else "Unknown"
        
        pattern_match = re.search(r'\*\*Pattern:\*\*\s*(.+?)(?:\s*\n|\s*$)', content)
        pattern = pattern_match.group(1).strip() if pattern_match else "Unknown"
        
        # Extract problem statement
        problem_match = re.search(r'## 📝 Problem Statement\s*\n\s*(.+?)(?:\n##|\Z)', content, re.DOTALL)
        problem_text = problem_match.group(1).strip() if problem_match else ""
        
        # Extract key insight
        insight_match = re.search(r'### (?:Key Insight|Why [^#]+\?)\s*\n\s*(.+?)(?:\n###|\n##|\Z)', content, re.DOTALL)
        key_insight = insight_match.group(1).strip() if insight_match else ""
        
        # Extract complexity
        time_match = re.search(r'(?:Time Complexity:|### Time Complexity:)\s*\*?\*?O\(([^)]+)\)', content)
        time_complexity = f"O({time_match.group(1)})" if time_match else "O(?)"
        
        space_match = re.search(r'(?:Space Complexity:|### Space Complexity:)\s*\*?\*?O\(([^)]+)\)', content)
        space_complexity = f"O({space_match.group(1)})" if space_match else "O(?)"
        
        # Extract solution code (Java)
        code_match = re.search(r'```java\s*\n(.*?)\n```', content, re.DOTALL)
        solution_code = code_match.group(1).strip() if code_match else ""
        
        return {
            'jira_id': jira_id,
            'title': title,
            'difficulty': difficulty,
            'pattern': pattern,
            'problem_text': problem_text,
            'key_insight': key_insight,
            'time_complexity': time_complexity,
            'space_complexity': space_complexity,
            'solution_code': solution_code,
            'file_path': file_path
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def wrap_text(text, width=45):
    """Wrap text to fit within card width"""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_length = len(word) + (1 if current_line else 0)
        if current_length + word_length <= width:
            current_line.append(word)
            current_length += word_length
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def extract_problem_summary(problem_text):
    """Extract a concise summary from problem description"""
    # Clean up the text
    text = problem_text.strip()
    
    # Try to find the core problem statement (usually first paragraph)
    # Split by double newlines or "Example" keyword
    parts = re.split(r'\n\n|Example\s*\d*:', text)
    core_statement = parts[0].strip() if parts else text
    
    # Try to find Input/Output examples
    input_match = re.search(r'Input:\s*(.+?)(?:\n|Output:|$)', text, re.DOTALL)
    output_match = re.search(r'Output:\s*(.+?)(?:\n|Example|Constraints|$)', text, re.DOTALL)
    
    summary_parts = []
    
    # Add core statement (truncated if too long)
    if core_statement:
        # Remove "Problem URL:" if present
        core_statement = re.sub(r'Problem URL:.*?(?:\n|$)', '', core_statement)
        core_statement = re.sub(r'Problem Description:', '', core_statement).strip()
        if len(core_statement) > 150:
            core_statement = core_statement[:147] + '...'
        summary_parts.append(core_statement)
    
    # Add input/output if found (one example only)
    if input_match and output_match:
        inp = input_match.group(1).strip().split('\n')[0][:50]  # First line only
        out = output_match.group(1).strip().split('\n')[0][:50]  # First line only
        summary_parts.append(f"Ex: In=[{inp}] Out=[{out}]")
    
    return ' '.join(summary_parts)

def get_pattern_hints(pattern, title):
    """Generate specific, actionable hints based on pattern"""
    pattern_lower = pattern.lower()
    
    # Pattern-specific hints
    if 'hash' in pattern_lower or 'array' in pattern_lower:
        return [
            "Have we seen this element before?",
            "What gives O(1) lookup/insert?"
        ]
    elif 'two pointer' in pattern_lower:
        return [
            "Can we use two pointers moving inward?",
            "Is the array sorted? Can we sort it?"
        ]
    elif 'sliding window' in pattern_lower:
        return [
            "What defines the window boundaries?",
            "When to expand vs. shrink window?"
        ]
    elif 'binary search' in pattern_lower:
        return [
            "What's the search space?",
            "How to eliminate half each time?"
        ]
    elif 'dfs' in pattern_lower or 'tree' in pattern_lower:
        return [
            "Base case for recursion?",
            "What to return at each node?"
        ]
    elif 'dynamic' in pattern_lower or 'dp' in pattern_lower:
        return [
            "What are the subproblems?",
            "What's the recurrence relation?"
        ]
    elif 'graph' in pattern_lower:
        return [
            "BFS or DFS? Why?",
            "How to track visited nodes?"
        ]
    else:
        # Generic but slightly better
        return [
            "What's the key observation?",
            "What data structure fits best?"
        ]

def visual_width(text):
    """Calculate visual display width accounting for wide characters like emojis"""
    width = 0
    for char in text:
        # Most emojis and special symbols are 2-width
        if ord(char) > 0x1F000:  # Emoji range
            width += 2
        else:
            width += 1
    return width

def format_card_line(text, width=50):
    """Format a line to fit exactly within card borders with proper padding"""
    # Remove any leading/trailing whitespace
    text = text.strip()
    
    # Calculate visual width
    current_width = visual_width(text)
    
    # Truncate if too long
    while current_width > width:
        text = text[:-1]
        current_width = visual_width(text)
    
    # Pad with spaces to exact width
    # Need to account for visual width difference
    visual_len = visual_width(text)
    padding_needed = width - visual_len
    
    return text + (' ' * padding_needed)

def generate_flashcard_markdown(info):
    """Generate flashcard markdown with front and back"""
    
    CARD_WIDTH = 50  # Internal width of card content
    BORDER_WIDTH = 54  # Total border width (50 content + 2 left padding + 2 right padding)
    
    # Create consistent borders
    top_border = f"┌{'─' * BORDER_WIDTH}┐"
    mid_border = f"├{'─' * BORDER_WIDTH}┤"
    bottom_border = f"└{'─' * BORDER_WIDTH}┘"
    
    # Difficulty emoji
    diff_emoji = {
        'Easy': '🟢',
        'Medium': '🟡', 
        'Hard': '🔴'
    }.get(info['difficulty'], '⚪')
    
    # Clean title (remove number prefix if exists)
    clean_title = re.sub(r'^\d+\s*-\s*', '', info['title'])
    
    # Extract concise problem summary
    problem_summary = extract_problem_summary(info['problem_text'])
    problem_lines = wrap_text(problem_summary, width=48)  # Slightly less for safety
    
    # Format problem lines for display (max 6 lines now - more space for problem)
    formatted_problem_lines = []
    for i in range(min(6, len(problem_lines))):
        formatted_problem_lines.append(format_card_line(problem_lines[i], CARD_WIDTH))
    
    # Fill remaining lines with empty space if less than 6
    while len(formatted_problem_lines) < 6:
        formatted_problem_lines.append(format_card_line('', CARD_WIDTH))
    
    # Create problem lines as separate rows
    prob_line1 = formatted_problem_lines[0]
    prob_line2 = formatted_problem_lines[1]
    prob_line3 = formatted_problem_lines[2]
    prob_line4 = formatted_problem_lines[3]
    prob_line5 = formatted_problem_lines[4]
    prob_line6 = formatted_problem_lines[5]
    
    # Extract algorithm/pseudocode - look for key code pattern
    code_lines = info['solution_code'].split('\n')
    
    # Try to find the main logic (skip imports and class declaration)
    main_logic_start = 0
    for i, line in enumerate(code_lines):
        if 'public' in line and '(' in line:  # Method signature
            main_logic_start = i
            break
    
    # Get 10 lines of actual logic (the core algorithm)
    logic_lines = code_lines[main_logic_start:main_logic_start+10]
    compact_code = '\n'.join(logic_lines)
    if len(code_lines) > main_logic_start + 10:
        compact_code += '\n    // ...'
    
    # Create pseudocode summary based on pattern
    pattern_lower = info['pattern'].lower()
    if 'hash' in pattern_lower:
        pseudo_steps = [
            '1. Create HashMap to store value→index',
            '2. For each element:',
            '   - Check if complement exists in map',
            '   - If yes: return indices',
            '   - If no: add current to map'
        ]
    elif 'two pointer' in pattern_lower:
        pseudo_steps = [
            '1. Initialize left=0, right=n-1',
            '2. While left < right:',
            '   - Check condition',
            '   - Move pointers based on comparison'
        ]
    elif 'sliding window' in pattern_lower:
        pseudo_steps = [
            '1. Initialize window boundaries',
            '2. Expand window: add right element',
            '3. Shrink window: remove left if invalid',
            '4. Track optimal answer'
        ]
    else:
        pseudo_steps = [
            '1. Identify base case',
            '2. Apply pattern logic',
            '3. Optimize with key data structure'
        ]
    
    pseudocode = '\n'.join(pseudo_steps)
    
    # Extract better key insight - look for specific patterns in the text
    insight_text = info['key_insight'][:200] if info['key_insight'] else ''
    
    # If no good insight found, create one from pattern
    if not insight_text or len(insight_text) < 20:
        pattern_lower = info['pattern'].lower()
        if 'hash' in pattern_lower:
            insight_text = 'Use HashMap to store seen elements for O(1) lookup'
        elif 'two pointer' in pattern_lower:
            insight_text = 'Use two pointers from opposite ends moving inward'
        elif 'sliding window' in pattern_lower:
            insight_text = 'Expand/shrink window based on condition'
        elif 'binary search' in pattern_lower:
            insight_text = 'Binary search on sorted space to find target'
        else:
            insight_text = 'Apply pattern to optimize brute force'
    
    insight_lines = wrap_text(insight_text, width=48)
    
    # Format insight lines (max 2 lines)
    formatted_insight_lines = []
    for i in range(min(2, len(insight_lines))):
        formatted_insight_lines.append(format_card_line(insight_lines[i], CARD_WIDTH))
    
    # Fill remaining line if only 1 insight line
    while len(formatted_insight_lines) < 2:
        formatted_insight_lines.append(format_card_line('', CARD_WIDTH))
    
    # Create insight lines as separate rows
    insight_line1 = formatted_insight_lines[0]
    insight_line2 = formatted_insight_lines[1]
    
    # Format header line with title and difficulty
    header_text = f"{info['jira_id']}  {clean_title[:30]}"
    header_line = format_card_line(f"{header_text}  {diff_emoji} {info['difficulty']}", CARD_WIDTH)
    
    # Format pattern line
    pattern_text = f"🎯 PATTERN: {info['pattern'][:35]}"
    pattern_line = format_card_line(pattern_text, CARD_WIDTH)
    
    # Get pattern-specific hints
    hints = get_pattern_hints(info['pattern'], clean_title)
    hint1 = format_card_line(f"• {hints[0]}", CARD_WIDTH)
    hint2 = format_card_line(f"• {hints[1]}", CARD_WIDTH)
    
    flashcard = f"""---
id: {info['jira_id']}
title: {clean_title}
pattern: {info['pattern']}
difficulty: {info['difficulty']}
---

# {info['jira_id']}: {clean_title}

## 🎴 FRONT (Problem)

```
{top_border}
│  {header_line}  │
{mid_border}
│  {format_card_line('', CARD_WIDTH)}  │
│  {prob_line1}  │
│  {prob_line2}  │
│  {prob_line3}  │
│  {prob_line4}  │
│  {prob_line5}  │
│  {prob_line6}  │
│  {format_card_line('', CARD_WIDTH)}  │
│  {format_card_line('💡 HINTS:', CARD_WIDTH)}  │
│  {hint1}  │
│  {hint2}  │
│  {format_card_line('', CARD_WIDTH)}  │
│  {pattern_line}  │
│  {format_card_line('', CARD_WIDTH)}  │
{bottom_border}
```

---

## 🎴 BACK (Solution)

```
{top_border}
│  {format_card_line(f"{clean_title[:30]} - SOLUTION", CARD_WIDTH)}  │
{mid_border}
│  {format_card_line('', CARD_WIDTH)}  │
│  {format_card_line('💡 KEY INSIGHT:', CARD_WIDTH)}  │
│  {insight_line1}  │
│  {insight_line2}  │
│  {format_card_line('', CARD_WIDTH)}  │
│  {format_card_line('🔢 ALGORITHM:', CARD_WIDTH)}  │
│  {format_card_line(pseudo_steps[0] if len(pseudo_steps) > 0 else '', CARD_WIDTH)}  │
│  {format_card_line(pseudo_steps[1] if len(pseudo_steps) > 1 else '', CARD_WIDTH)}  │
│  {format_card_line(pseudo_steps[2] if len(pseudo_steps) > 2 else '', CARD_WIDTH)}  │
│  {format_card_line(pseudo_steps[3] if len(pseudo_steps) > 3 else '', CARD_WIDTH)}  │
│  {format_card_line(pseudo_steps[4] if len(pseudo_steps) > 4 else '', CARD_WIDTH)}  │
│  {format_card_line('', CARD_WIDTH)}  │
│  {format_card_line(f"⏱️  {info['time_complexity']}  💾 {info['space_complexity']}", CARD_WIDTH)}  │
│  {format_card_line('', CARD_WIDTH)}  │
{bottom_border}
```

---

**Print Instructions:**
- Cut along the dotted lines
- Fold in half (front/back)
- Use for spaced repetition review
"""
    
    return flashcard

def generate_print_html(flashcards_dir):
    """Generate a single HTML file for printing all flashcards"""
    
    flashcards = []
    individual_dir = flashcards_dir / 'individual'
    
    for md_file in sorted(individual_dir.glob('*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract front and back sections
            flashcards.append(content)
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode Flashcards - Print Ready</title>
    <style>
        @page {
            size: 4in 6in;
            margin: 0;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.3;
        }
        
        .flashcard {
            width: 4in;
            height: 6in;
            border: 2px solid #333;
            page-break-after: always;
            padding: 0.25in;
            position: relative;
            background: white;
        }
        
        .flashcard.front {
            background: #f8f9fa;
        }
        
        .flashcard.back {
            background: #e9ecef;
        }
        
        .flashcard.easy { border-color: #28a745; }
        .flashcard.medium { border-color: #ffc107; }
        .flashcard.hard { border-color: #dc3545; }
        
        .header {
            font-weight: bold;
            font-size: 10pt;
            padding-bottom: 0.1in;
            border-bottom: 1px solid #666;
            margin-bottom: 0.15in;
        }
        
        .content {
            font-size: 8pt;
            white-space: pre-wrap;
        }
        
        .hints, .solution {
            margin-top: 0.15in;
            padding-top: 0.15in;
            border-top: 1px dashed #999;
        }
        
        .complexity {
            position: absolute;
            bottom: 0.25in;
            left: 0.25in;
            right: 0.25in;
            padding-top: 0.1in;
            border-top: 1px solid #999;
            font-size: 8pt;
            font-weight: bold;
        }
        
        code {
            background: #f4f4f4;
            padding: 0.05in;
            font-size: 7pt;
        }
        
        @media screen {
            body {
                background: #ddd;
                padding: 20px;
            }
            .flashcard {
                margin: 20px auto;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
        }
        
        @media print {
            body {
                background: white;
            }
            .no-print {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="no-print" style="text-align: center; padding: 20px; background: white; margin-bottom: 20px;">
        <h1>🎴 LeetCode Flashcards</h1>
        <p><strong>Print Instructions:</strong> File → Print → Select "Print Backgrounds" → Print</p>
        <p>Each problem has 2 cards: Front (Problem) and Back (Solution)</p>
    </div>
"""
    
    # Add flashcard HTML for each problem
    html += f"<p class='no-print'>Total flashcards: {len(flashcards) * 2}</p>\n"
    html += "</body></html>"
    
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_flashcard.py <problem-file.md>")
        print("   or: python generate_flashcard.py --all")
        sys.exit(1)
    
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    problems_dir = repo_root / 'problems'
    flashcards_dir = repo_root / 'flashcards'
    
    if sys.argv[1] == '--all':
        # Generate flashcards for all completed problems
        print("🎴 Generating flashcards for all completed problems...")
        count = 0
        for problem_file in problems_dir.rglob('*.md'):
            with open(problem_file, 'r', encoding='utf-8') as f:
                if '✅ Completed' in f.read():
                    info = extract_problem_info(problem_file)
                    if info:
                        flashcard_md = generate_flashcard_markdown(info)
                        output_file = flashcards_dir / 'individual' / f"{info['jira_id']}-{info['title'].replace(' ', '-').lower()}.md"
                        with open(output_file, 'w', encoding='utf-8') as out:
                            out.write(flashcard_md)
                        print(f"  ✅ {info['jira_id']}: {info['title']}")
                        count += 1
        
        # Generate print-all HTML
        html = generate_print_html(flashcards_dir)
        with open(flashcards_dir / 'print-all.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n✅ Generated {count} flashcards!")
        print(f"📄 Open flashcards/print-all.html to print all cards")
    else:
        # Generate flashcard for specific problem
        problem_file = Path(sys.argv[1])
        if not problem_file.exists():
            print(f"Error: File not found: {problem_file}")
            sys.exit(1)
        
        info = extract_problem_info(problem_file)
        if not info:
            print("Failed to extract problem information")
            sys.exit(1)
        
        flashcard_md = generate_flashcard_markdown(info)
        output_file = flashcards_dir / 'individual' / f"{info['jira_id']}-{info['title'].replace(' ', '-').lower()}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(flashcard_md)
        
        print(f"✅ Flashcard generated: {output_file}")

if __name__ == '__main__':
    main()
