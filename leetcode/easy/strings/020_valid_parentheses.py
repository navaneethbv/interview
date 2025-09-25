"""
LeetCode Problem: 20 - Valid Parentheses
Difficulty: Easy
Category: Strings

Problem Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach:
        1. Use a stack to keep track of opening brackets
        2. When encountering opening bracket, push to stack
        3. When encountering closing bracket, check if it matches top of stack
        4. If matches, pop from stack; if not, return False
        5. At the end, stack should be empty for valid parentheses
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return not stack  # True if stack is empty


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    assert solution.isValid("()") == True
    
    # Test case 2
    assert solution.isValid("()[]{}")== True
    
    # Test case 3
    assert solution.isValid("(]") == False
    
    # Test case 4
    assert solution.isValid("([)]") == False
    
    # Test case 5
    assert solution.isValid("{[]}") == True
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()