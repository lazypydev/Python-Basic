def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    text = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')
