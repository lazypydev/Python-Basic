def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))
    print(f'The factorial of {number} is {factorial(number)}.')
