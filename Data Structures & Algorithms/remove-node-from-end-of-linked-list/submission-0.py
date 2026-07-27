# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i = len(arr) - n
        arr.pop(i)
        newHead = ListNode()
        p = newHead
        for n in arr:
            newHead.next = ListNode(n)
            newHead = newHead.next
        return p.next