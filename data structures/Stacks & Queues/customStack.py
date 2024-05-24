from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    def print(self):
        l=[]
        for items in self.container:
            l.append(items)
        return l
    
s=Stack()
s.push(20)
s.push(2)
s.push(120)
s.push(202)
print(s.pop())
print(s.print())

print(s.peek())
print(s.print())
