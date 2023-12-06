def max_heapify(arr, i):
    l_pos = 2*i+1
    r_pos = 2*i+2

    if l_pos<len(arr) and arr[l_pos]>arr[i]:
        largest = l_pos
    else:
        largest = i
    if r_pos<len(arr) and arr[r_pos]>arr[largest]:
        largest = r_pos

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest)

data = [19,12,16,1,4,7,17,23,27]
n = len(data)
for i in range(n // 2 - 1, -1, -1):
    max_heapify(data, i)
    
print("Max Heap:", data)
