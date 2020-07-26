#Implement queue using array

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear =capacity-1
        self.Q = [None]*capacity
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print('The queue is full')
            return
        self.rear = (self.rear+1)%self.capacity
        self.Q[self.rear] = item
        self.size+=1
        print('%s enqueued to the queue'%str(item))

    def dequeue(self):
        if self.is_empty():
            print('The queue is empty')
            return
        print('%s dequeued from queue'%str(self.Q[self.front]))
        self.front = (self.front+1)%self.capacity
        self.size-=1

    def que_front(self):
        if self.is_empty():
            print('The queue is empty')
            return
        print('Front item is %s'%str(self.Q[self.front]))

    def que_rear(self):
        if self.is_empty():
            print('The queue is empty')
            return
        print('Rear item is %s'%str(self.Q[self.rear]))

queue = Queue(30)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.que_front()
queue.que_rear()