# 2. -Recursive method-

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        temp = temp * n 
    return temp 

print(recursive_factorial(4))
# Answer 24