class Node:
    def __init__(self, data,prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, data):
        node = Node(data)

        if(self.head != None):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            node.prev = temp
            temp.next = node

        else:
            self.head = node

    def insert_start(self, data):
        node = Node(data)

        if(self.head != None):
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def insert_between(self, data, after):
        node = Node(data)
        temp = self.head
      
        while(temp.data != after):
            temp = temp.next
        node.prev = temp
        node.next = temp.next
        temp.next = node

    def delete_node(self, data):
        temp = self.head

        if(self.head.data == data):
            self.head = temp.next
            self.head.prev = None
            return
        while(temp.data != data):
            temp = temp.next 
        if(temp.next == None):
            temp.prev.next = None 
            return      
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def print_all(self):
        if(self.head == None):
            print("No data available")
        else:
            temp = self.head
            while(temp.next != None):
                print(temp.data)
                temp = temp.next
            print(temp.data)

    def print_prev(self, value):
        temp = self.head
        while(temp.data != value):
            temp = temp.next
        print(temp.prev.data)

ll = DoublyLL()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_end(50)

ll.insert_start(5)
ll.insert_start(4)
ll.insert_start(3)
ll.insert_start(2)

ll.insert_between(100, 50)

# ll.delete_node(100)
ll.delete_node(2)

ll.print_all()