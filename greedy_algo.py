from collections import abc
from collections import abc
def max_sum(arr):
    sorted_arr = arr.sort()
    i = 0
    j = len(arr)-1
    sum = 0

    while i < j:
        sum+=(abs(arr[i]-arr[j]))

        i+=1
        j-=1

    return sum

def min_sum(arr):
    sorted_arr = arr.sort()
    sum = 0
    i = 0

    while i < len(arr)//2:
        sum+=abs(arr[2*i]-arr[2*i+1])
        i+=1

    return sum

arr = [3,5,10,2,6,9]

# print(f"Maximum Sum : {max_sum(arr)}")
# print(f"Minimum Sum : {min_sum(arr)}")

def min_denominator(arr, amount):
    coins = arr.sort()
    balance = amount
    i = len(arr)-1
    count = 0

    while balance != 0:
        if arr[i] <= balance:
            balance -= arr[i]
            count += 1
        else:
            i-=1
    return count

arr = [2,10,20,30,40,50]

print(min_denominator(arr, 224))