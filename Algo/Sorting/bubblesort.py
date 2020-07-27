def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                s = array[j]
                array[j] = array[j+1]
                array[j+1] = s
                swapped = True
        if swapped == False:
            break

array = [64, 34, 25, 12, 22, 11, 90]
bubblesort(array)
print(array)