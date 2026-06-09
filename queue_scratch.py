class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, value):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue.insert(self.rear, value)

        else:
            self.rear += 1
            self.queue.insert(self.rear, value)

    def delete(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.front += 1

    def print_all(self):
        for i in range(self.front, self.rear+1):
            print(self.queue[i])

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(50)
q.insert(60)
q.insert(70)

q.delete()
q.delete()
q.delete()

q.print_all()