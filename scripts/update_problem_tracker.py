#!/usr/bin/env python3
"""
Script to update the problem tracker in README.md
Scans all problem files and generates a status table
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_problem_info(file_path):
    """Extract title, status, difficulty, and pattern from a problem file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title (first heading)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"
        
        # Extract status
        status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?:\s*\n|\s*$)', content)
        status = status_match.group(1).strip() if status_match else "❓ Unknown"
        
        # Extract difficulty
        difficulty_match = re.search(r'\*\*Difficulty:\*\*\s*(\w+)', content)
        difficulty = difficulty_match.group(1).strip() if difficulty_match else "Unknown"
        
        # Extract pattern
        pattern_match = re.search(r'\*\*Pattern:\*\*\s*(.+?)(?:\s*\n|\s*$)', content)
        pattern = pattern_match.group(1).strip() if pattern_match else "Unknown"
        
        # Extract LeetCode link if available
        leetcode_match = re.search(r'\*\*LeetCode:\*\*\s*(https?://[^\s]+)', content)
        leetcode_url = leetcode_match.group(1).strip() if leetcode_match else None
        
        # Extract Jira ticket
        jira_match = re.search(r'\[([^\]]+)\]\((https://[^\)]+atlassian[^\)]+)\)', content)
        jira_id = jira_match.group(1) if jira_match else None
        
        return {
            'title': title,
            'status': status,
            'difficulty': difficulty,
            'pattern': pattern,
            'leetcode_url': leetcode_url,
            'jira_id': jira_id
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def get_all_problems(problems_dir):
    """Get all problem files organized by pattern"""
    problems_by_pattern = defaultdict(list)
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(problems_dir):
        for file in files:
            if file.endswith('.md') and file.startswith('LND-'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, problems_dir)
                
                info = extract_problem_info(file_path)
                if info:
                    info['file_path'] = relative_path
                    info['file_name'] = file
                    pattern = info['pattern']
                    problems_by_pattern[pattern].append(info)
    
    return problems_by_pattern

def generate_status_icon(status):
    """Convert status text to icon"""
    status_lower = status.lower()
    if '✅' in status or 'completed' in status_lower or 'done' in status_lower:
        return '✅'
    elif '🟡' in status or 'in progress' in status_lower:
        return '🟡'
    elif '🟠' in status or 'stuck' in status_lower:
        return '🟠'
    else:
        return '⏳'

def generate_difficulty_badge(difficulty):
    """Generate colored difficulty badge"""
    if difficulty.lower() == 'easy':
        return '🟢 Easy'
    elif difficulty.lower() == 'medium':
        return '🟡 Medium'
    elif difficulty.lower() == 'hard':
        return '🔴 Hard'
    else:
        return '⚪ Unknown'

def generate_progress_bar(completed, total, width=50):
    """Generate ASCII progress bar"""
    if total == 0:
        return "[" + " " * width + "] 0%"
    
    percentage = completed / total
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    percent_text = f"{int(percentage * 100)}%"
    
    return f"[{bar}] {percent_text}"

def generate_tracker_markdown(problems_by_pattern):
    """Generate markdown table for the tracker"""
    lines = []
    
    # Calculate statistics
    total = 0
    completed = 0
    easy_total = 0
    medium_total = 0
    hard_total = 0
    easy_done = 0
    medium_done = 0
    hard_done = 0
    
    for pattern in sorted(problems_by_pattern.keys()):
        problems = problems_by_pattern[pattern]
        for p in problems:
            total += 1
            is_completed = '✅' in p['status'] or 'completed' in p['status'].lower()
            
            if is_completed:
                completed += 1
            
            # Count by difficulty
            diff = p['difficulty'].lower()
            if diff == 'easy':
                easy_total += 1
                if is_completed:
                    easy_done += 1
            elif diff == 'medium':
                medium_total += 1
                if is_completed:
                    medium_done += 1
            elif diff == 'hard':
                hard_total += 1
                if is_completed:
                    hard_done += 1
    
    # Header with visual progress
    lines.append("## 📊 Problem Tracker")
    lines.append("")
    lines.append(f"### Overall Progress: {completed}/{total} Problems ({int(completed/total*100) if total > 0 else 0}%)")
    lines.append("")
    lines.append("```")
    lines.append(generate_progress_bar(completed, total, 50))
    lines.append("```")
    lines.append("")
    
    # Difficulty breakdown
    lines.append("### 📈 Progress by Difficulty")
    lines.append("")
    lines.append("| Difficulty | Solved | Total | Progress |")
    lines.append("|------------|--------|-------|----------|")
    
    if easy_total > 0:
        easy_pct = int(easy_done/easy_total*100)
        easy_bar = generate_progress_bar(easy_done, easy_total, 20)
        lines.append(f"| 🟢 Easy | {easy_done} | {easy_total} | `{easy_bar}` {easy_pct}% |")
    
    if medium_total > 0:
        medium_pct = int(medium_done/medium_total*100)
        medium_bar = generate_progress_bar(medium_done, medium_total, 20)
        lines.append(f"| 🟡 Medium | {medium_done} | {medium_total} | `{medium_bar}` {medium_pct}% |")
    
    if hard_total > 0:
        hard_pct = int(hard_done/hard_total*100)
        hard_bar = generate_progress_bar(hard_done, hard_total, 20)
        lines.append(f"| 🔴 Hard | {hard_done} | {hard_total} | `{hard_bar}` {hard_pct}% |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Quick filters section
    lines.append("### 🔍 Quick Filters")
    lines.append("")
    lines.append("**Filter by Status:**")
    lines.append("- ✅ Completed: Use browser search (Ctrl/Cmd+F) for \"✅\"")
    lines.append("- ⏳ To Do: Search for \"⏳\"")
    lines.append("- 🟡 In Progress: Search for \"🟡\"")
    lines.append("")
    lines.append("**Filter by Difficulty:**")
    lines.append("- 🟢 Easy | 🟡 Medium | 🔴 Hard")
    lines.append("")
    lines.append("**Filter by Pattern:** Jump to section below")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # By Pattern - Enhanced table
    problem_number = 1
    
    for pattern in sorted(problems_by_pattern.keys()):
        problems = sorted(problems_by_pattern[pattern], key=lambda x: x['file_name'])
        pattern_completed = sum(1 for p in problems if '✅' in p['status'] or 'completed' in p['status'].lower())
        pattern_pct = int(pattern_completed/len(problems)*100) if len(problems) > 0 else 0
        
        lines.append(f"### {pattern}")
        lines.append(f"**Progress:** {pattern_completed}/{len(problems)} completed ({pattern_pct}%)")
        lines.append("")
        
        # Enhanced table with more columns
        lines.append("| # | Status | Problem | Difficulty | Pattern | Resources | Jira | Notes |")
        lines.append("|---|--------|---------|------------|---------|-----------|------|-------|")
        
        for problem in problems:
            status_icon = generate_status_icon(problem['status'])
            difficulty_badge = generate_difficulty_badge(problem['difficulty'])
            
            # Create problem link with cleaner title
            clean_title = problem['title'].replace(' - ', ' • ')
            problem_link = f"[{clean_title}](problems/{problem['file_path']})"
            
            # Shorter pattern name for table
            pattern_short = pattern[:20] + "..." if len(pattern) > 20 else pattern
            
            # Create Jira link with icon
            if problem['jira_id']:
                jira_cell = f"[{problem['jira_id']}](https://rohitroy007.atlassian.net/browse/{problem['jira_id']})"
            else:
                jira_cell = "-"
            
            # Create resource links with icons
            resources = []
            if problem['leetcode_url']:
                resources.append(f"[📝 LC]({problem['leetcode_url']})") 
            if problem.get('solution_url'):
                resources.append(f"[💡 Sol]({problem['solution_url']})")
            if problem.get('video_url'):
                resources.append(f"[🎥 Vid]({problem['video_url']})")
            
            resource_cell = " ".join(resources) if resources else "-"
            
            # Notes placeholder
            notes_cell = "📝" if '✅' in problem['status'] or 'completed' in problem['status'].lower() else "-"
            
            lines.append(f"| {problem_number} | {status_icon} | {problem_link} | {difficulty_badge} | {pattern_short} | {resource_cell} | {jira_cell} | {notes_cell} |")
            problem_number += 1
        
        lines.append("")
    
    return "\n".join(lines)

def update_readme(tracker_content, repo_root):
    """Update README.md with the tracker content"""
    readme_path = repo_root / "README.md"
    
    if not readme_path.exists():
        print(f"README.md not found at {readme_path}")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the tracker section or create it
    tracker_start = "<!-- PROBLEM_TRACKER_START -->"
    tracker_end = "<!-- PROBLEM_TRACKER_END -->"
    
    if tracker_start in content and tracker_end in content:
        # Replace existing tracker
        pattern = re.compile(
            f"{re.escape(tracker_start)}.*?{re.escape(tracker_end)}",
            re.DOTALL
        )
        new_content = pattern.sub(
            f"{tracker_start}\n{tracker_content}\n{tracker_end}",
            content
        )
    else:
        # Add tracker at the end
        new_content = content + f"\n\n{tracker_start}\n{tracker_content}\n{tracker_end}\n"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated README.md with problem tracker")
    return True

def main():
    """Main function"""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent  # Go up one level from scripts/ to LnD/
    problems_dir = repo_root / "problems"
    
    if not problems_dir.exists():
        print(f"Error: Problems directory not found at {problems_dir}")
        return
    
    print("🔍 Scanning problem files...")
    problems_by_pattern = get_all_problems(problems_dir)
    
    print(f"📝 Found {sum(len(p) for p in problems_by_pattern.values())} problems across {len(problems_by_pattern)} patterns")
    
    print("📊 Generating tracker markdown...")
    tracker_content = generate_tracker_markdown(problems_by_pattern)
    
    print("💾 Updating README.md...")
    update_readme(tracker_content, repo_root)
    
    print("✅ Done!")

if __name__ == "__main__":
    main()
