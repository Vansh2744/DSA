arr = [78,90,34,62,50,40,20]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
    
print(arr)