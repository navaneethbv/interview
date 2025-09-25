#!/usr/bin/env python3
"""
Utility script to run LeetCode solutions
Usage: python utils/run_solution.py <path_to_solution.py>
"""

import sys
import os
import importlib.util
import time


def run_solution(file_path):
    """Run a LeetCode solution file"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        return False
    
    if not file_path.endswith('.py'):
        print("Error: Only Python files are supported")
        return False
    
    try:
        # Load the module
        spec = importlib.util.spec_from_file_location("solution", file_path)
        module = importlib.util.module_from_spec(spec)
        
        print(f"Running solution: {file_path}")
        print("=" * 50)
        
        start_time = time.time()
        spec.loader.exec_module(module)
        end_time = time.time()
        
        print("=" * 50)
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return True
        
    except Exception as e:
        print(f"Error running solution: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python utils/run_solution.py <path_to_solution.py>")
        print("Example: python utils/run_solution.py leetcode/easy/arrays/001_two_sum.py")
        return
    
    file_path = sys.argv[1]
    run_solution(file_path)


if __name__ == "__main__":
    main()