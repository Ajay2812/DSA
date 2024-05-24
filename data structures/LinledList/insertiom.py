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


    def insert_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_end(data)


    def length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
        

    def remove(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
        c=0
        itr=self.head
        while itr:
            if c==index-1:
                itr.next=itr.next.next
            itr=itr.next
            c+=1


    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        if index==0:
            new_node=Node(data,self.head)
            self.head=new_node
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            count+=1


    def insert_using_recursion(self,index,data,current=None):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            new_node=Node(data,self.head)
            self.head=new_node
            return
        if current is None:
            current=self.head
        if current is None:
            print("Index out of range")
            return
        if index==1:
            new_node=Node(data,current.next)
            current.next=new_node
            return
        self.insert_using_recursion(index-1,data,current.next)

    def insert_after(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
        itr=self.head
        while itr:
            if itr.next==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next


    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next






if __name__=='__main__':
                
    ll=Linkedlist()
    ll.insert(24)
    ll.insert(32)
    ll.insert(45)
    ll.insert(4)
    #print(ll.length())
    #ll.remove(9)
    #ll.insert_at(3,"Hanu")
    #ll.insert_after(4,2)
    ll.insert_using_recursion(4,40)
    ll.print()