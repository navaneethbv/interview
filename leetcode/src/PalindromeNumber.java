/**
 * LeetCode Problem 9: Palindrome Number
 * Given an integer x, return true if x is palindrome integer.
 * An integer is a palindrome when it reads the same backward as forward.
 */
public class PalindromeNumber {
    
    public boolean isPalindrome(int x) {
        // Negative numbers are not palindromes
        if (x < 0) {
            return false;
        }
        
        // Single digit numbers are palindromes
        if (x < 10) {
            return true;
        }
        
        // Reverse the number and compare
        int original = x;
        int reversed = 0;
        
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        
        return original == reversed;
    }
    
    public static void main(String[] args) {
        PalindromeNumber solution = new PalindromeNumber();
        
        // Test cases
        int[] testCases = {121, -121, 10, 12321, 0, 1, 1001};
        boolean[] expected = {true, false, false, true, true, true, true};
        
        System.out.println("Testing Palindrome Number solution:");
        for (int i = 0; i < testCases.length; i++) {
            boolean result = solution.isPalindrome(testCases[i]);
            System.out.printf("isPalindrome(%d) = %b (expected: %b) %s%n", 
                testCases[i], result, expected[i], 
                result == expected[i] ? "✓" : "✗");
        }
    }
}