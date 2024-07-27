def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    reversed_text = reverse_string(text)
    print(f'Reversed string: {reversed_text}')
