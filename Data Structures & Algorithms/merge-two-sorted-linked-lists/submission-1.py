# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        head1 = list1
        while head1:
            arr.append(head1.val)
            head1 = head1.next
        
        head2 = list2
        while head2:
            arr.append(head2.val)
            head2 = head2.next 
        
        d = ListNode(0)
        curr = d

        arr.sort()
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return d.next
        
        