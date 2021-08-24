def calculate(r, unit, arr, n):
    if n == 0:
        return -1

    totalFoodRequired = r*unit
    foodTillNow = 0

    for i in range(n):
        foodTillNow += arr[i]

        #Will break when sum reaches required sum of food
        if foodTillNow >= totalFoodRequired: 
            break
    
    #it means the food insufficient #it will return zero if food is 
    # insufficient as required
    if totalFoodRequired > foodTillNow:  
        return 0            

    #it will return numbers that in how much houses rat got the required 
    # food example 3 i.e. n = 2 (2 + 1) = 3
    return i + 1  




r = int(input())
unit = int(input())
n = int(input())
'''
arr = []
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele)
'''


arr = list(map(int, input().split()[:n]))
print(calculate(r, unit, arr, n)) 
#call calculate function and will return output as per inputs