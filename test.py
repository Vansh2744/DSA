arr = [16,17,4,3,5,2]

greater_right = arr[-1]
res = [arr[-1]]
max_so_far = float('-inf')

for i in range(len(arr)-2, -1, -1):
    if arr[i] >= greater_right:
        greater_right = arr[i]
        res.append(arr[i])

print(max_so_far)