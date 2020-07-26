import math

def jump_search(array, x):
    n = len(array)
    step = math.sqrt(n)
    prev = 0
    while array[int(min(step, n)-1)]<x:
        prev = step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    while array[int(prev)]<x:
        prev+=1
        if prev==min(step, n):
            return -1
    if array[int(prev)]==x:
        return prev
    return -1

array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 55

index = int(jump_search(array, x))
print(index)