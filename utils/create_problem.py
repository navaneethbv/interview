#!/usr/bin/env python3
"""
Utility script to create a new LeetCode problem from template
Usage: python utils/create_problem.py <difficulty> <category> <problem_number> <problem_name> [language]
"""

import sys
import os
from pathlib import Path


def create_problem_file(difficulty, category, problem_number, problem_name, language="python"):
    """Create a new problem file from template"""
    
    # Validate inputs
    valid_difficulties = ["easy", "medium", "hard"]
    if difficulty not in valid_difficulties:
        print(f"Error: Difficulty must be one of {valid_difficulties}")
        return False
    
    valid_categories = [
        "arrays", "strings", "linked-lists", "trees", "dynamic-programming",
        "backtracking", "graphs", "sorting", "searching", "math"
    ]
    if category not in valid_categories:
        print(f"Error: Category must be one of {valid_categories}")
        return False
    
    # Create file name
    file_name = f"{problem_number:03d}_{problem_name.lower().replace(' ', '_').replace('-', '_')}"
    
    # Determine file extension and template
    if language == "python":
        file_extension = ".py"
        template_file = "templates/python_template.py"
    elif language == "java":
        file_extension = ".java"
        template_file = "templates/java_template.java"
    elif language == "javascript":
        file_extension = ".js"
        template_file = "templates/javascript_template.js"
    else:
        print(f"Error: Language '{language}' not supported. Use python, java, or javascript")
        return False
    
    # Create directory path
    problem_dir = Path("leetcode") / difficulty / category
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create full file path
    problem_file = problem_dir / (file_name + file_extension)
    
    if problem_file.exists():
        print(f"Error: File '{problem_file}' already exists")
        return False
    
    # Read template
    template_path = Path(template_file)
    if not template_path.exists():
        print(f"Error: Template file '{template_file}' not found")
        return False
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Replace placeholders
    problem_title = problem_name.replace('_', ' ').replace('-', ' ').title()
    template_content = template_content.replace("[Problem Number]", str(problem_number))
    template_content = template_content.replace("[Problem Title]", problem_title)
    template_content = template_content.replace("[Easy/Medium/Hard]", difficulty.title())
    template_content = template_content.replace("[Arrays/Strings/Trees/etc.]", category.title())
    
    # Write the new file
    with open(problem_file, 'w') as f:
        f.write(template_content)
    
    print(f"Created new problem file: {problem_file}")
    return True


def main():
    if len(sys.argv) < 5:
        print("Usage: python utils/create_problem.py <difficulty> <category> <problem_number> <problem_name> [language]")
        print("")
        print("Arguments:")
        print("  difficulty: easy, medium, or hard")
        print("  category: arrays, strings, linked-lists, trees, dynamic-programming, etc.")
        print("  problem_number: LeetCode problem number (e.g., 1, 15, 200)")
        print("  problem_name: Problem name (e.g., 'two-sum', 'valid-parentheses')")
        print("  language: python (default), java, or javascript")
        print("")
        print("Example:")
        print("  python utils/create_problem.py easy arrays 1 two-sum python")
        return
    
    difficulty = sys.argv[1]
    category = sys.argv[2]
    
    try:
        problem_number = int(sys.argv[3])
    except ValueError:
        print("Error: Problem number must be an integer")
        return
    
    problem_name = sys.argv[4]
    language = sys.argv[5] if len(sys.argv) > 5 else "python"
    
    create_problem_file(difficulty, category, problem_number, problem_name, language)


if __name__ == "__main__":
    main()