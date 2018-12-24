# Chapter3 - Q2
# Stack Min
# time: O(1)
# space: O(n)

class StackMin:
 
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # O(1) time
    def push(self,item):
        if self.is_empty():
            self.min_stack.append(item)
        else:
            if item < self.peek(self.min_stack):
                self.min_stack.append(item)
        self.stack.append(item)

    # O(1) time
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is Empty!')
        val = self.stack.pop()
        if val == self.peek(self.min_stack):
            self.min_stack.pop()
        return val
   
    # O(1) time
    def min(self):
        return self.peek(self.min_stack)
  
    def is_empty(self):
        return not len(self.stack)

    def peek(self,s):
        return s[-1]


# Test
stack = StackMin()
stack.push(5)
print(stack.min())
stack.push(6)
print(stack.min())
stack.push(3)
print(stack.min())
stack.push(7)
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
