#!/usr/bin/env python3
"""
Utility script to run all LeetCode solution tests
Usage: python utils/test_all.py [difficulty] [category]
"""

import os
import sys
import importlib.util
import time
from pathlib import Path


def find_python_files(directory, difficulty=None, category=None):
    """Find all Python solution files"""
    files = []
    leetcode_dir = Path(directory) / "leetcode"
    
    if not leetcode_dir.exists():
        print("No leetcode directory found")
        return files
    
    # Determine directories to search
    if difficulty:
        search_dirs = [leetcode_dir / difficulty]
    else:
        search_dirs = [leetcode_dir / d for d in ["easy", "medium", "hard"] if (leetcode_dir / d).exists()]
    
    for diff_dir in search_dirs:
        if not diff_dir.exists():
            continue
            
        if category:
            cat_dirs = [diff_dir / category]
        else:
            cat_dirs = [d for d in diff_dir.iterdir() if d.is_dir()]
        
        for cat_dir in cat_dirs:
            if not cat_dir.exists():
                continue
            for py_file in cat_dir.glob("*.py"):
                files.append(py_file)
    
    return sorted(files)


def run_test_file(file_path):
    """Run tests for a single file"""
    try:
        spec = importlib.util.spec_from_file_location("solution", file_path)
        module = importlib.util.module_from_spec(spec)
        
        # Redirect stdout to capture print statements
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            spec.loader.exec_module(module)
        
        output = f.getvalue()
        return True, output
        
    except Exception as e:
        return False, str(e)


def main():
    current_dir = os.getcwd()
    
    # Parse command line arguments
    difficulty = None
    category = None
    
    if len(sys.argv) > 1:
        difficulty = sys.argv[1]
    if len(sys.argv) > 2:
        category = sys.argv[2]
    
    # Find all Python files
    python_files = find_python_files(current_dir, difficulty, category)
    
    if not python_files:
        print("No Python solution files found")
        return
    
    print(f"Found {len(python_files)} solution files")
    print("=" * 60)
    
    passed = 0
    failed = 0
    total_time = 0
    
    for file_path in python_files:
        relative_path = file_path.relative_to(current_dir)
        print(f"Testing: {relative_path}")
        
        start_time = time.time()
        success, output = run_test_file(file_path)
        end_time = time.time()
        
        execution_time = end_time - start_time
        total_time += execution_time
        
        if success:
            passed += 1
            print(f"✅ PASSED ({execution_time:.3f}s)")
            if output.strip():
                print(f"   Output: {output.strip()}")
        else:
            failed += 1
            print(f"❌ FAILED ({execution_time:.3f}s)")
            print(f"   Error: {output}")
        
        print("-" * 40)
    
    print("=" * 60)
    print(f"Summary: {passed} passed, {failed} failed")
    print(f"Total execution time: {total_time:.3f}s")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()