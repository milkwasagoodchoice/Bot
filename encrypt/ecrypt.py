def encrypt_caesar(message, key):
    result = []
    shift = key % 26
    for char in message:
        if char.isalpha():
            if char.islower():
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif char.isupper():
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    key = int(input("Enter key: "))
    message = input("Enter message: ")
    encrypted_message = encrypt_caesar(message, key)
    print(f"Result: {encrypted_message}")
