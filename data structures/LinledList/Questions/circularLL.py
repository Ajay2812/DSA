
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class CLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data):
        new_node=Node(data,self.head)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        new_node.next=self.head
        self.tail=new_node
    def remove(self,index):
        if index==0:
            if self.head.next==self.head:
                self.head=None
                self.tail=None
            else:
                self.tail.next=self.head.next
                self.head=self.head.next
        else:
            c=0
            itr=self.head
            while c<index-1:
                itr=itr.next
                c+=1
                if itr.next==self.head:
                    print("Index out of range")
                    return
            itr.next=itr.next.next
            if itr.next==self.head:
                    self.tail=itr



    def print(self):
        if self.head is None:
            print("Empty LL")
        itr=self.head
        lstr=''
        while True:
            lstr+=str(itr.data)+"-->"
            itr=itr.next
            if itr==self.head:
                break
        print(lstr)
       
            





       


ll=CLL()
ll.insert(23)
ll.insert(3)
ll.insert(12)
ll.insert(31)
ll.insert(13)
ll.remove(4)
ll.print()

