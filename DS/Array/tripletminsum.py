#Given an array of distinct integers arr[]. The task is to find a triplet(a group of 3 elements) that has the minimum sum.

# Solution1: Generate all possible sums and compare

from sys import maxsize
# def min_sum_triplet(array):
#     n = len(array)
#     ans = maxsize
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 ans = min(ans, array[i]+array[j]+array[k])
#     return ans

# array = [ 1, 2, 3, 4, 5, -1, 5, -2 ]
# print(min_sum_triplet(array))

# Solution2: Find first, second and third minimum and then calculate the sum
def min_sum_triplet(array):
    n = len(array)
    fmin = maxsize
    smin = maxsize
    tmin = maxsize
    for i in range(n):
        if array[i]<fmin:
            tmin = smin
            smin = fmin
            fmin = array[i]    
        elif array[i]<smin:
            tmin = smin
            smin = array[i]
        elif array[i]<tmin:
            tmin = array[i]
    return (fmin+smin+tmin)

array = [ 1, 2, 3, 4, 5, -1, 5, -2 ]
print(min_sum_triplet(array))
        