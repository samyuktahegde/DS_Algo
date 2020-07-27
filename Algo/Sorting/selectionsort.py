def selectionsort(array):
    n = len(array)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if array[j]<array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

array = [64, 25, 12, 22, 11] 
selectionsort(array)
print(array)