#!/usr/bin/env python3
"""
Rename problem files from Jira ID format to LeetCode number format.
Current: LND-{JiraID}-{SeqNum}-{problem-name}.md
Target: LC-{LeetCodeNum}-{problem-name}.md
"""

import os
import re
from pathlib import Path

def extract_leetcode_number(file_path):
    """Extract LeetCode problem number from the file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for LeetCode URL pattern
        # Pattern: https://leetcode.com/problems/{problem-name}
        # We need to map problem name to number from the title
        
        # Try to find LeetCode problem number from various sources:
        # 1. Check if there's a direct problem number in the URL or content
        # 2. Extract from title (e.g., "# 49 - Group Anagrams")
        
        # Method 1: Extract from title line (most reliable)
        title_match = re.search(r'^#\s+(\d+)\s+-\s+(.+)$', content, re.MULTILINE)
        if title_match:
            leetcode_num = title_match.group(1)
            problem_name = title_match.group(2).strip()
            return leetcode_num, problem_name
        
        return None, None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None

def generate_new_filename(leetcode_num, problem_name):
    """Generate new filename in format: LC-{num}-{problem-name}.md"""
    # Convert problem name to kebab-case
    slug = problem_name.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars
    slug = re.sub(r'[-\s]+', '-', slug)    # Replace spaces/hyphens with single hyphen
    slug = slug.strip('-')                  # Remove leading/trailing hyphens
    
    return f"LC-{leetcode_num}-{slug}.md"

def rename_files(problems_dir, dry_run=True):
    """Rename all problem files in the directory."""
    problems_path = Path(problems_dir)
    
    if not problems_path.exists():
        print(f"Error: Directory {problems_dir} does not exist")
        return
    
    # Find all markdown files with LND- prefix
    pattern_dirs = [d for d in problems_path.iterdir() if d.is_dir()]
    
    rename_map = []
    
    for pattern_dir in pattern_dirs:
        for file_path in pattern_dir.glob("LND-*.md"):
            leetcode_num, problem_name = extract_leetcode_number(file_path)
            
            if leetcode_num and problem_name:
                new_filename = generate_new_filename(leetcode_num, problem_name)
                new_path = file_path.parent / new_filename
                
                rename_map.append({
                    'old': file_path,
                    'new': new_path,
                    'leetcode_num': leetcode_num,
                    'problem_name': problem_name
                })
            else:
                print(f"⚠️  Could not extract LeetCode number from: {file_path.name}")
    
    # Sort by LeetCode number for better display
    rename_map.sort(key=lambda x: int(x['leetcode_num']))
    
    # Display rename plan
    print(f"\n{'='*80}")
    print(f"Found {len(rename_map)} files to rename")
    print(f"{'='*80}\n")
    
    for item in rename_map:
        print(f"LC-{item['leetcode_num']:>4} | {item['old'].name}")
        print(f"       → {item['new'].name}")
        print()
    
    if dry_run:
        print(f"\n{'='*80}")
        print("DRY RUN - No files were renamed")
        print("Run with dry_run=False to actually rename files")
        print(f"{'='*80}\n")
        return rename_map
    
    # Actually rename files
    print(f"\n{'='*80}")
    print("Renaming files...")
    print(f"{'='*80}\n")
    
    success_count = 0
    for item in rename_map:
        try:
            item['old'].rename(item['new'])
            print(f"✅ Renamed: {item['old'].name} → {item['new'].name}")
            success_count += 1
        except Exception as e:
            print(f"❌ Error renaming {item['old'].name}: {e}")
    
    print(f"\n{'='*80}")
    print(f"Successfully renamed {success_count}/{len(rename_map)} files")
    print(f"{'='*80}\n")
    
    return rename_map

if __name__ == "__main__":
    import sys
    
    # Get the problems directory
    script_dir = Path(__file__).parent
    problems_dir = script_dir.parent / "problems"
    
    # Check if --execute flag is provided
    execute = "--execute" in sys.argv
    
    if execute:
        print("⚠️  EXECUTING RENAME OPERATION ⚠️\n")
        rename_files(problems_dir, dry_run=False)
    else:
        print("🔍 DRY RUN MODE - Preview only\n")
        print("To actually rename files, run with: --execute\n")
        rename_files(problems_dir, dry_run=True)
