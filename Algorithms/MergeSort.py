def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        
        merge_sort(l_arr)
        merge_sort(r_arr)

        i=j=k=0
        # compare and copy elements into new array
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i+=1
            else:
                arr[k] = r_arr[j]
                j+=1
            k+=1

        # copy leftover elements
        while i<len(l_arr):
            arr[k] = l_arr[i]
            i+=1
            k+=1
        while j<len(r_arr):
            arr[k] = r_arr[j]
            j+=1
            k+=1


data = [2,9,7,1,5,6,3]
merge_sort(data)
print("Sorted data:\t", data)