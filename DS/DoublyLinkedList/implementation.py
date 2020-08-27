class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('This node does not exist in DLL')
            return
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next is not None:
            prev_node.next.prev = new_node
            prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insertBefore(self, next_node, new_data):
        if next_node is None:
            print('This node does not exist in DLL')
            return
        new_node = Node(data=new_data)
        if self.head is next_node:
            next_node.prev = new_node
            new_node.next = next_node
            self.head = new_node
            return
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        next_node.prev = new_node


