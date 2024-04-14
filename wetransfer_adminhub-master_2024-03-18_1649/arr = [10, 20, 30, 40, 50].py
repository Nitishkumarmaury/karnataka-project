arr = [10, 20, 30, 40, 50]
x = 10

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

index = linear_search(arr, x)

if index != -1:
    print(f"value at index {index}")
else:
    print(f" not found ")



# binary
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
       
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

index = binary_search(arr, 0, len(arr)-1, x)

if x==x:
    print(f"Binary search")

if index != -1:
   
    print(f"value at index {index}")
else:
    print(f" not found ")