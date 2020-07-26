class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    #Add node in the front
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    #Add a node after a given node
    def insert_after(self, prev_node, data):
        node = Node(data)
        if prev_node is None:
            print('The given previous node must be in the linked list')

        node.next = prev_node.next
        prev_node.next = node

    #Add a node at the end
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node


# Start with the empty list 
llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
llist.push(7)
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
llist.push(1)
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
llist.insert_after(llist.head.next, 8) 
  
print('Created linked list is:',)
llist.print_list() 

