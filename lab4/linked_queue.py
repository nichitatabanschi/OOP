from queue import Queue

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedQueue(Queue):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front:
            data = self.front.data
            self.front = self.front.next_node
            return data

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return not bool(self.front)

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next_node
        return count
