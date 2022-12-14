#1. --Linear Search--

def search(arr, target):
    for i in range(len(arr)):
        
        if arr[i] == target:
            return i
arr = [2,5,18,30,13,22,14,42]
target = 13

print(search(arr, target))
# Answer 4