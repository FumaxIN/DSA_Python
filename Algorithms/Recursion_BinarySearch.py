def binary_search(data, target, low, high):
    mid = (low+high)//2
    
    if low > high:
        return False
    else:
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        elif data[mid] < target:
            return binary_search(data, target, mid+1, high)
        
arr = list(map(int, input("Enter list of numbers: ").split()))
item = int(input("Enter a number: "))
loc = binary_search(arr, item, 0, len(arr)-1)
if loc:
    print("Element fount at: ", loc+1)
print('Element not found')