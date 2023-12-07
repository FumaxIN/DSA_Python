def max_heapify(arr, i, n):
    l_pos = 2*i+1
    r_pos = 2*i+2

    if l_pos<n and arr[l_pos]>arr[i]:
        largest = l_pos
    else:
        largest = i
    if r_pos<n and arr[r_pos]>arr[largest]:
        largest = r_pos

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, n)
    

def heap_sort(arr):
    #create max_heap
    n=len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(data, i, n)

    #Sort
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)

data = [19,12,16,1,4,7,17,23,27]
heap_sort(data)
print("Sorted data:", data)

