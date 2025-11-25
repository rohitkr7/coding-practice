#!/usr/bin/env python3
"""
Update all references from old LND-{JiraID}-{SeqNum}-{name}.md format
to new LC-{LeetCodeNum}-{name}.md format
"""

import os
import re
from pathlib import Path

def build_mapping(problems_dir):
    """Build a mapping from old filenames to new filenames."""
    problems_path = Path(problems_dir)
    mapping = {}
    
    # Find all LC-*.md files (new format)
    pattern_dirs = [d for d in problems_path.iterdir() if d.is_dir()]
    
    for pattern_dir in pattern_dirs:
        for file_path in pattern_dir.glob("LC-*.md"):
            # Read the file to get the Jira ticket number
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract Jira ticket ID (e.g., LND-28)
                jira_match = re.search(r'\*\*Jira Ticket:\*\*\s*\[([^\]]+)\]', content)
                if jira_match:
                    jira_id = jira_match.group(1)
                    
                    # Extract LeetCode number from filename (e.g., LC-4-group-anagrams.md)
                    lc_match = re.match(r'LC-(\d+)-(.+)\.md', file_path.name)
                    if lc_match:
                        lc_num = lc_match.group(1)
                        problem_slug = lc_match.group(2)
                        
                        # Build old filename pattern
                        # Old format: LND-{JiraID}-{SeqNum}-{slug}.md
                        # We need to match any old reference with this Jira ID
                        old_pattern = f"{jira_id}-{lc_num}-{problem_slug}.md"
                        new_filename = file_path.name
                        
                        mapping[old_pattern] = new_filename
                        
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    return mapping

def update_file_references(file_path, mapping, dry_run=True):
    """Update references in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Update file path references (e.g., problems/hash-table/LND-28-4-group-anagrams.md)
        for old_name, new_name in mapping.items():
            # Pattern: problems/{pattern}/LND-{JiraID}-{SeqNum}-{slug}.md
            old_pattern = re.escape(old_name)
            pattern = rf'(problems/[^/]+/)({old_pattern})'
            
            def replacement(match):
                changes.append(f"{match.group(2)} → {new_name}")
                return match.group(1) + new_name
            
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            if not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main(dry_run=True):
    """Main function to update all references."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    problems_dir = repo_root / "problems"
    
    # Build mapping from old to new filenames
    print("Building filename mapping...")
    mapping = build_mapping(problems_dir)
    print(f"Found {len(mapping)} file mappings\n")
    
    # Files to check for references
    files_to_check = [
        repo_root / "README.md",
        repo_root / "PATTERNS_GUIDE.md",
    ]
    
    # Add all markdown files in docs/
    docs_dir = repo_root / "docs"
    if docs_dir.exists():
        files_to_check.extend(docs_dir.glob("*.md"))
    
    # Add all workflow files
    workflows_dir = repo_root / ".windsurf" / "workflows"
    if workflows_dir.exists():
        files_to_check.extend(workflows_dir.glob("*.md"))
    
    # Update references
    print(f"{'='*80}")
    print(f"Checking {len(files_to_check)} files for references...")
    print(f"{'='*80}\n")
    
    updated_files = []
    
    for file_path in files_to_check:
        if not file_path.exists():
            continue
            
        modified, changes = update_file_references(file_path, mapping, dry_run)
        
        if modified:
            updated_files.append(file_path)
            print(f"📝 {file_path.relative_to(repo_root)}")
            for change in changes[:5]:  # Show first 5 changes
                print(f"   • {change}")
            if len(changes) > 5:
                print(f"   ... and {len(changes) - 5} more changes")
            print()
    
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN - Found {len(updated_files)} files with references to update")
        print("Run with --execute to apply changes")
    else:
        print(f"✅ Updated {len(updated_files)} files")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    import sys
    
    execute = "--execute" in sys.argv
    
    if execute:
        print("⚠️  EXECUTING UPDATE OPERATION ⚠️\n")
        main(dry_run=False)
    else:
        print("🔍 DRY RUN MODE - Preview only\n")
        print("To actually update files, run with: --execute\n")
        main(dry_run=True)
