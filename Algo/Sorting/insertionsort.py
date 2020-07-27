def insertionsort(array):
    n = len(array)
    for i in range(n):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key

array = [12, 11, 13, 5, 6] 
insertionsort(array)
print(array)