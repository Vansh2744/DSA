class Dequeue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert_start(self, value):
        self.queue.insert(0, value)

    def insert_end(self, value):
        self.queue.append(value)

    def delete_start(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)
    
    def delete_end(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop()
    
deq = Dequeue()

deq.insert_start(10)
deq.insert_start(20)
deq.insert_start(30)

deq.insert_end(50)
deq.insert_end(60)
deq.insert_end(70)

print(deq.delete_start())
print(deq.delete_start())
print(deq.delete_start())

print(deq.delete_end())
print(deq.delete_end())
print(deq.delete_end())
print(deq.delete_end())