# --Bubble Sort Unoptimized--

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort_unop(A):
    iterations = 0 

    for i in A:
        for j in range(len(A) - 1):
            iterations += 1 
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
    return A, iterations

A = [9,8,7,6,5,4,3,2,1]

print(bubble_sort_unop(A))
# Answer ([1, 2, 3, 4, 5, 6, 7, 8, 9], 72) -- Double the iterations vs optimized