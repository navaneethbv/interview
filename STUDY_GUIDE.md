# LeetCode Study Guide

## 📋 Study Plan Overview

This study guide provides a structured approach to mastering algorithm and data structure problems for technical interviews.

## 🎯 Phase-Based Learning Path

### Phase 1: Foundation (2-3 weeks)
**Focus**: Basic data structures and algorithms
**Target**: Complete 30-40 easy problems

#### Week 1-2: Arrays and Strings
- **Arrays**: Two pointers, sliding window, prefix sums
- **Strings**: String manipulation, pattern matching, character counting
- **Key Problems**:
  - Two Sum (1)
  - Best Time to Buy and Sell Stock (121)
  - Valid Anagram (242)
  - Valid Parentheses (20)
  - Longest Common Prefix (14)

#### Week 3: Basic Data Structures
- **Hash Maps**: Frequency counting, fast lookups
- **Stacks**: LIFO operations, balanced parentheses
- **Queues**: BFS, level-order processing
- **Key Problems**:
  - Contains Duplicate (217)
  - Valid Parentheses (20)
  - Implement Queue using Stacks (232)

### Phase 2: Intermediate Concepts (3-4 weeks)
**Focus**: Tree/graph traversals, basic dynamic programming
**Target**: Complete 40-50 medium problems

#### Week 4-5: Trees and Recursion
- **Binary Trees**: DFS, BFS, tree properties
- **Binary Search Trees**: Search, insert, validate
- **Key Problems**:
  - Binary Tree Inorder Traversal (94)
  - Maximum Depth of Binary Tree (104)
  - Binary Tree Level Order Traversal (102)
  - Validate Binary Search Tree (98)

#### Week 6: Linked Lists
- **Operations**: Insertion, deletion, reversal
- **Two Pointers**: Fast/slow pointer technique
- **Key Problems**:
  - Reverse Linked List (206)
  - Merge Two Sorted Lists (21)
  - Linked List Cycle (141)
  - Remove Nth Node From End (19)

#### Week 7: Introduction to DP
- **Concepts**: Memoization, tabulation
- **Patterns**: 1D DP, decision making
- **Key Problems**:
  - Climbing Stairs (70)
  - House Robber (198)
  - Maximum Subarray (53)

### Phase 3: Advanced Topics (4-5 weeks)
**Focus**: Complex algorithms, optimization
**Target**: Complete 30-40 hard problems

#### Week 8-9: Advanced Dynamic Programming
- **2D DP**: Grid problems, string matching
- **Optimization**: Space optimization, bottom-up approaches
- **Key Problems**:
  - Unique Paths (62)
  - Longest Common Subsequence (1143)
  - Edit Distance (72)
  - Trapping Rain Water (42)

#### Week 10-11: Graph Algorithms
- **Traversals**: DFS, BFS on graphs
- **Shortest Path**: Dijkstra, Floyd-Warshall
- **Key Problems**:
  - Number of Islands (200)
  - Course Schedule (207)
  - Network Delay Time (743)

#### Week 12: Advanced Topics
- **Backtracking**: Constraint satisfaction
- **Bit Manipulation**: XOR, bit masking
- **Key Problems**:
  - Permutations (46)
  - N-Queens (51)
  - Single Number (136)

## 🧠 Problem-Solving Framework

### 1. Understand the Problem (5 minutes)
- Read the problem statement twice
- Identify input/output format
- Note constraints and edge cases
- Ask clarifying questions

### 2. Plan the Approach (10 minutes)
- Think of multiple approaches
- Consider time/space complexity
- Choose the optimal approach
- Outline the algorithm steps

### 3. Code the Solution (15-20 minutes)
- Start with basic structure
- Handle edge cases
- Write clean, readable code
- Add comments for complex logic

### 4. Test and Optimize (10 minutes)
- Test with provided examples
- Test edge cases
- Verify time/space complexity
- Optimize if possible

## 📊 Complexity Analysis Guide

