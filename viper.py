import math

def substitute_characters(plaintext, key):
    substitution_dict = {}
    for letter in range(ord('A'), ord('Z') + 1):
        ascii_value = ord('!') + ((letter - ord('A') + key) % 26)
        substitution_dict[chr(letter)] = chr(ascii_value)

    ciphertext = ""
    for char in plaintext:
        if char.isalpha() and char.isupper():
            ciphertext += substitution_dict[char]
        else:
            ciphertext += char
    return ciphertext

def reverse_text(text):
    return text[::-1]

def create_cipher_matrix(text):
    rows = math.ceil(len(text) / 3)
    matrix = []
    for i in range(0, len(text), 3):
        matrix.append(list(text[i:i+3].ljust(3, ' ')))
    return matrix

def zigzag_read_matrix(matrix):
    result = ""
    for j in range(2, -1, -1):
        if j % 2 == 0:
            for i in range(len(matrix)):
                result += matrix[i][j]
        else:
            for i in range(len(matrix)-1, -1, -1):
                result += matrix[i][j]
    return result

def main():
    plaintext = input("Enter the plaintext (capital letters only): ")
    key = int(input("Enter the key (1 to 26): "))

    if not (1 <= key <= 26):
        print("Invalid key. Key must be between 1 and 26.")
        return

    # Step 1:Substitution cipher
    substituted_text = substitute_characters(plaintext, key)
    print("Step 1 result:", substituted_text)

    # Step 2:Reverse the result
    reversed_text = reverse_text(substituted_text)
    print("Step 2 result:", reversed_text)

    # Step 3:Create matrix
    cipher_matrix = create_cipher_matrix(reversed_text)
    print("Matrix:")
    for row in cipher_matrix:
        print(''.join(row))

    # Step 4:Zigzag read
    ciphertext = zigzag_read_matrix(cipher_matrix)
    print("Cipher text:", ciphertext)

if __name__ == "__main__":
    main()