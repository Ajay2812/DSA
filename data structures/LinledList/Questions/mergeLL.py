from module import *
def merge_sort(head):
    if head == None and head.next ==None:
        return head
    mid_prev=get_middle(head)
    mid=mid_prev.next
    mid_prev.next=None
    left=merge_sort(head)
    right=merge_sort(mid)
    return merge(left,right)
    

def merge(list1,list2):
    head=Node()
    itr=head
    while list1 and list2:
        if list1<list2:
            itr.next=list1
            list1=list1.next
        else:
            itr.next=list2
            list2=list2.next
        itr=itr.next
    itr.next=list1 or list2
    return head.next


def get_middle(head):
    f=head
    s=head
    if f!=None and f.next!=None:
        f=f.next.next
        s=s.next
    return s

