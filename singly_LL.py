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
            while(temp.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def print_all(self):
        t1 = self.head

        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        
        print(t1.data)

ll = SinglyLL()

ll.insert_end(10)
ll.insert_end(20)

ll.print_all()