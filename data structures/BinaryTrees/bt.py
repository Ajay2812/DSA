
    

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def populate(self):
        value = int(input("Enter the root: "))
        self.root = Node(value)
        self._populate(self.root)

    def _populate(self, node):
        left = input(f"Do you want to insert left of {node.value}? (true/false): ").lower() == 'true'
        if left:
            value = int(input('Enter the value: '))
            node.left = Node(value)
            self._populate(node.left)

        right = input(f"Do you want to insert right of {node.value}? (true/false): ").lower() == 'true'
        if right:
            value = int(input('Enter the value: '))
            node.right = Node(value)
            self._populate(node.right)

    def display(self, node, space=""):
        if node is None:
            return
        # Display the current node
        print(space + str(node.value))
        # Display the left child
        self.display(node.left, space + "\t")
        # Display the right child
        self.display(node.right, space + "\t")


# Creating and populating the tree
tree = BinaryTree()
tree.populate()

# Display the tree structure
tree.display(tree.root)
