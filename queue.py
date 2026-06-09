class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, value):
        self.queue.append(value)

    def delete(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)
    
q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())