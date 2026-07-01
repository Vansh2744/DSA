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

print(f"Maximum Sum : {max_sum(arr)}")
print(f"Minimum Sum : {min_sum(arr)}")