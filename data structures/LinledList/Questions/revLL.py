from module import *
class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

def reverse_linked_list(head, tail):
    if head is None:
        return tail

    next_node = head.next
    head.next = tail
    return reverse_linked_list(next_node, head)
def print_linked_list(head):
    current = head
    while current is not None:
        print(str(current.data) + "-->",end="")
        current = current.next
def Inplace_rev():
    if LL.length()<2:
        return
    prev=None
    pres=LL.head 
    next=pres.next
    while pres !=None:
        pres.next=prev
        prev=pres
        pres=next
        if next!=None:
            next=next.next
    LL.head=prev


LL=Linkedlist()
LL.insert_end(1)
LL.insert_end(2)
LL.insert_end(3)
LL.insert_end(4)
LL.insert_end(5)
#new_head=reverse_linked_list(LL.head,None)
#print_linked_list(new_head)
Inplace_rev()
LL.print()
