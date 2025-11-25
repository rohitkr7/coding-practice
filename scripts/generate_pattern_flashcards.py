#!/usr/bin/env python3
"""
Generate flashcards for coding patterns.
Creates one flashcard per pattern with key characteristics, when to use, and example problems.
"""

import os
from pathlib import Path

# Pattern information based on the 16 coding patterns from your guide
PATTERNS = {
    "Hash Table / Array & Hashing": {
        "key_concept": "Use HashMap/HashSet for O(1) lookup and frequency tracking",
        "when_to_use": [
            "Need to track seen elements",
            "Count frequencies",
            "Find pairs/complements",
            "Detect duplicates"
        ],
        "time_complexity": "O(n) for single pass",
        "space_complexity": "O(n) for storing elements",
        "key_operations": [
            "map.put(key, value)",
            "map.containsKey(key)",
            "map.get(key)",
            "set.add(element)"
        ],
        "common_problems": [
            "Two Sum (#1)",
            "Contains Duplicate (#217)",
            "Valid Anagram (#242)",
            "Group Anagrams (#49)"
        ]
    },
    "Two Pointers": {
        "key_concept": "Use two pointers moving towards each other or in same direction",
        "when_to_use": [
            "Sorted array problems",
            "Find pairs with target sum",
            "Remove duplicates in-place",
            "Reverse operations"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(1) constant space",
        "key_operations": [
            "left = 0, right = n-1",
            "while (left < right)",
            "Compare arr[left] + arr[right]",
            "Move pointers based on condition"
        ],
        "common_problems": [
            "Two Sum II (#167)",
            "3Sum (#15)",
            "Container With Most Water (#11)",
            "Valid Palindrome (#125)"
        ]
    },
    "Sliding Window": {
        "key_concept": "Maintain a window that slides through array/string",
        "when_to_use": [
            "Subarray/substring problems",
            "Find max/min in window",
            "Contiguous elements",
            "Fixed or variable window size"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(k) for window data",
        "key_operations": [
            "Expand window: add right element",
            "Shrink window: remove left element",
            "Track window state (sum, count, etc)",
            "Update result when valid"
        ],
        "common_problems": [
            "Max Sum Subarray of Size K",
            "Longest Substring Without Repeating",
            "Minimum Window Substring (#76)",
            "Sliding Window Maximum (#239)"
        ]
    },
    "Binary Search": {
        "key_concept": "Divide search space in half each iteration",
        "when_to_use": [
            "Sorted array search",
            "Find target or insertion point",
            "Search in rotated array",
            "Minimize/maximize with condition"
        ],
        "time_complexity": "O(log n) logarithmic",
        "space_complexity": "O(1) iterative, O(log n) recursive",
        "key_operations": [
            "left = 0, right = n-1",
            "mid = left + (right - left) / 2",
            "Compare arr[mid] with target",
            "Adjust left or right pointer"
        ],
        "common_problems": [
            "Binary Search (#704)",
            "Search Insert Position (#35)",
            "Find Peak Element (#162)",
            "Search in Rotated Array (#33)"
        ]
    },
    "Dynamic Programming": {
        "key_concept": "Break problem into overlapping subproblems, store results",
        "when_to_use": [
            "Optimization problems (min/max)",
            "Counting problems",
            "Overlapping subproblems",
            "Optimal substructure exists"
        ],
        "time_complexity": "O(n²) or O(n×m) typically",
        "space_complexity": "O(n) or O(n×m) for DP table",
        "key_operations": [
            "Define dp[i] meaning",
            "Find recurrence relation",
            "Initialize base cases",
            "Fill dp table bottom-up"
        ],
        "common_problems": [
            "Climbing Stairs (#70)",
            "House Robber (#198)",
            "Coin Change (#322)",
            "Longest Common Subsequence (#1143)"
        ]
    },
    "Fast & Slow Pointers": {
        "key_concept": "Two pointers moving at different speeds to detect cycles",
        "when_to_use": [
            "Detect cycles in linked list",
            "Find middle of linked list",
            "Detect loop start point",
            "Happy number problems"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(1) constant space",
        "key_operations": [
            "slow = slow.next",
            "fast = fast.next.next",
            "if (slow == fast) cycle exists",
            "Reset one pointer to find start"
        ],
        "common_problems": [
            "Linked List Cycle (#141)",
            "Happy Number (#202)",
            "Middle of Linked List (#876)",
            "Find Duplicate Number (#287)"
        ]
    },
    "Merge Intervals": {
        "key_concept": "Sort intervals and merge overlapping ones",
        "when_to_use": [
            "Overlapping intervals",
            "Scheduling conflicts",
            "Range merging",
            "Time slot problems"
        ],
        "time_complexity": "O(n log n) for sorting",
        "space_complexity": "O(n) for result",
        "key_operations": [
            "Sort intervals by start time",
            "Compare current.end with next.start",
            "Merge if overlapping",
            "Add non-overlapping to result"
        ],
        "common_problems": [
            "Merge Intervals (#56)",
            "Insert Interval (#57)",
            "Meeting Rooms (#252)",
            "Non-overlapping Intervals (#435)"
        ]
    },
    "Cyclic Sort": {
        "key_concept": "Place each number at its correct index in O(n)",
        "when_to_use": [
            "Array contains 1 to n",
            "Find missing/duplicate numbers",
            "In-place sorting needed",
            "Numbers in specific range"
        ],
        "time_complexity": "O(n) linear time",
        "space_complexity": "O(1) in-place",
        "key_operations": [
            "while (nums[i] != i+1)",
            "swap nums[i] with nums[nums[i]-1]",
            "Place each number at index num-1",
            "Identify misplaced numbers"
        ],
        "common_problems": [
            "Missing Number (#268)",
            "Find All Duplicates (#442)",
            "Find Duplicate Number (#287)",
            "First Missing Positive (#41)"
        ]
    },
    "In-place Reversal of LinkedList": {
        "key_concept": "Reverse linked list pointers in-place",
        "when_to_use": [
            "Reverse entire list",
            "Reverse sublist",
            "Reverse in groups",
            "Palindrome check"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(1) in-place",
        "key_operations": [
            "prev = null, curr = head",
            "next = curr.next",
            "curr.next = prev",
            "prev = curr, curr = next"
        ],
        "common_problems": [
            "Reverse Linked List (#206)",
            "Reverse Linked List II (#92)",
            "Reverse Nodes in k-Group (#25)",
            "Palindrome Linked List (#234)"
        ]
    },
    "Tree BFS": {
        "key_concept": "Level-order traversal using queue",
        "when_to_use": [
            "Level-by-level traversal",
            "Find level information",
            "Shortest path in tree",
            "Connect level nodes"
        ],
        "time_complexity": "O(n) visit all nodes",
        "space_complexity": "O(w) width of tree",
        "key_operations": [
            "Queue<Node> queue = new LinkedList()",
            "queue.offer(root)",
            "int levelSize = queue.size()",
            "Process level, add children"
        ],
        "common_problems": [
            "Binary Tree Level Order (#102)",
            "Zigzag Level Order (#103)",
            "Right Side View (#199)",
            "Minimum Depth (#111)"
        ]
    },
    "Tree DFS": {
        "key_concept": "Depth-first traversal (preorder/inorder/postorder)",
        "when_to_use": [
            "Path problems",
            "Tree height/depth",
            "Validate tree properties",
            "Serialize/deserialize"
        ],
        "time_complexity": "O(n) visit all nodes",
        "space_complexity": "O(h) recursion stack",
        "key_operations": [
            "Base case: if (node == null)",
            "Process current node",
            "Recurse left: dfs(node.left)",
            "Recurse right: dfs(node.right)"
        ],
        "common_problems": [
            "Maximum Depth (#104)",
            "Path Sum (#112)",
            "Diameter of Tree (#543)",
            "Lowest Common Ancestor (#236)"
        ]
    },
    "Heaps / Priority Queue": {
        "key_concept": "Maintain sorted order with O(log n) operations",
        "when_to_use": [
            "Find K largest/smallest",
            "Merge K sorted lists",
            "Median of stream",
            "Top K frequent elements"
        ],
        "time_complexity": "O(n log k) for K elements",
        "space_complexity": "O(k) for heap",
        "key_operations": [
            "PriorityQueue<Integer> heap",
            "heap.offer(element)",
            "heap.poll() // remove min/max",
            "heap.peek() // view min/max"
        ],
        "common_problems": [
            "Kth Largest Element (#215)",
            "Top K Frequent (#347)",
            "Merge K Sorted Lists (#23)",
            "Find Median from Stream (#295)"
        ]
    },
    "Subsets": {
        "key_concept": "Generate all combinations using backtracking",
        "when_to_use": [
            "All possible combinations",
            "Permutations",
            "Subset generation",
            "Combination sum"
        ],
        "time_complexity": "O(2^n) exponential",
        "space_complexity": "O(n) recursion depth",
        "key_operations": [
            "backtrack(current, start)",
            "Add current to result",
            "for i in start to n",
            "backtrack with i+1"
        ],
        "common_problems": [
            "Subsets (#78)",
            "Subsets II (#90)",
            "Permutations (#46)",
            "Combination Sum (#39)"
        ]
    },
    "Modified Binary Search": {
        "key_concept": "Binary search on modified/rotated arrays",
        "when_to_use": [
            "Rotated sorted array",
            "Find peak element",
            "Search in matrix",
            "Find minimum in rotated"
        ],
        "time_complexity": "O(log n) logarithmic",
        "space_complexity": "O(1) constant",
        "key_operations": [
            "Identify sorted half",
            "Check if target in sorted half",
            "Adjust left/right accordingly",
            "Handle rotation point"
        ],
        "common_problems": [
            "Search Rotated Array (#33)",
            "Find Minimum Rotated (#153)",
            "Search 2D Matrix (#74)",
            "Find Peak Element (#162)"
        ]
    },
    "Bitwise XOR": {
        "key_concept": "Use XOR properties: a^a=0, a^0=a",
        "when_to_use": [
            "Find unique element",
            "Missing number",
            "Bit manipulation",
            "Pairs cancellation"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(1) constant",
        "key_operations": [
            "result = 0",
            "result ^= num (for each num)",
            "Pairs cancel out",
            "Unique remains"
        ],
        "common_problems": [
            "Single Number (#136)",
            "Single Number II (#137)",
            "Missing Number (#268)",
            "Find Duplicate (#287)"
        ]
    },
    "Top K Elements": {
        "key_concept": "Use heap to efficiently find K largest/smallest",
        "when_to_use": [
            "Find K largest/smallest",
            "K closest points",
            "K frequent elements",
            "Kth largest/smallest"
        ],
        "time_complexity": "O(n log k)",
        "space_complexity": "O(k) for heap",
        "key_operations": [
            "Min heap for K largest",
            "Max heap for K smallest",
            "Maintain heap size K",
            "Poll/offer as needed"
        ],
        "common_problems": [
            "Kth Largest (#215)",
            "Top K Frequent (#347)",
            "K Closest Points (#973)",
            "Kth Smallest in Matrix (#378)"
        ]
    },
    "K-way Merge": {
        "key_concept": "Merge K sorted arrays/lists using min heap",
        "when_to_use": [
            "Merge K sorted lists",
            "Smallest range from K lists",
            "Kth smallest in sorted matrix",
            "Merge sorted files"
        ],
        "time_complexity": "O(n log k)",
        "space_complexity": "O(k) for heap",
        "key_operations": [
            "Add first element from each list",
            "Poll minimum from heap",
            "Add next from same list",
            "Repeat until all merged"
        ],
        "common_problems": [
            "Merge K Sorted Lists (#23)",
            "Kth Smallest Matrix (#378)",
            "Smallest Range K Lists (#632)",
            "Find K Pairs Smallest Sums (#373)"
        ]
    },
    "Topological Sort": {
        "key_concept": "Order nodes in DAG based on dependencies",
        "when_to_use": [
            "Task scheduling",
            "Course prerequisites",
            "Build dependencies",
            "Directed acyclic graph"
        ],
        "time_complexity": "O(V + E) vertices + edges",
        "space_complexity": "O(V) for graph storage",
        "key_operations": [
            "Calculate in-degree for each node",
            "Queue nodes with in-degree 0",
            "Process and reduce in-degree",
            "Detect cycle if not all processed"
        ],
        "common_problems": [
            "Course Schedule (#207)",
            "Course Schedule II (#210)",
            "Alien Dictionary (#269)",
            "Sequence Reconstruction (#444)"
        ]
    },
    "Monotonic Stack": {
        "key_concept": "Maintain stack in increasing/decreasing order",
        "when_to_use": [
            "Next greater/smaller element",
            "Stock span problems",
            "Histogram area",
            "Temperature problems"
        ],
        "time_complexity": "O(n) single pass",
        "space_complexity": "O(n) for stack",
        "key_operations": [
            "Stack<Integer> stack",
            "while (!stack.empty() && condition)",
            "stack.pop() // violates monotonic",
            "stack.push(current)"
        ],
        "common_problems": [
            "Next Greater Element (#496)",
            "Daily Temperatures (#739)",
            "Largest Rectangle Histogram (#84)",
            "Trapping Rain Water (#42)"
        ]
    }
}

def visual_width(text):
    """Calculate visual display width accounting for emojis"""
    width = 0
    for char in text:
        if ord(char) > 0x1F000:  # Emoji range
            width += 2
        else:
            width += 1
    return width

def format_line(text, width=50):
    """Format a line to exact width with padding"""
    text = text.strip()
    current_width = visual_width(text)
    
    while current_width > width:
        text = text[:-1]
        current_width = visual_width(text)
    
    padding_needed = width - visual_width(text)
    return text + (' ' * padding_needed)

def wrap_text(text, width=48):
    """Wrap text to fit within width"""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_len = len(word)
        if current_length + word_len + len(current_line) <= width:
            current_line.append(word)
            current_length += word_len
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = word_len
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def generate_pattern_flashcard(pattern_name, pattern_info):
    """Generate a flashcard for a coding pattern"""
    
    CARD_WIDTH = 50
    BORDER_WIDTH = 54
    
    top_border = f"┌{'─' * BORDER_WIDTH}┐"
    mid_border = f"├{'─' * BORDER_WIDTH}┤"
    bottom_border = f"└{'─' * BORDER_WIDTH}┘"
    
    # Format pattern name for header
    header_line = format_line(f"PATTERN: {pattern_name[:35]}", CARD_WIDTH)
    
    # Format key concept (wrap if needed)
    concept_lines = wrap_text(pattern_info['key_concept'], 48)
    concept_line1 = format_line(concept_lines[0] if len(concept_lines) > 0 else '', CARD_WIDTH)
    concept_line2 = format_line(concept_lines[1] if len(concept_lines) > 1 else '', CARD_WIDTH)
    
    # Format when to use (first 3)
    when_lines = []
    for i in range(min(3, len(pattern_info['when_to_use']))):
        when_lines.append(format_line(f"• {pattern_info['when_to_use'][i][:46]}", CARD_WIDTH))
    while len(when_lines) < 3:
        when_lines.append(format_line('', CARD_WIDTH))
    
    # Format example problems (first 3)
    example_lines = []
    for i in range(min(3, len(pattern_info['common_problems']))):
        example_lines.append(format_line(f"• {pattern_info['common_problems'][i][:46]}", CARD_WIDTH))
    while len(example_lines) < 3:
        example_lines.append(format_line('', CARD_WIDTH))
    
    # Format operations (first 3)
    op_lines = []
    for i in range(min(3, len(pattern_info['key_operations']))):
        op_lines.append(format_line(f"• {pattern_info['key_operations'][i][:46]}", CARD_WIDTH))
    while len(op_lines) < 3:
        op_lines.append(format_line('', CARD_WIDTH))
    
    flashcard = f"""---
pattern: {pattern_name}
type: pattern_reference
---

# Pattern: {pattern_name}

## 🎴 FRONT (Pattern Overview)

```
{top_border}
│  {header_line}  │
{mid_border}
│  {format_line('', CARD_WIDTH)}  │
│  {format_line('🎯 KEY CONCEPT:', CARD_WIDTH)}  │
│  {concept_line1}  │
│  {concept_line2}  │
│  {format_line('', CARD_WIDTH)}  │
│  {format_line('📌 WHEN TO USE:', CARD_WIDTH)}  │
│  {when_lines[0]}  │
│  {when_lines[1]}  │
│  {when_lines[2]}  │
│  {format_line('', CARD_WIDTH)}  │
│  {format_line('💡 EXAMPLE PROBLEMS:', CARD_WIDTH)}  │
│  {example_lines[0]}  │
│  {example_lines[1]}  │
│  {example_lines[2]}  │
│  {format_line('', CARD_WIDTH)}  │
{bottom_border}
```

---

## 🎴 BACK (Implementation)

```
{top_border}
│  {format_line(f"{pattern_name[:40]} - DETAILS", CARD_WIDTH)}  │
{mid_border}
│  {format_line('', CARD_WIDTH)}  │
│  {format_line('🔧 KEY OPERATIONS:', CARD_WIDTH)}  │
│  {op_lines[0]}  │
│  {op_lines[1]}  │
│  {op_lines[2]}  │
│  {format_line('', CARD_WIDTH)}  │
│  {format_line(f"⏱️  TIME:  {pattern_info['time_complexity'][:30]}", CARD_WIDTH)}  │
│  {format_line(f"💾 SPACE: {pattern_info['space_complexity'][:30]}", CARD_WIDTH)}  │
│  {format_line('', CARD_WIDTH)}  │
│  {format_line('✅ RECOGNITION TIPS:', CARD_WIDTH)}  │
│  {when_lines[0]}  │
│  {when_lines[1]}  │
│  {format_line('', CARD_WIDTH)}  │
{bottom_border}
```

---
"""
    
    return flashcard

def main():
    # Get the flashcards directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    flashcards_dir = repo_root / 'flashcards'
    by_pattern_dir = flashcards_dir / 'by-pattern'
    
    # Create by-pattern directory if it doesn't exist
    by_pattern_dir.mkdir(parents=True, exist_ok=True)
    
    print("🎴 Generating pattern flashcards...")
    
    # Generate flashcard for each pattern
    for pattern_name, pattern_info in PATTERNS.items():
        # Create safe filename
        safe_name = pattern_name.lower().replace('/', '-').replace(' ', '-')
        output_file = by_pattern_dir / f"{safe_name}.md"
        
        # Generate flashcard content
        flashcard_content = generate_pattern_flashcard(pattern_name, pattern_info)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(flashcard_content)
        
        print(f"  ✅ {pattern_name}")
    
    print(f"\n✅ Generated {len(PATTERNS)} pattern flashcards!")
    print(f"📁 Saved to: {by_pattern_dir}")
    print(f"\n💡 These flashcards help you remember pattern characteristics")
    print(f"   and when to apply each pattern!")

if __name__ == '__main__':
    main()
