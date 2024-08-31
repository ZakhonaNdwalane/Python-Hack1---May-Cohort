class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []  # Stack for enqueue operation
        self.stack2 = []  # Stack for dequeue operation

    def enqueue(self, x: int):
        # Push element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop and return the top element from stack2
        if self.stack2:
            return self.stack2.pop()
        else:
            # If both stacks are empty, raise an exception or return None
            raise IndexError("dequeue from an empty queue")

# Test the QueueWithStacks class
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4
