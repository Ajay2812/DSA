class MyQueue:

    def __init__(self):
        self.first=[]
        self.second=[]

    def push(self, x: int) -> None:
        self.first.append(x)

        

    def pop(self) -> int:
        if not self.second:
            while len(self.first) !=0:
                self.second.append(self.first.pop())
        removed=self.second.pop()
        
        return removed
        

    def peek(self) -> int:
        if not self.second:

            while len(self.first) !=0:
                self.second.append(self.first.pop())
        peeked=self.second[-1]        
        return peeked
        
        

    def empty(self) -> bool:
        is_empty=not self.first and not self.second
        return is_empty

        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.peek()
obj.pop()
obj.empty()