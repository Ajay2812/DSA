class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast!=None and fast.next !=None:
            fast=fast.next.next
            slow=slow.next
        return slow
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head==None:
                return head
            prev=None
            present=head
            next=present.next
            while present != None:
                present.next=prev
                prev=present
                present=next
                if next != None:
                    next=next.next
            #head=prev
            return prev
        
        

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid=self.middleNode(head)
        headsecond=self.reverseList(mid)
        revhead=headsecond
        while head!=None and headsecond!=None:
            if head.val != headsecond.val:
                break
            head=head.next
            headsecond=headsecond.next
        self.reverseList(revhead)
        return head==None or headsecond==None
        