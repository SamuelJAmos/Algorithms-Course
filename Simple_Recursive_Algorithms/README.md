# How to use this project 

1. Create new terminal folder at specific lessons folder 
    EX: Factorials_L01
2. In the terminal write __"Python3 main.py"__
    EX: In Factorials_L01 this command would run the following 
        ```
        # 1. Iterative method

        def iterative_factorial(n):
            fact = 1
            for i in range (2, n + 1):
                fact *= i
            return fact

        print(iterative_factorial(5))
        # Answer 120
        ```
        
        ```
        # 2. Recursive method

        def recursive_factorial(n):
            if n == 1:
                return n
            else:
                temp = recursive_factorial(n-1)
                temp = temp * n 
            return temp 

        print(recursive_factorial(4))
        # Answer 24
        ```