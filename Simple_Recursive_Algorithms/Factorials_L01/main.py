# 1. Iterative method

# def iterative_factorial(n):
#     fact = 1
#     for i in range (2, n + 1):
#         fact *= i
#     return fact

# print(iterative_factorial(5))
# Answer 120

# 2. Recursive method

# def recursive_factorial(n):
#     if n == 1:
#         return n
#     else:
#         temp = recursive_factorial(n-1)
#         temp = temp * n 
#     return temp 

# print(recursive_factorial(4))
# Answer 24

# 3. Shorthand recursive method

# def recursive_factorial(n):
#     if n == 1: return n
#     else: return n * recursive_factorial(n-1)

# print(recursive_factorial(3))
# Answer 6 
