#Solution1: Using two stacks. Make enqueue operation costly
# class Queue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def enqueue(self, x):
#         while len(self.stack1)!= 0:
#             self.stack2.append(self.stack1.pop())

#         self.stack1.append(x)

#         while len(self.stack2)!=0:
#             self.stack1.append(self.stack2.pop())

#     def dequeue(self):
#         if len(self.stack1) == 0:
#             print('Queue is empty')
#             return
#         return self.stack1.pop()

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())

#Solution2: Using two stacks. Make dequeue operation costly
# class Queue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def enqueue(self, x):
#         self.stack1.append(x)

#     def dequeue(self):
#         if len(self.stack1)==0 and len(self.stack2)==0:
#             print('Queue is empty')
#             return
#         if len(self.stack2)==0:
#             while len(self.stack1)!=0:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2.pop()

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print(q.dequeue())
# q.enqueue(4)
# print(q.dequeue())


#Solution3: Using a stack and function call stack.
class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, x):
        self.stack.append(x)

    def dequeue(self):
        if len(self.stack)<=0:
            print('Queue is empty')
            return
        x = self.stack.pop()
        if len(self.stack)<=0:
            return x
        item = self.dequeue()
        self.stack.append(x)
        return item
            

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
        