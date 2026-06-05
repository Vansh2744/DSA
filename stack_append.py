class Stack:
    def __init__(self):
        self.stack = []

    def find_len(self):
        return len(self.stack)
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack[len(self.stack) - 1]
        
stk = Stack()

stk.push(30)
stk.push(20)
stk.push(10)

stk.pop()

print(stk.peek())