def partition(A, start, end):
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i=i+1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[end] = A[end], A[i+1]
    
    return i+1


def quick_sort(arr, low, high):
    if low<high:
        q = partition(arr, low, high)
        quick_sort(arr, low, q-1)
        quick_sort(arr, q+1, high)


data = [8,7,2,1,0,9,6]
quick_sort(data, 0, len(data)-1)
print("Sorted data:\t", data)