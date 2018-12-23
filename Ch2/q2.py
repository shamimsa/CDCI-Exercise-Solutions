# Chapter2 - Q2
# Return k-th to the last element in a linked list

class Node:
 
    def __init__(self,key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Recursive solution
    # time: O(n)
    # space: O(n)
    def kth_to_last_rec(self, head, k):
        if head is None:
            return 0
        count = self.kth_to_last_rec(head.next, k) + 1
        #print(count)
        #return count
        if count == k:
            print("{}-th element to the last is: {}".format(k, head.key))
        print(count)
        return count
   
    ''' 
    # First find the length of the linked list, then find the k-th to last
    # time: O(n)
    def k_th_to_last()
    '''

    '''
    # Use runner algorithm
    # time: 
    # space: O(1) ??
    '''

# Test
ll = LinkedList()
n1 = Node(1)
ll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(4)
n2.next = n3
n4 = Node(3)
n3.next = n4
n5 = Node(5)
n4.next = n5

# ll: 1 -> 2 -> 4 -> 3 -> 5
ll.kth_to_last_rec(ll.head,3)
