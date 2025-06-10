class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(10)
s.push(20)
print("Top element:", s.peek())
print("Pop element:", s.pop())
print("Is stack empty?", s.is_empty())
