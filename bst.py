class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root == None:
        return Node(data)

    if root.data < data:
        root.right = insert(root.right, data)

    else:
        root.left = insert(root.left, data)

    return root

def inorder_traversal(root):
    if root != None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

root = insert(None, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 60)
root = insert(root, 70)
root = insert(root, 80)

inorder_traversal(root)