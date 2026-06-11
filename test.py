class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, url):
        self.current = Node(url)

    def visit(self, url):
        node = Node(url)
        self.current.next = None
        node.prev = self.current
        self.current.next = node
        self.current = node

    def back(self):
        if self.current.prev:
            self.current = self.current.prev

        return self.current.url
    
    def forward(self):
        if self.current.next:
            self.current = self.current.next

        return self.current.url
    
    def current_page(self):
        return self.current.url


hist = BrowserHistory("google.com")

print(hist.current_page())

hist.visit("chatgpt.com")

print(hist.current_page())

hist.visit("youtube.com")

print(hist.current_page())

print(hist.back())
print(hist.forward())

print(hist.current_page())