### Time Complexity Common Patterns
- **O(1)**: Hash table lookup, array access
- **O(log n)**: Binary search, balanced tree operations
- **O(n)**: Single pass through array, linear search
- **O(n log n)**: Efficient sorting, divide and conquer
- **O(n²)**: Nested loops, bubble sort
- **O(2ⁿ)**: Recursive algorithms with branching

### Space Complexity Considerations
- **Input space**: Don't count input in space complexity
- **Auxiliary space**: Extra space used by algorithm
- **Recursion**: Stack space for recursive calls
- **Data structures**: Arrays, hash maps, trees created

## 🔧 Common Patterns and Techniques

### 1. Two Pointers
**When to use**: Array/string problems, finding pairs
**Examples**: Two Sum II, 3Sum, Container With Most Water

### 2. Sliding Window
**When to use**: Substring/subarray problems
**Examples**: Longest Substring Without Repeating Characters

### 3. Fast & Slow Pointers
**When to use**: Linked list cycles, finding middle
**Examples**: Linked List Cycle, Find Middle of Linked List

### 4. Merge Intervals
**When to use**: Overlapping intervals
**Examples**: Merge Intervals, Insert Interval

### 5. Cyclic Sort
**When to use**: Array with numbers in given range
**Examples**: Find Missing Number, Find Duplicate Number

### 6. In-place Reversal of Linked List
**When to use**: Reversing parts of linked list
**Examples**: Reverse Linked List, Reverse Nodes in k-Group

### 7. Tree BFS
**When to use**: Level-order traversal, shortest path in tree
**Examples**: Binary Tree Level Order, Minimum Depth

### 8. Tree DFS
**When to use**: Tree traversal, path sum problems
**Examples**: Path Sum, Maximum Depth

### 9. Two Heaps
**When to use**: Finding median, scheduling
**Examples**: Find Median from Data Stream

### 10. Subsets
**When to use**: Generating all combinations
**Examples**: Subsets, Permutations

### 11. Modified Binary Search
**When to use**: Sorted arrays with modifications
**Examples**: Search in Rotated Sorted Array

### 12. Top K Elements
**When to use**: Finding largest/smallest K elements
**Examples**: Kth Largest Element, Top K Frequent

### 13. K-way Merge
**When to use**: Merging multiple sorted arrays
**Examples**: Merge k Sorted Lists

### 14. Dynamic Programming
**When to use**: Optimization problems, overlapping subproblems
**Examples**: Knapsack, Fibonacci, Longest Common Subsequence

## 🚨 Common Mistakes to Avoid

1. **Not handling edge cases**: Empty inputs, single elements
2. **Integer overflow**: Use long for large calculations
3. **Array bounds**: Check indices before accessing
4. **Null pointers**: Validate inputs before use
5. **Off-by-one errors**: Careful with loop boundaries
6. **Not considering time limits**: Optimize for given constraints
7. **Forgetting to return**: Always return the required value
8. **Modifying input**: Create copy if original needed

## 📝 Interview Tips

### Before the Interview
- Practice on whiteboard/paper
- Review basic data structures
- Prepare questions to ask interviewer
- Mock interview practice

### During the Interview
- Think out loud
- Start with brute force, then optimize
- Write clean, readable code
- Test your solution
- Discuss trade-offs

### After Coding
- Walk through test cases
- Analyze time/space complexity
- Suggest optimizations
- Handle follow-up questions

## 📚 Additional Resources

- **Books**: 
  - Cracking the Coding Interview
  - Elements of Programming Interviews
  - Algorithm Design Manual

- **Online Platforms**:
  - LeetCode
  - HackerRank
  - CodeSignal
  - InterviewBit

- **Video Resources**:
  - NeetCode YouTube
  - Back to Back SWE
  - Tushar Roy

## 🎯 Success Metrics

### Daily Goals
- 2-3 problems per day consistently
- Focus on understanding over speed
- Review and optimize solutions
- Practice explaining approach

### Weekly Review
- Identify problem patterns
- Review failed attempts
- Practice similar problems
- Mock interview sessions

### Monthly Assessment
- Complete practice tests
- Analyze weak areas
- Adjust study plan
- Increase difficulty level