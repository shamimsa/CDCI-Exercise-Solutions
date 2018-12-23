# Chapter2 - Q1

from collections import Counter

class Node:
 
    def __init__(self,key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        curr  = self.head
        while curr:
            print(curr.key)
            curr = curr.next

    # time: O(n)
    # space: O(n)
    def remove_dup(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            return self.head
        counter = Counter()
        curr = self.head
        prev = None
        while curr is not None:
            if curr.key in counter:
                prev.next = curr.next
            else:
                counter[curr.key] += 1
                prev = curr
            curr = curr.next
        print(counter)
        return self.head

    '''
    # follow-up
    # Use the "runner" technique
    # time: O(n^2)
    # space: O(1)
    def remove_dup(self):
        
    '''

# Test 1
print("Test 1")
ll = LinkedList()
n1 = Node(1)
ll.head = n1
n2 = Node(3)
n1.next = n2
n3 = Node(4)
n2.next = n3
n4 = Node(3)
n3.next = n4
n5 = Node(2)
n4.next = n5

# ll: 1 -> 3 -> 4 -> 3 -> 2
print('Linked List before duplicate removal:')
ll.print_list()
# remove duplicate(s)
ll.remove_dup()
# ll: 1 -> 3 -> 4 -> 2
print('Linked List after duplicate removal:')
ll.print_list()

# Test 2
print("Test 2")
ll = LinkedList()
n1 = Node(4)
ll.head = n1

# ll: 4 -> None
print('Linked List before duplicate removal:')
ll.print_list()
# remove duplicate(s)
ll.remove_dup()
# ll: 4 -> None
print('Linked List after duplicate removal:')
ll.print_list()

# Test 3
print("Test 3")
ll = LinkedList()
n1 = Node(4)
ll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(2)
n2.next = n3
n4 = Node(2)
n3.next = n4
n4.next = None

# ll: 4 -> 2 -> 2 -> 2
print('Linked List before duplicate removal:')
ll.print_list()
# remove duplicate(s)
ll.remove_dup()
# ll: 4 -> 2
print('Linked List after duplicate removal:')
ll.print_list()

