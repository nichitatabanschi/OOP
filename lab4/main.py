from array_stack import ArrayStack
from linked_stack import LinkedStack
from dynamic_array_stack import DynamicArrayStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from circular_array_queue import CircularArrayQueue


def main():
    # Stack examples
    print("Stack Examples:")

    # ArrayStack
    array_stack = ArrayStack()
    array_stack.push(1)
    array_stack.push(2)
    array_stack.push(3)
    print("ArrayStack:")
    print("Top:", array_stack.peek())
    print("Pop:", array_stack.pop())
    print("Is Empty:", array_stack.is_empty())
    print("Size:", array_stack.size())

    # LinkedStack
    linked_stack = LinkedStack()
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(3)
    print("\nLinkedStack:")
    print("Top:", linked_stack.peek())
    print("Pop:", linked_stack.pop())
    print("Is Empty:", linked_stack.is_empty())
    print("Size:", linked_stack.size())

    # DynamicArrayStack
    dynamic_array_stack = DynamicArrayStack()
    dynamic_array_stack.push(1)
    dynamic_array_stack.push(2)
    dynamic_array_stack.push(3)
    print("\nDynamicArrayStack:")
    print("Top:", dynamic_array_stack.peek())
    print("Pop:", dynamic_array_stack.pop())
    print("Is Empty:", dynamic_array_stack.is_empty())
    print("Size:", dynamic_array_stack.size())

    # Queue examples
    print("\nQueue Examples:")

    # ArrayQueue
    array_queue = ArrayQueue()
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    print("ArrayQueue:")
    print("Front:", array_queue.peek())
    print("Dequeue:", array_queue.dequeue())
    print("Is Empty:", array_queue.is_empty())
    print("Size:", array_queue.size())

    # LinkedQueue
    linked_queue = LinkedQueue()
    linked_queue.enqueue(1)
    linked_queue.enqueue(2)
    linked_queue.enqueue(3)
    print("\nLinkedQueue:")
    print("Front:", linked_queue.peek())
    print("Dequeue:", linked_queue.dequeue())
    print("Is Empty:", linked_queue.is_empty())
    print("Size:", linked_queue.size())

    # CircularArrayQueue
    circular_array_queue = CircularArrayQueue(5)
    circular_array_queue.enqueue(1)
    circular_array_queue.enqueue(2)
    circular_array_queue.enqueue(3)
    print("\nCircularArrayQueue:")
    print("Front:", circular_array_queue.peek())
    print("Dequeue:", circular_array_queue.dequeue())
    print("Is Empty:", circular_array_queue.is_empty())
    print("Size:", circular_array_queue.size())


if __name__ == "__main__":
    main()
