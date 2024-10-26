def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    key = int(input("Enter the key: "))

    decrypted_message = caesar_decrypt(ciphertext, key)
    print(f"Decrypted message: {decrypted_message}")