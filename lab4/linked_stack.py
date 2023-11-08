from stack import Stack

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedStack(Stack):
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next_node
            return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return not bool(self.top)

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next_node
        return count
