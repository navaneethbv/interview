# Interview Preparation Repository

A comprehensive LeetCode practice repository organized by difficulty and category to help you prepare for technical interviews.

## 📁 Repository Structure

```
leetcode/
├── easy/
│   ├── arrays/
│   ├── strings/
│   ├── linked-lists/
│   ├── trees/
│   ├── dynamic-programming/
│   ├── backtracking/
│   ├── graphs/
│   ├── sorting/
│   ├── searching/
│   └── math/
├── medium/
│   └── [same categories as easy]
└── hard/
    └── [same categories as easy]

templates/
├── python_template.py
├── java_template.java
└── javascript_template.js

utils/
├── run_solution.py      # Run individual solutions
├── test_all.py         # Run all tests
└── create_problem.py   # Create new problem files
```

## 🚀 Getting Started

### Running Solutions

Run an individual solution:
```bash
python utils/run_solution.py leetcode/easy/arrays/001_two_sum.py
```

### Running All Tests

Run all tests:
```bash
python utils/test_all.py
```

Run tests for specific difficulty:
```bash
python utils/test_all.py easy
```

Run tests for specific category:
```bash
python utils/test_all.py medium arrays
```

### Creating New Problems

Create a new problem from template:
```bash
python utils/create_problem.py easy arrays 26 remove-duplicates python
```

This creates: `leetcode/easy/arrays/026_remove_duplicates.py`

## 📚 Problem Categories

- **Arrays**: Array manipulation, sliding window, two pointers
- **Strings**: String processing, pattern matching, parsing
- **Linked Lists**: Node manipulation, cycle detection, merging
- **Trees**: Binary trees, BST, tree traversals, recursion
- **Dynamic Programming**: Memoization, tabulation, optimization
- **Backtracking**: Constraint satisfaction, permutations, combinations
- **Graphs**: BFS, DFS, shortest path, topological sort
- **Sorting**: Quick sort, merge sort, heap sort variations
- **Searching**: Binary search, linear search variations
- **Math**: Number theory, geometry, bit manipulation

## 🎯 Practice Strategy

### Phase 1: Foundation (Easy Problems)
1. Start with arrays and strings
2. Master two-pointer technique
3. Learn basic hash map usage
4. Practice simple recursion

### Phase 2: Core Concepts (Easy to Medium)
1. Linked list operations
2. Tree traversals (DFS, BFS)
3. Basic dynamic programming
4. Stack and queue problems

### Phase 3: Advanced Techniques (Medium to Hard)
1. Complex dynamic programming
2. Graph algorithms
3. Advanced data structures
4. Optimization problems

## 📋 Solution Template Structure

Each solution includes:
- **Problem description** and constraints
- **Examples** with explanations
- **Time/Space complexity** analysis
- **Approach explanation** with steps
- **Clean implementation** with comments
- **Test cases** for verification

## 🧪 Testing

All solutions include comprehensive test cases:
- Edge cases (empty inputs, single elements)
- Boundary conditions (min/max values)
- Multiple valid scenarios
- Performance validation for large inputs

## 📈 Progress Tracking

Track your progress by:
1. Completing problems in each category
2. Understanding time/space complexity
3. Implementing multiple approaches
4. Optimizing solutions
5. Writing comprehensive tests

## 🔧 Supported Languages

- **Python** (primary): Full template and utility support
- **Java**: Template available, manual testing
- **JavaScript**: Template available, manual testing

## 📖 Resources

- [LeetCode](https://leetcode.com/) - Official problem source
- [NeetCode](https://neetcode.io/) - Curated problem lists
- [AlgoExpert](https://www.algoexpert.io/) - Structured learning path
- [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/) - Classic interview prep book

## 🤝 Contributing

Feel free to:
- Add new problems and solutions
- Improve existing solutions
- Add solutions in other languages
- Enhance utility scripts
- Fix bugs or add features

## 📝 Notes

- All solutions are tested and verified
- Focus on understanding concepts, not just memorizing
- Practice explaining solutions out loud
- Time yourself during practice sessions
- Review and optimize your solutions regularly
