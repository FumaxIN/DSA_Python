def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

data = [2,9,7,1,5,6,3]
insertion_sort(data)
print("Sorted data:\t", data)