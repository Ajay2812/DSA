class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        new_node=Node(data,self.head,None)
        if self.head !=None:
            self.head.prev=new_node
        self.head=new_node
  
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)

    def length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    def insert(self,data,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        if index==0:
           self.insert_at_front(data)
    
        c=0
        itr=self.head
        while itr:
            if c==index-1:
                itr.next=Node(data,itr.next,itr)
            itr=itr.next
            c+=1


    def insert_after(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next,self.head)
        itr=self.head
        while itr:
            if data_after==itr.next:
                itr.next=Node(data_to_insert,itr.next,itr)
                break
            itr=itr.next
  



    def print_forward(self):
        if self.head is None:
            print("LL is empty")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def get_last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr
    

    def print_backward(self):
        if self.head is None:
            print("LL is empty")
        last_node=self.get_last_node()
        itr=last_node
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.prev
        print(llstr)

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(7)
    ll.insert_at_end(9)
    ll.insert_aft(9,12)


    ll.print_forward()
    


