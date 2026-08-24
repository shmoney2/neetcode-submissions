# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr_2 = list2
        dummy = ListNode()
        curr_3 = dummy
        while curr and curr_2:
            if curr.val >= curr_2.val:
                curr_3.next = curr_2
                curr_2 = curr_2.next
            elif curr_2.val > curr.val:
                curr_3.next = curr
                curr = curr.next
            curr_3 = curr_3.next
        
        curr_3.next = curr if curr else curr_2
        return dummy.next