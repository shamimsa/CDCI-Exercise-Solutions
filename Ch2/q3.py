# Chapter2 - Q3
# Delete a node from the middle of a linked list having access only to that node

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

    def del_middle(self, del_node):
        if self.head is None or del_node.next is None:
            return False
        del_node.key = del_node.next.key
        del_node.next = del_node.next.next
        return 

# Test
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
print('Linked List before removal of the middle node:')
ll.print_list()
ll.del_middle(n4)
# ll: 1 -> 3 -> 4 -> 2
print('Linked List after node removal:')
ll.print_list()


