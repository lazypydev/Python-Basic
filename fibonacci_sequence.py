def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    print(f'Fibonacci sequence with {num_terms} terms: {fibonacci(num_terms)}')
