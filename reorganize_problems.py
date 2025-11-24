#!/usr/bin/env python3
"""
Script to reorganize problems into correct pattern directories
and update their pattern metadata.
"""

import os
import re
import shutil
from pathlib import Path

# Define the correct pattern for each problem based on LeetCode categories and problem characteristics
PROBLEM_PATTERNS = {
    # Hash Table / Array & Hashing
    "LND-27-3-valid-anagram.md": "hash-table",
    "LND-28-4-group-anagrams.md": "hash-table",
    "LND-29-1-two-sum.md": "hash-table",
    "LND-30-2-contains-duplicate.md": "hash-table",
    "LND-35-8-longest-consecutive-sequence.md": "hash-table",
    
    # String / Design
    "LND-32-7-encode-and-decode-strings.md": "string-manipulation",
    
    # Trie
    "LND-34-41-design-add-and-search-words-data-structure.md": "trie",
    "LND-20-42-word-search-ii.md": "trie",
    
    # Dynamic Programming (1-D)
    "LND-45-56-decode-ways.md": "dynamic-programming",
    "LND-47-53-house-robber-ii.md": "dynamic-programming",
    "LND-56-52-house-robber.md": "dynamic-programming",
    "LND-72-59-word-break.md": "dynamic-programming",
    "LND-73-62-longest-common-subsequence.md": "dynamic-programming",
    "LND-76-60-longest-increasing-subsequence.md": "dynamic-programming",
    "LND-78-61-unique-paths.md": "dynamic-programming",
    
    # Matrix / Math & Geometry
    "LND-89-69-rotate-image.md": "matrix",
    "LND-90-70-spiral-matrix.md": "matrix",
    "LND-94-71-set-matrix-zeroes.md": "matrix",
    
    # These are actually correct Two Pointers problems
    "LND-119-9-valid-palindrome.md": "two-pointers",
    "LND-121-10-3sum.md": "two-pointers",
    "LND-116-11-container-with-most-water.md": "two-pointers",
    "LND-117-12-best-time-to-buy-and-sell-stock.md": "two-pointers",
    "LND-132-28-remove-nth-node-from-end-of-list.md": "two-pointers",
    "LND-141-27-reorder-list.md": "two-pointers",
    "LND-1-first-task.md": "two-pointers",  # Keep as is if it's already there
}

# Pattern display names
PATTERN_NAMES = {
    "hash-table": "Hash Table / Array & Hashing",
    "string-manipulation": "String Manipulation",
    "trie": "Trie",
    "dynamic-programming": "Dynamic Programming",
    "matrix": "Matrix / Math & Geometry",
    "two-pointers": "Two Pointers",
}

def create_pattern_directories(base_dir):
    """Create missing pattern directories."""
    patterns_to_create = ["hash-table", "string-manipulation", "trie", "dynamic-programming", "matrix"]
    
    for pattern in patterns_to_create:
        pattern_dir = base_dir / pattern
        if not pattern_dir.exists():
            pattern_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {pattern_dir}")
        else:
            print(f"📁 Directory already exists: {pattern_dir}")

def update_pattern_in_file(file_path, new_pattern_name):
    """Update the Pattern field in a problem file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the Pattern line
        updated_content = re.sub(
            r'\*\*Pattern:\*\*[^\n]+',
            f'**Pattern:** {new_pattern_name}',
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def move_problem_file(source_path, dest_dir, filename):
    """Move a problem file to the correct directory."""
    dest_path = dest_dir / filename
    
    if source_path == dest_path:
        print(f"  ℹ️  {filename} already in correct location")
        return True
    
    try:
        shutil.move(str(source_path), str(dest_path))
        print(f"  ✅ Moved {filename}")
        return True
    except Exception as e:
        print(f"  ❌ Error moving {filename}: {e}")
        return False

def main():
    """Main reorganization function."""
    base_dir = Path("/Users/rohit.roy/Documents/LnD/problems")
    two_pointers_dir = base_dir / "two-pointers"
    
    print("=" * 70)
    print("🔧 PROBLEM REORGANIZATION SCRIPT")
    print("=" * 70)
    print()
    
    # Step 1: Create missing directories
    print("Step 1: Creating missing pattern directories...")
    print("-" * 70)
    create_pattern_directories(base_dir)
    print()
    
    # Step 2: Reorganize problems
    print("Step 2: Reorganizing problems...")
    print("-" * 70)
    
    moved_count = 0
    updated_count = 0
    errors = []
    
    for filename, pattern_key in PROBLEM_PATTERNS.items():
        source_path = two_pointers_dir / filename
        pattern_name = PATTERN_NAMES[pattern_key]
        dest_dir = base_dir / pattern_key
        
        if not source_path.exists():
            print(f"⚠️  File not found: {filename}")
            continue
        
        print(f"\n📄 {filename}")
        print(f"   Pattern: {pattern_name}")
        
        # Update pattern in file
        if update_pattern_in_file(source_path, pattern_name):
            updated_count += 1
            print(f"   ✅ Updated pattern metadata")
        else:
            errors.append(filename)
        
        # Move file if needed
        if pattern_key != "two-pointers":
            dest_path = dest_dir / filename
            if move_problem_file(source_path, dest_dir, filename):
                moved_count += 1
                # Update source_path for the moved file
                source_path = dest_path
    
    # Step 3: Summary
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"✅ Files updated: {updated_count}")
    print(f"✅ Files moved: {moved_count}")
    
    if errors:
        print(f"❌ Errors: {len(errors)}")
        for error in errors:
            print(f"   - {error}")
    else:
        print("✨ No errors!")
    
    print()
    print("=" * 70)
    print("🎉 Reorganization complete!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Review the changes")
    print("2. Run './update_tracker.sh' to update the README")
    print("3. Commit the changes to git")

if __name__ == "__main__":
    main()
