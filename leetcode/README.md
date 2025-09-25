# LeetCode Java Solutions

This directory contains Java solutions for LeetCode problems with an easy-to-use testing setup.

## Directory Structure

```
leetcode/
├── src/           # Java source files for solutions
├── test/          # Test files and test cases
├── compile.sh     # Script to compile Java files
├── run.sh         # Script to run solutions
└── README.md      # This file
```

## How to Use

### 1. Compile Java Files
```bash
./compile.sh
```

### 2. Run a Specific Solution
```bash
./run.sh <ClassName>
```

### 3. Run with Custom Input
```bash
echo "your input" | ./run.sh <ClassName>
```

## Example

1. Create your solution in `src/TwoSum.java`
2. Compile: `./compile.sh`
3. Run: `./run.sh TwoSum`

## Adding New Problems

1. Create a new Java file in the `src/` directory
2. Follow the naming convention: `ProblemName.java`
3. Include a main method for testing
4. Compile and run using the provided scripts