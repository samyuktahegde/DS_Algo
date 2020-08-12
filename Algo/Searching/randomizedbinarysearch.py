import random

#Solution1: Recursive Implementation
# def get_random(x, y):
#     tmp = (x+random.randint(0, 100000)%(y-x+1))
#     return tmp

# def randomizedBinarySearch(array, l, r, x):
#     if r>=l:
#         mid = get_random(l, r)
#         if array[mid] == x:
#             return mid
#         if array[mid]>x:
#             return randomizedBinarySearch(array, l, mid-1, x)
#         return randomizedBinarySearch(array, mid+1, r, x)
#     return -1

# array = [2, 3, 4, 10, 40]
# n = len(array)
# x = 10
# result = randomizedBinarySearch(array, 0, n-1, x)
# if result == -1:
#     print('Element is not present in the array')
# else:
#     print('Element is present at index ', result)


#Solution2: Recursive Implementation
def get_random(x, y):
    return random.randint(x, y)

def randomizedBinarySearch(array, l, r, x):
    while l<=r:
        mid = get_random(l, r)
        if array[mid] == x:
            return mid
        if array[mid]>x:
            r = mid-1
        else:
            l = mid+1
    return -1

array = [2, 3, 4, 10, 40]
n = len(array)
x = 10
result = randomizedBinarySearch(array, 0, n-1, x)
if result == -1:
    print('Element is not present in the array')
else:
    print('Element is present at index ', result)