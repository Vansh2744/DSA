class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.front = self.rear = -1
        self.size = size

    def insert(self, val):
        if (self.rear+1) % self.size == self.front:
            print("Queue is Full")

        elif self.front == -1:
            self.rear = self.front = 0
            self.queue[self.rear] = val
        
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = val

    def delete(self):
        if self.front == -1:
            print("Queue is Empty")

        elif self.front == self.rear:
            print(self.queue[self.front])
            self.front = self.rear = -1
        
        else:
            print(self.queue[self.front])
            self.front = (self.front+1)%self.size

queue = CircularQueue(5)

queue.insert(10)
queue.insert(20)
queue.insert(30)
queue.insert(40)
queue.insert(50)

queue.delete()
queue.delete()
queue.delete()
queue.delete()
queue.delete()
queue.delete()