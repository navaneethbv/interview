"""
LeetCode Problem: 21 - Merge Two Sorted Lists
Difficulty: Easy
Category: Linked Lists

Problem Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n + m) where n and m are lengths of the lists
        Space Complexity: O(1)
        
        Approach:
        1. Create a dummy node to simplify edge cases
        2. Use two pointers to compare nodes from both lists
        3. Attach the smaller node to the result and advance pointer
        4. Handle remaining nodes from either list
        """
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        current.next = list1 or list2
        
        return dummy.next


def create_linked_list(values):
    """Helper function to create linked list from list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to list for testing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
    
    # Test case 2: Empty lists
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == []
    
    # Test case 3: One empty list
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [0]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()