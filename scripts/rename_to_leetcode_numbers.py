#!/usr/bin/env python3
"""
Rename problem and flashcard files to use actual LeetCode problem numbers.
Uses leetcode_mappings.json to map problem slugs to LeetCode numbers.
"""

import json
import os
import re
from pathlib import Path

def load_mappings():
    """Load LeetCode problem mappings from JSON file."""
    script_dir = Path(__file__).parent
    mapping_file = script_dir / "leetcode_mappings.json"
    
    with open(mapping_file, 'r') as f:
        data = json.load(f)
    
    return data['mappings']

def extract_slug_from_filename(filename):
    """Extract the problem slug from a filename like 'LC-3-valid-anagram.md'."""
    # Pattern: LC-<number>-<slug>.md
    match = re.match(r'LC-\d+-(.*?)\.md$', filename)
    if match:
        return match.group(1)
    return None

def rename_files_in_directory(directory, mappings, dry_run=True):
    """Rename all LC-*.md files in a directory."""
    renamed_count = 0
    skipped_count = 0
    
    for file_path in Path(directory).rglob("LC-*.md"):
        filename = file_path.name
        slug = extract_slug_from_filename(filename)
        
        if not slug:
            print(f"⚠️  Skipped (couldn't extract slug): {file_path}")
            skipped_count += 1
            continue
        
        # Get the correct LeetCode number from mappings
        leetcode_num = mappings.get(slug)
        
        if not leetcode_num:
            print(f"⚠️  Skipped (no mapping found for '{slug}'): {file_path}")
            skipped_count += 1
            continue
        
        # Create new filename
        new_filename = f"LC-{leetcode_num}-{slug}.md"
        new_path = file_path.parent / new_filename
        
        # Skip if already correct
        if filename == new_filename:
            print(f"✓  Already correct: {file_path}")
            continue
        
        # Rename the file
        if dry_run:
            print(f"Would rename: {file_path.relative_to(directory)}")
            print(f"         to: {new_path.relative_to(directory)}")
        else:
            file_path.rename(new_path)
            print(f"✓  Renamed: {filename} → {new_filename}")
        
        renamed_count += 1
    
    return renamed_count, skipped_count

def main():
    """Main function to rename all problem and flashcard files."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("=" * 70)
    print("LeetCode Problem File Renamer")
    print("=" * 70)
    print()
    
    # Load mappings
    print("📚 Loading LeetCode mappings...")
    mappings = load_mappings()
    print(f"✓  Loaded {len(mappings)} problem mappings")
    print()
    
    # Dry run first
    print("🔍 DRY RUN - Scanning for files to rename...")
    print("-" * 70)
    
    problems_dir = project_root / "problems"
    flashcards_dir = project_root / "flashcards" / "individual"
    
    total_renamed = 0
    total_skipped = 0
    
    # Scan problems directory
    if problems_dir.exists():
        print(f"\n📂 Scanning: problems/")
        renamed, skipped = rename_files_in_directory(problems_dir, mappings, dry_run=True)
        total_renamed += renamed
        total_skipped += skipped
    
    # Scan flashcards directory
    if flashcards_dir.exists():
        print(f"\n📂 Scanning: flashcards/individual/")
        renamed, skipped = rename_files_in_directory(flashcards_dir, mappings, dry_run=True)
        total_renamed += renamed
        total_skipped += skipped
    
    print()
    print("=" * 70)
    print(f"Summary: {total_renamed} files will be renamed, {total_skipped} skipped")
    print("=" * 70)
    print()
    
    # Ask for confirmation
    response = input("Proceed with renaming? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n🔄 Renaming files...")
        print("-" * 70)
        
        total_renamed = 0
        
        # Rename in problems directory
        if problems_dir.exists():
            print(f"\n📂 Renaming in: problems/")
            renamed, _ = rename_files_in_directory(problems_dir, mappings, dry_run=False)
            total_renamed += renamed
        
        # Rename in flashcards directory
        if flashcards_dir.exists():
            print(f"\n📂 Renaming in: flashcards/individual/")
            renamed, _ = rename_files_in_directory(flashcards_dir, mappings, dry_run=False)
            total_renamed += renamed
        
        print()
        print("=" * 70)
        print(f"✅ Complete! Renamed {total_renamed} files")
        print("=" * 70)
    else:
        print("\n❌ Renaming cancelled.")

if __name__ == "__main__":
    main()
