from stack import Stack

class ArrayStack(Stack):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)
