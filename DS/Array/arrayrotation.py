#Solution1: Using temp array

# def arrayRotate(array, d):
#     n = len(array)
#     temp = []
#     k = 0
#     for i in range(d):
#         temp.append(array[i])
#     for j in range(d, n):
#         array[k] = array[j]
#         k = k+1
#     p = 0
#     for l in range(n-d, n):
#         array[l] = temp[p]
#         p=p+1
#     return array

# array = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# print(arrayRotate(array, d))

#Solution2: Rotate one by one
# def arrayRotate(array, d):
#     for i in range(d):
#         rotateOne(array)
#     return array

# def rotateOne(array):
#     n = len(array)
#     temp = array[0]
#     for i in range(n-1):
#         array[i] = array[i+1]
#     array[n-1] = temp

# array = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# print(arrayRotate(array, d))



#Solution3: Using GCD Method. Juggling algorithm
# def arrayRotate(array, d):
#     n = len(array)
#     d = d%n
#     g_c_d = gcd(d, n)
#     for i in range(g_c_d):
#         temp = array[i]
#         j = i
#         while 1:
#             k = j+d
#             if k>=n:
#                 k = k-n
#             if k==i:
#                 break
#             array[j] = array[k]
#             j = k
#         array[j] = temp
#     return array

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b, a%b)

# array = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# print(arrayRotate(array, d))

# Solution4: Reversal algorithm for array rotation
# def reverseArray(array, start, end):
#     while start<end:
#         array[start], array[end] = array[end], array[start]
#         start+=1
#         end-=1

# def arrayRotate(array, d):
#     if d==0:
#         return
#     n = len(array)
#     reverseArray(array, 0, d-1)
#     reverseArray(array, d, n-1)
#     reverseArray(array, 0, n-1)

# array = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# arrayRotate(array, d)
# print(array)


#Solution4a: Block swap algorithm - Iterative implementation

def blockswap(array, d):
    n = len(array)
    i = d
    j = n-d
    while i!=j:
        if i<j:
            swap(array, d-i, d+j-i, i)
            j-=i
        else:
            swap(array, d-i, d, j)
            i-=j
    swap(array, d-i, d, i)

def swap(array, a, b, d):
    for i in range(d):
        array[a+i], array[b+i] = array[b+i], array[a+i]

array = [1, 2, 3, 4, 5, 6, 7]
d = 2
blockswap(array, d)
print(array)

