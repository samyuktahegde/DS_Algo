# Solution1:Using recursion
# def fibonacci(n):
#     if n<0:
#         print('Invalid input')
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(9))

# Solution2: Using Dynamic Programming
# def fibonacci(n):
#     FibArray = [0, 1]
#     while len(FibArray)<n+1:
#         FibArray.append(0)
#     if n<=1:
#         return n
#     else:
#         if FibArray[n-1]==0:
#             FibArray[n-1] = fibonacci(n-1)
#         if FibArray[n-2]==0:
#             FibArray[n-2] = fibonacci(n-2)
#     FibArray[n] = FibArray[n-1]+FibArray[n-2]
#     return FibArray[n]

# print(fibonacci(9))

# Solution2: Using space optimisation
def fibonacci(n):
    a = 0
    b = 1
    if n<0:
        print('Invalid input')
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
    return c

print(fibonacci(9))



