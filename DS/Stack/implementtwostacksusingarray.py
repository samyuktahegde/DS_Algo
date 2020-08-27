class two_stacks:
    def __init__(self, n):
        self.size = n
        self.array = [None]*n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1<self.top2-1:
            self.top1 = self.top1+1
            self.array[self.top1] = x
        else:
            print('Stack1 overflow')

    def push2(self, x):
        if self.top2>self.top1+1:
            self.top2 = self.top2-1
            self.array[self.top2] = x
        else:
            print('Stack2 overflow')

    def pop1(self):
        if self.top1>-1:
            x = self.array[self.top1]
            self.top1 = self.top1-1
            return x
        else:
            print('Stack1 underflow')

    def pop2(self):
        if self.top2<self.size:
            x = self.array[self.top2]
            self.top2 = self.top2+1
            return x
        else:
            print('Stack2 underflow')

ts = two_stacks(5) 
ts.push1(5) 
ts.push2(10) 
ts.push2(15) 
ts.push1(11) 
ts.push2(7) 
  
print("Popped element from stack1 is " + str(ts.pop1())) 
ts.push2(40) 
print("Popped element from stack2 is " + str(ts.pop2())) 
  