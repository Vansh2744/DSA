class Stack:
    def __init__(self):
        self.stack = []

    def find_len(self):
        return len(self.stack)
    
    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack.pop(0)
        
    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack[0]
        
stk = Stack()

stk.push(10)
stk.push(20)
stk.push(30)

stk.pop()

print(stk.stack)