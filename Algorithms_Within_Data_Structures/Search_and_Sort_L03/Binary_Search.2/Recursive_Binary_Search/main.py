# --Recursive Binary Search--

def binary_rec(arr, start, end, target):
    if end >= start:

        mid = start + end - 1 // 2 

        if arr[mid] < target:
            binary_rec(arr, mid + 1, end, target)
        
        elif arr[mid] > target:
            return binary_rec(arr, start, mid - 1, target)
        else:
            return mid
    else: 
        return -1 

arr = [2,5,8,10,16,22,25]
target = 10

result = binary_rec(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is presented at index %d" % result)
else:
    print("Element is not presented in array")

# Answer 3