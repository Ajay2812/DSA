class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.recInsert(self.root,data)
        

    def recInsert(self,current_node,data):
        if data<current_node.data:
            if current_node.left is None:
                current_node.left=Node(data)
            else:
                self.recInsert(current_node.left,data)
        elif data>current_node.data:
            if current_node.right is None:
                current_node.right=Node(data)
            else:
                self.recInsert(current_node.right,data)

    def insertArray(self,nums):
        for i in range(len(nums)):
            self.insert(nums[i])
    def insertSorted(self,nums):
        self.sortedInsert(nums,0,len(nums))

    def sortedInsert(self,nums,start,end):
        if start>=end:
            return
        mid=(start+end)//2
        self.insert(nums[mid])
        self.sortedInsert(nums,start,mid)
        self.sortedInsert(nums,mid+1,end)

    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print("    " * level + prefix + str(node.data))
            if node.left is not None:
                self.display(node.left, level + 1, "L--- ")
            if node.right is not None:
                self.display(node.right, level + 1, "R--- ")

    def height(self,node):
        if node is None:
            return 0
        left_height=self.height(node.left) 
        right_height=self.height(node.right)

        return 1+max(left_height,right_height)
    

    
    def is_balanced(self):
        
        # Start checking from the root
        return self._check_balance(self.root)
    
    def _check_balance(self,node):
            # An empty tree is balanced
            if node is None:
                return True
            
            # Calculate height of left and right subtrees using the separate height function
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            
            # Check if the current node is balanced
            if abs(left_height - right_height) > 1:
                return False
            
            # Recursively check if the left and right subtrees are balanced
            return self._check_balance(node.left) and self._check_balance(node.right)



bst = BinarySearchTree()
nums=[1,2,3,4,5,6,7,8,9,10]
bst.insertSorted(nums)
bst.display()
print(bst.is_balanced())
            
    