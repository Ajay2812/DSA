class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.val)
    
A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
#print(A)

#DEPTH FIRST SEARCH
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
#print(pre_order(A))

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
#print(in_order(A))

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

print(post_order(A))


def pre_order_iterative(node):
    stk=[node]
    while stk:
        node=stk.pop()
        print(node)
        if node.right:stk.append(node.right)
        if node.left:stk.append(node.left)
#print(pre_order_iterative(A))


def search(node,target):
    if not node:
        return False
    if node.val==target:
        return True
    return search(node.left,target) or search(node.right,target)
#print(search(A,10))


#BREADTH FIRST SEARCH IMPLEMENTED USING QUEUE [level order]
from collections import deque
def level_order(node):
    q=deque()
    q.append(node)
    while q:
        node=q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
#print(level_order(A))


A1=TreeNode(5)
B1=TreeNode(1)
C1=TreeNode(8)
D1=TreeNode(-1)
E1=TreeNode(3)
F1=TreeNode(7)
G1=TreeNode(9)

A1.left,A1.right=B1,C1
B1.left,B1.right=D1,E1
C1.left,C1.right=F1,G1

#print(in_order(A1))



#Searching in Binary Search Tree

def search_bst(node,target):
    if not node:
        return False
    if node.value==target:
        return True
    if target>node.value:
        return search(node.right,target)
    else:
        return search(node.left,target)





