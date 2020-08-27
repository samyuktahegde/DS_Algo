class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def orientation(p1, p2, p3):
    val = (float(p2.y-p1.y)*(p3.x-p2.x)) - (float(p3.y-p2.y)*(p2.x-p1.x))
    if val>0:
        return 1
    elif val<0:
        return 2
    else:
        return 0

p1 = Point(0, 0) 
p2 = Point(4, 4) 
p3 = Point(1, 2) 
  
o = orientation(p1, p2, p3) 
  
if (o == 0): 
    print("Linear") 
elif (o == 1): 
    print("Clockwise") 
else: 
    print("CounterClockwise") 