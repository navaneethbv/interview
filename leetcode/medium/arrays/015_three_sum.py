"""
LeetCode Problem: 15 - 3Sum
Difficulty: Medium
Category: Arrays

Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n²)
        Space Complexity: O(1) if we don't count the output array
        
        Approach:
        1. Sort the array to enable two-pointer technique
        2. For each element, use two pointers to find pairs that sum to negative of current element
        3. Skip duplicates to avoid duplicate triplets
        4. Use left and right pointers to find valid combinations
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    result1 = solution.threeSum([-1, 0, 1, 2, -1, -4])
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result1) == sorted(expected1)
    
    # Test case 2
    result2 = solution.threeSum([0, 1, 1])
    expected2 = []
    assert result2 == expected2
    
    # Test case 3
    result3 = solution.threeSum([0, 0, 0])
    expected3 = [[0, 0, 0]]
    assert result3 == expected3
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()