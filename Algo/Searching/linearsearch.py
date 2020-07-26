#Given an array arr[] of n elements, write a function to search a given element x in arr[].

def linear_search(array, x):
    n = len(array)
    for i in range(n):
        if x==array[i]:
            return i
    return -1

array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# x = 110
x = 175

result = linear_search(array, x)
if result==-1:
    print('It is not present')
else:
    print(str(x)+' is present at index '+str(result))
