#Solution1:Iterative Implementation

# def binary_search(array, l, r, x):
#     while l<=r:
#         mid = l+(r-l)//2
#         if array[mid] == x:
#             return mid
#         elif array[mid]>x:
#             r = mid-1
#         else:
#             l = mid+1
#     return -1

# array = [ 2, 3, 4, 10, 40 ] 
# x = 11
# result = binary_search(array, 0, len(array)-1, x)
# if result != -1:
#     print('Element found at %s' %str(result))
# else:
#     print('Element not found')


#Solution2:Recursive Implementation

def binary_search(array, l, r, x):
    mid = l+(r-l)//2
    if l<=r:
        if array[mid] == x:
            return mid
        elif array[mid]>x:
            return binary_search(array, l, mid-1, x)
        else:
            return binary_search(array, l+1, r, x)
    else:
        return -1

array = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binary_search(array, 0, len(array)-1, x)
if result != -1:
    print('Element found at %s' %str(result))
else:
    print('Element not found')
    
