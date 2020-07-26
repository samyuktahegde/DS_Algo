#Iterative Implementation

# def interpolationsearch(array, x):
#     n = len(array)
#     lo = 0
#     hi = n-1
#     while lo<=hi and x>=array[lo] and x<=array[hi]:
#         if lo==hi:
#             if array[lo] == x:
#                 return lo
#             return -1
#         pos = lo+int(((float(hi-lo)/(array[hi]-array[lo]))*(x-array[lo])))
#         if array[pos] == x:
#             return pos
#         if array[pos]<x:
#             lo = pos+1
#         else:
#             hi = pos-1
#     return -1

# array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
# x = 18
# print(interpolationsearch(array, x))



#Recursive Implementation

def interpolationsearch(array, lo, hi, x):
    n = len(array)
    if lo<=hi and array[lo]<=x and array[hi]>=x:
        pos = lo+int(((float(hi-lo)/(array[hi]-array[lo]))*(x-array[lo])))
        if array[pos] == x:
            return pos
        if array[pos]<x:
            return interpolationsearch(array, pos+1, hi, x)
        if array[pos]>x:
            return interpolationsearch(array, lo, pos-1, x)
    return -1

array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
x = 18
n = len(array)
print(interpolationsearch(array, 0, n-1, x))
