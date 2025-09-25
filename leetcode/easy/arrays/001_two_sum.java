/**
 * LeetCode Problem: 1 - Two Sum
 * Difficulty: Easy
 * Category: Arrays
 * 
 * Problem Description:
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * 
 * Example:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 * 
 * Constraints:
 * - 2 <= nums.length <= 10^4
 * - -10^9 <= nums[i] <= 10^9
 * - -10^9 <= target <= 10^9
 * - Only one valid answer exists.
 */

import java.util.*;

public class TwoSum {
    
    /**
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     * 
     * Approach:
     * 1. Use a HashMap to store number and its index
     * 2. For each number, check if complement (target - current) exists in HashMap
     * 3. If exists, return current index and complement's index
     * 4. If not exists, add current number and index to HashMap
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            numMap.put(nums[i], i);
        }
        
        return new int[]{}; // Should never reach here based on problem constraints
    }
    
    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        
        // Test case 1
        int[] nums1 = {2, 7, 11, 15};
        int[] result1 = solution.twoSum(nums1, 9);
        assert Arrays.equals(result1, new int[]{0, 1}) : "Test case 1 failed";
        
        // Test case 2
        int[] nums2 = {3, 2, 4};
        int[] result2 = solution.twoSum(nums2, 6);
        assert Arrays.equals(result2, new int[]{1, 2}) : "Test case 2 failed";
        
        // Test case 3
        int[] nums3 = {3, 3};
        int[] result3 = solution.twoSum(nums3, 6);
        assert Arrays.equals(result3, new int[]{0, 1}) : "Test case 3 failed";
        
        System.out.println("All test cases passed!");
    }
}