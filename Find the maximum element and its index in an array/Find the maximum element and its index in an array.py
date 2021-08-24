def FindMax(arr):
    #initialze first value as largest
    max = arr[0]
    for i in range(1, len(arr)):

        #if there is any other value greater than max, max is updated to that element
        if arr[i] > max:
            max = arr[i]
        ind = arr.index(max)
    #Print the maximum value
    print(max)
    #return index of the maximum value
    return ind

arr = list(map(int, input().split()))
print(FindMax(arr))