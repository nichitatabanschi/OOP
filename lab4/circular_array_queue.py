from queue import Queue

class CircularArrayQueue(Queue):
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size < self.capacity:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            data = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return data

    def peek(self):
        return self.items[self.front] if self.size > 0 else None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size
