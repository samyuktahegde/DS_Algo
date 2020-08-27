#Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum. 
#Solution1
# from sys import maxsize
# def max_sum(array):
#     n = len(array)
#     max_so_far = -maxsize-1
#     max_ending_here = 0
#     for i in range(n):
#         max_ending_here = max_ending_here+array[i]
#         if max_so_far<max_ending_here:
#             max_so_far = max_ending_here
#         if max_ending_here<0:
#             max_ending_here=0
#     return max_so_far

# array = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
# print("Maximum contiguous sum is", max_sum(array))


#Solution2
def max_sum(array):
    n = len(array)
    max_so_far = array[0]
    curr_max = array[0]
    for i in range(1, n):
        curr_max = max(array[i], curr_max+array[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

array = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print("Maximum contiguous sum is", max_sum(array))
