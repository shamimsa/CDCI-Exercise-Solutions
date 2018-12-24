# Chapter3 - Q1
# Implement three stacks using a single array

class ThreeInOne:

    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.array = [0] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            raise Exception('Stack is Full!')
        self.sizes[stack_num] += 1
        self.array[self.get_top_idx(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is Empty!')
        idx = self.get_top_idx(stack_num)
        pop_item = self.array[idx]
        self.array[idx] = 0
        self.sizes[stack_num] -= 1
        return pop_item

    def peek(self, stack_num):
        return self.array[self.get_top_idx(stack_num)]

    def get_top_idx(self, stack_num):
        return stack_num * self.stack_size + self.sizes[stack_num] - 1 

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size


# Test
stack = ThreeInOne(2)
#stack.pop(1)
stack.push(5,1)
print(stack.pop(1))
stack.push(1,2)
stack.push(10,1)
stack.push(2,1)
#stack.push(1,1)
print(stack.pop(1))
stack.push(1,1)

