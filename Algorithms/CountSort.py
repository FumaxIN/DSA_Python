def count_sort(arr):
    count_arr = [0] * (max(arr)+1)
    output_arr = [0] * len(arr)

    for i in range(0, len(arr)):
        count_arr[arr[i]] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1

    return(output_arr)


data = [2,9,7,1,5,6,3]
sorted_data = count_sort(data)
print("Sorted data:\t", sorted_data)