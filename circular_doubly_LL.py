class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CicularDoublyLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        node = Node(data)
        
        if(self.head != None):
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next

            node.prev = temp
            node.next = self.head
            temp.next = node
        else:
            self.head = node
            node.prev = self.head
            node.next = self.head

    def insert_start(self, data):
        node = Node(data)

        if(self.head != None):
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            node.next = self.head
            node.prev = temp
            temp.next = node
            self.head.prev = temp
            self.head = node
        else:
            self.head = node
            node.prev = self.head
            node.next = self.head

    def insert_between(self, data, after):
        node = Node(data)
        temp = self.head

        while(temp.data != after):
            temp = temp.next
        if(temp.next != self.head):
            node.next = temp.next
            node.prev = temp
            temp.next = node
        else:
            node.next = self.head
            node.prev = temp
            self.head.prev = node
            temp.next = node

    def delete_node(self, data):
        if(self.head.data == data):
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            self.head.prev = temp
        else:
            temp = self.head
            prev = temp
            while(temp.data != data):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp.next.prev = prev

    def check_connect(self, value):
        temp = self.head

        while(temp.data != value):
            temp = temp.next

        print(f"Next : {temp.next.data}")
        print(f"Prev : {temp.prev.data}")

    def print_all(self):
        temp = self.head
        while(temp.next != self.head):
            print(temp.data)
            temp = temp.next
        print(temp.data)

ll = CicularDoublyLL()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_start(5)
ll.insert_start(4)
ll.insert_start(3)

ll.insert_between(40, 5)
ll.insert_between(50, 30)

ll.delete_node(3)

ll.print_all()
ll.check_connect(50)