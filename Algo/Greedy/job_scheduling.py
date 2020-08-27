def printJobScheduling(array, t):
    n = len(array)
    for i in range(n):
        for j in range(n-1-i):
            if array[j][2]<array[j+1][2]:
                array[j], array[j+1] = array[j+1], array[j]

    result = [False]*t
    job = [-1]*t
    
    for i in range(len(array)):
        for j in range(min(t-1, array[i][1]-1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = array[i][0]
                break
    
    print(job)

array = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
  
printJobScheduling(array, 3)