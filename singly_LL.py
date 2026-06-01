class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, data):
        temp = Node(data)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insert_start(self, data):
        temp = Node(data)
        if(self.head == None):
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insert_between(self, data, after):
        temp = Node(data)
        t1 = self.head

        if(self.head == after):
            self.head.next = temp

        while(t1.data != after):
            t1 = t1.next
        temp.next = t1.next
        t1.next = temp

    def delete_node(self, value):
        t1 = self.head
        prev = t1
        if(self.head.data == value):
            self.head = prev.next

        while(t1.data != value):
            prev = t1
            t1 = t1.next

        prev.next = t1.next

    def print_all(self):
        t1 = self.head

        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        
        print(t1.data)

ll = SinglyLL()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_start(5)
ll.insert_between(30, 5)
ll.delete_node(20)

ll.print_all()