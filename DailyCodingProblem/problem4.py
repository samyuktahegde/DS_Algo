# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def missing(array):
    array.sort()
    new_array = [x for x in array if x > 0]
    # print(new_array)
    for i in range(len(new_array)-1):
        # print(i)
        if new_array[i]+1 != new_array[i+1]:
            return new_array[i]+1
    i+=1
    return new_array[i]+1


array = [3, 4, -1, 1]
print(missing(array))

array = [1, 2, 0]
print(missing(array))
    
