def min_and_max(arr, l, r):
    if l == r:
        return arr[l], arr[r]
    elif l+1 == r:
        if arr[l] < arr[r]:
            return arr[l], arr[r]
        else:
            return arr[r], arr[l]
        
    m = (l+r)//2

    min1, max1 = min_and_max(arr, l, m)
    min2, max2 = min_and_max(arr, m+1, r)

    max = 0
    min = 0

    if min1 < min2:
        min = min1
    else:
        min = min2

    if max1 > max2:
        max = max1
    else:
        max = max2

    return min,max

arr = [3,45,6,34,12,67,90,45,60]

print(min_and_max(arr, 0, len(arr)-1))