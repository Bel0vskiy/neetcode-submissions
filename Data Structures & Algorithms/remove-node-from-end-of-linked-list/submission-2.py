# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        i = l - n
        curr = head
        if i == 0:
            return head.next
        for j in range(l):
            if j+1 == i:
                if curr.next.next:
                    tail = curr.next.next
                    curr.next = tail
                else:
                    curr.next = None
            else:
                curr = curr.next
        return head