class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root != None:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root != None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root != None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)

preorder_traversal(node)
print()
inorder_traversal(node)
print()
postorder_traversal(node)