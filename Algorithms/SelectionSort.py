def selection_sort(arr):
    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]

data = [2,9,7,1,5,6,3]
selection_sort(data)
print("Sorted data:\t", data)