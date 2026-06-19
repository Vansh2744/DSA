class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, data):
    current = root
    if current == None:
        current = Node(data)
        return
    if data < current.data:
        current = current.left
    else:
        current = current.right

node = Node(20)
