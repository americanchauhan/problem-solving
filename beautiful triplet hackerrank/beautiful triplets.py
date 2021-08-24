from collections import Counter

def beautifulTriplets(d, arr):
    m = Counter(arr)
    count = 0
    
    for num in arr:
        if m[num + d] and m[num + d + d]:
            count += 1
            
    return count

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))
print(beautifulTriplets(d, arr))