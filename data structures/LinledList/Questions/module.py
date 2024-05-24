class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class Linkedlist:
    def __init__(self):
        self.head=None


    def insert(self,data):
        new_node=Node(data,self.head)
        self.head=new_node


    def print(self):
        if self.head is None:
            print("Empty LL")
        lstr=''
        itr=self.head
        while itr:
            lstr+=str(itr.data)+'-->'
            itr=itr.next
        print(lstr)

    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c