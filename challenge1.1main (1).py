def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
Output:

csharp
Copy code
The factorial of 5 is 120
This code defines a function factorial that uses recursion to calculate the factorial of a given number. In this example, it calculates the factorial of 5, which is 5! = 5 * 4 * 3 * 2 * 1 = 120.




Is this conversation helpful so far?




