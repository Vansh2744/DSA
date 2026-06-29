def perform_sort(arr, l, r):
    if l < r:
        idx = partition(arr, l, r)
        perform_sort(arr, l, idx-1)
        perform_sort(arr, idx+1, r)

def partition(arr, l, r):
    pivot = arr[l]

    i = l+1
    j = r

    while True:
        while arr[i] < pivot and i <= j:
            i += 1

        while arr[j] > pivot and i <= j:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

        else:
            break

    arr[l], arr[j] = arr[j], arr[l]

    return j


arr = [78, 90, 45, 10, 20, 35]

perform_sort(arr, 0, len(arr)-1)

print(arr)