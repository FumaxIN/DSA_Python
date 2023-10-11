def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


data = [2,9,7,1,5,6,3]
bubble_sort(data)
print("Sorted data:\t", data)