# Intuition
#To solve this problem, we need to swap the values of kth node from the beginning and kth node from the end of a given linked list.

# Approach
#We can use a two-pass approach to solve this problem. In the first pass, we can find the kth node from the beginning of the list, and in the second pass, we can find the kth node from the end of the list. Once we have found both nodes, we can simply swap their values.

#We can find the kth node from the beginning of the list by traversing the list k-1 times. Similarly, we can find the kth node from the end of the list by traversing the list n-k times, where n is the length of the list.

# Complexity
#- Time complexity:
#O(n), where n is the length of the linked list. I need to traverse the linked list twice, once to find the kth node from the beginning and once to find the kth node from the end. Each traversal takes O(n) time.

#- Space complexity:
#O(1)

# Code in Python
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Find the length of the linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
    # Find the kth node from the beginning
        curr = head
        for i in range(k-1):
            curr = curr.next
        kth_from_beginning = curr
    
    # Find the kth node from the end
        curr = head
        for i in range(n-k):
            curr = curr.next
        kth_from_end = curr
    
    # Swap the values of the two nodes
        kth_from_beginning.val, kth_from_end.val = kth_from_end.val, kth_from_beginning.val
    
        return head
