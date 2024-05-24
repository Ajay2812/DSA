from module import *


def remove_duplicates(ll):
        itr=ll.head
        if ll.head is not None:
            while itr.next:
                if itr.data==itr.next.data:
                        itr.next=itr.next.next
                else:
                    itr=itr.next


def merge(first,second):
        f=first.head
        s=second.head
        new=Linkedlist()
        while f != None and s != None:
            if f.data <s.data:
                new.insert_end(f.data)
                f=f.next
            else:
                new.insert_end(s.data)
                s=s.next
        while f!=None:
            new.insert_end(f.data)
            f=f.next
        while s!=None:
            new.insert_end(s.data)
            s=s.next
        return new


if __name__ == '__main__':
    first=Linkedlist()
    second=Linkedlist()
    first.insert_end(1)
    first.insert_end(2)
    first.insert_end(5)
    first.insert_end(7)
    second.insert_end(1)
    second.insert_end(3)
    second.insert_end(5)
    second.insert_end(11)
    second.insert_end(13)
    ans=merge(first,second)
    ans.print()



