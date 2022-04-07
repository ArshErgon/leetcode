class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        return dummy.next   
    
    def removeNthFormEndWithOutDummy(self, n):
        fast, slow = head, head
        
        for _ in range(n):
            fast = fast.next
            
        if not fast:
            return head
        
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head
