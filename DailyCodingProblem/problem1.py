# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


# Solution1: Using two loops
# def summation(array, k):
#     for i in range(len(array)-1):
#         for j in range(i+1, len(array)):
#             if array[i]+array[j] == k:
#                 return True
#     return False


# array = [10, 15, 3, 7]
# k = 17
# print(summation(array, k))

# Solution2: Sorting and two pointer technique
# def summation(array, k):
#     array.sort()
#     l = 0
#     r = len(array)-1
#     while l<r:
#         if array[l]+array[r]==k:
#             return True
#         elif array[l]+array[r]<k:
#             l=l+1
#         else:
#             r=r-1
#     return False

# array = [10, 15, 3, 7]
# k = 19
# print(summation(array, k))

# Solution3: Using Hashing technique
def summation(array, k):
    n = len(array)
    s = set()
    flag = 0
    for i in range(n):
        if k-array[i] not in s:
            s.add(array[i])
            print(array[i], k-array[i])
            flag = 1
    if flag == 1:
        return True
    else:
        return False

array = [10, 15, 3, 7, 12, 6]
k = 18
print(summation(array, k))  

    



    