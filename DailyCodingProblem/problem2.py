# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# Solution1: Using division
# def multiplication(array):
#     product_array = []
#     for i in range(len(array)):
#         prod = 1
#         for num in array[:i]+array[i+1:]:
#             prod*=num
#         product_array.append(prod)
#     return product_array


# array = [1, 2, 3, 4, 5]
# print(multiplication(array))

# array = [3, 2, 1]
# print(multiplication(array))

# Solution2: Using prefix and suffix arrays
def multiplication(array):
    n = len(array)
    if n==1:
        print(0)
        return 
    left = [0]*n
    right = [0]*n
    prod = [0]*n
    left[0]=1
    right[n-1] = 1
    for i in range(1, n):
        left[i] = left[i-1]*array[i-1]
    for j in range(n-2, -1, -1):
        right[j] = right[j+1]*array[j+1]
    for k in range(n):
        prod[k] = left[k]*right[k]
    return prod

array = [1, 2, 3, 4, 5]
print(multiplication(array))

array = [3, 2, 1]
print(multiplication(array))