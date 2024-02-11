def fibonacci_series(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series


# Taking the number of terms as input from the user
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Generating and printing the Fibonacci series
result = fibonacci_series(n)
print("Fibonacci Series:", result)
