def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Number of terms
n_terms = int(input("Enter the number of terms: "))

# Print Fibonacci series
print([fibonacci(i) for i in range(1, n_terms + 1)])