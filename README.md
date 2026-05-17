# Fibonacci-series-using-recursion
Fibonacci Series using Recursion

This Python program prints the Fibonacci series using recursion.

What is Recursion?

Recursion is a method where a function calls itself repeatedly to solve a problem.

In this program, the fibonacci() function calls itself to calculate previous Fibonacci numbers.

Fibonacci Formula

Each number is the sum of the previous two numbers:

F(n)=F(n−1)+F(n−2)

Base conditions:

F(0)=0,F(1)=1

How the Program Works
Step 1

User enters the number of terms.

Example:

Enter the number of terms: 7
Step 2

The function checks base cases:

if n <= 0:
    return 0

elif n == 1:
    return 1

These stop the recursion.

Step 3

For other numbers, function calls itself:

return fibonacci(n-1) + fibonacci(n-2)

Example:

fibonacci(5)
= fibonacci(4) + fibonacci(3)

The process continues until base conditions are reached.

Example Output
Enter the number of terms: 7
Fibonacci Series:
0 1 1 2 3 5 8
Time Complexity
O(2ⁿ)
Because the function repeatedly recalculates values.
Space Complexity
O(n)
Due to recursive function call stack.
Concepts Used
Functions
Recursion
Base Case
Loop
Function Calling
Mathematical Series
