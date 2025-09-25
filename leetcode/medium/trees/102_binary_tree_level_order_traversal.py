"""
LeetCode Problem: 102 - Binary Tree Level Order Traversal
Difficulty: Medium
Category: Trees

Problem Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        
        Approach:
        1. Use BFS with a queue to traverse level by level
        2. Process all nodes at current level before moving to next
        3. Keep track of level size to group nodes correctly
        4. Add node values to current level list
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result


def create_binary_tree(values):
    """Helper function to create binary tree from list of values (level order)"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    root1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.levelOrder(root1)
    assert result1 == [[3], [9, 20], [15, 7]]
    
    # Test case 2: Single node
    root2 = create_binary_tree([1])
    result2 = solution.levelOrder(root2)
    assert result2 == [[1]]
    
    # Test case 3: Empty tree
    root3 = create_binary_tree([])
    result3 = solution.levelOrder(root3)
    assert result3 == []
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()