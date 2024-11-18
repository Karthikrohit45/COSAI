def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

n = 10

fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")
