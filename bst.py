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

def search(root, data):
    if root == None:
        print("Not Found")
        return

    if root.data == data:
        print("Data Found")
        return

    if root.data > data:
        search(root.left, data)

    else:
        search(root.right, data)

def get_successor(root):
    root = root.right
    while root.left != None:
        root = root.left
    return root

def delete(root, data):
    if root == None:
        print("Not Found")
        return
    elif root.data > data:
        root.left = delete(root.left, data)
    elif root.data < data:
        root.right = delete(root.right, data)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
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

print("\n")
# search(root, 70)
# search(root, 90)

root = delete(root, 30)
inorder_traversal(root)