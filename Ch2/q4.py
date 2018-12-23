# Chapter2 - Q4
# partition linked list around a value

class Node:
 
    def __init__(self,key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # insert key at the beginning
    def push(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def print_list(self):
        curr  = self.head
        while curr:
            print(curr.key)
            curr = curr.next

    def partition(self, x):
        curr = self.tail = self.head
        while curr:
            nxt = curr.next
            curr.next = None
            if curr.key < x:
                curr.next = self.head
                self.head = curr
            else:
                self.tail.next = curr
                self.tail = curr
            curr = nxt
        return self.head

# Test
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(10)
ll.push(5)
ll.push(8)
ll.push(5)
ll.push(3)

print('Linked List before partition:')
ll.print_list()
partition_val = 5
ll.partition(partition_val)
print('Linked List after partition around x={}:'.format(partition_val))
ll.print_list()


