print("Fibonacci Series using recursion\n")
n = int(input("Enter the number of terms: "))
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")