"""
LeetCode Problem: 1 - Two Sum
Difficulty: Easy
Category: Arrays

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach:
        1. Use a hash map to store number and its index
        2. For each number, check if complement (target - current) exists in hash map
        3. If exists, return current index and complement's index
        4. If not exists, add current number and index to hash map
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  # Should never reach here based on problem constraints


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()