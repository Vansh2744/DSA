class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularSinglyLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            node.next = self.head

        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next

            temp.next = node
            node.next = self.head

    def insert_start(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next

            temp.next = node
            node.next = self.head
            self.head = node

    def insert_between(self, data, after):
        node = Node(data)
        temp = self.head
        while(temp.data != after):
            temp = temp.next
        if(temp.next == self.head):
            node.next = self.head
            temp.next = node
        else:
            node.next = temp.next
            temp.next = node

    def delete_node(self, data):
        if(self.head.data == data):
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            temp = self.head
            prev = temp
            while(temp.data != data):
                prev = temp
                temp = temp.next
            if(temp.next == self.head):
                prev.next = self.head
            else:
                prev.next = temp.next


    def check_connect(self, value):
        temp = self.head

        while(temp.data != value):
            temp = temp.next

        print(temp.next.data)
    
    def print_all(self):
        temp = self.head
        while(temp.next != self.head):
            print(temp.data)
            temp = temp.next
        print(temp.data)

ll = CircularSinglyLL()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

ll.insert_start(5)
ll.insert_start(4)
ll.insert_start(3)

ll.insert_between(50, 40)

ll.delete_node(30)

ll.print_all()
# ll.check_connect(50)