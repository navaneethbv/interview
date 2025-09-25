"""
LeetCode Problem: 42 - Trapping Rain Water
Difficulty: Hard
Category: Dynamic Programming

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 3 * 10^4
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach (Two Pointers):
        1. Use two pointers from left and right ends
        2. Keep track of max height seen so far from both sides
        3. Move pointer with smaller max height
        4. Water trapped at current position = min(left_max, right_max) - current_height
        5. Continue until pointers meet
        """
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped
    
    def trap_dp(self, height: List[int]) -> int:
        """
        Alternative DP Solution
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach:
        1. Pre-compute left_max and right_max arrays
        2. For each position, water = min(left_max[i], right_max[i]) - height[i]
        3. Sum up all positive water values
        """
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Fill right_max array
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate trapped water
        water_trapped = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                water_trapped += water_level - height[i]
        
        return water_trapped


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert solution.trap(height1) == 6
    assert solution.trap_dp(height1) == 6
    
    # Test case 2
    height2 = [4,2,0,3,2,5]
    assert solution.trap(height2) == 9
    assert solution.trap_dp(height2) == 9
    
    # Test case 3: No water can be trapped
    height3 = [1,2,3,4,5]
    assert solution.trap(height3) == 0
    assert solution.trap_dp(height3) == 0
    
    # Test case 4: Single element
    height4 = [5]
    assert solution.trap(height4) == 0
    assert solution.trap_dp(height4) == 0
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()