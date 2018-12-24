# Chapter3 - Q4
# Queue via Stacks

# O(n) space complexity where n is the number of items in the queue.
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # O(1) time
    def enqueue(self, item):
        self.stack1.append(item)

    # O(n) time
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is Empty!')
        if self.get_size(self.stack2) == 0:
            while self.get_size(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        value = self.stack2.pop()
        return value

    # O(1) time
    def is_empty(self):
        return (len(self.stack1) + len(self.stack2)) == 0

    # Method to get the queue size
    def get_size(self,stack):
        return len(stack)

# Test 1
queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

