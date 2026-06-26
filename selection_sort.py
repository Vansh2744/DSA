arr = [78,90,34,62,50,40,20]


for i in range(len(arr)):
    m = i
    for j in range(i, len(arr)):
        if arr[m] > arr[j]:
            m = j
    arr[i], arr[m] = arr[m], arr[i]

print(arr)