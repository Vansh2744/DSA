class Dequeue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert_start(self, value):
        if self.front > 0:
            self.front -= 1
            self.queue.insert(self.front, value)

        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queue.insert(self.front, value)

        else:
            print("queue is full cannot insert in the start")

    def insert_end(self, value):
        if self.front == -1:
            self.front = 0
            self.queue.insert(self.front, value)

        else:
            self.rear += 1
            self.queue.insert(self.rear, value)

    def delete_start(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        else:
            self.front += 1

    def delete_end(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        else:
            self.rear -= 1
    
    def print_all(self):
        for i in range(self.front, self.rear+1):
            print(self.queue[i])

deq = Dequeue()

deq.insert_start(30)
    
deq.insert_end(40)
deq.insert_end(50)
deq.insert_end(60)

deq.delete_start()
deq.delete_start()

deq.delete_end()

deq.insert_start(60)
deq.insert_start(70)
deq.insert_start(80)

deq.print_all()