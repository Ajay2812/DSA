from module import *

def finding_cycle(head):
    fast=head
    slow=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

def lengthCycle(head):
    fast=head
    slow=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            temp=slow
            length=1
            while temp!=slow:
                temp=temp.next
                length+=1
            return length
    return 0

def detectCycle(head):
    length=0
    fast=head
    slow=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            length=lengthCycle(slow)
            break
    if length==0:
        return None
    f=head
    s=head
    while length>0:
        s=s.next
        length-=1
    while f!=s:
        s=s.next
        f=f.next
    return s
def get_square(number):
    ans=0
    while number>0:
        rem=number%10
        ans+=rem**2
        number/=10
    return ans
def happynumber(n):
    fast=n
    slow=n
    slow=get_square(slow)
    fast=get_square(get_square(fast))
    while slow!=fast:
        slow=get_square(slow)
        fast=get_square(get_square(fast))
    if slow==1:
        return True
    return False







