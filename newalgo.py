def encrypt(plaintext, key):
    # Step 2: Shifting
    shifted_text = ""
    for char in plaintext:
        if char.isalpha():
            shifted_text += chr(((ord(char) - 65 + key) % 26) + 33)  # Shifting and converting to special characters
        elif char == " ":
            shifted_text += "@"
        else:
            shifted_text += char
    
    # concate string
    reversed_text = shifted_text[::-1]
    
    matrix = [reversed_text[i:i+3] for i in range(0, len(reversed_text), 3)]
    
    # ciphertext
    ciphertext = ""
    for i in range(len(matrix)):
        if i % 2 == 0:
            ciphertext += matrix[i]
        else:
            ciphertext += matrix[i][::-1]
    
    return ciphertext

def decrypt(ciphertext, key):
    matrix = []
    index = 0
    while index < len(ciphertext):
        if len(matrix) % 2 == 0:
            matrix.append(ciphertext[index:index+3])
        else:
            matrix.append(ciphertext[index:index+3][::-1])
        index += 3
    
    # Step 2: Reverse the matrix
    # matrix = matrix[::-1]
    # print("Reversed Matrix:")
    for row in matrix:
        print(row)
    
    # Step 3: Extract the reversed text from the matrix
    reversed_text = ""
    for row in matrix:
        reversed_text += row
    print("Reversed Text:", reversed_text)
    
    # Step 4: Reverse the concatenated string
    reversed_text = reversed_text[::-1]
    print("Reversed Text After Reversal:", reversed_text)
    
    # Step 5: Shift the reversed text back to PTEXT
    PTEXT = ""
    for char in reversed_text:
        PTEXT += chr((ord(char) - 33 - key)  + 65)
        # if char.isalpha():
        #     PTEXT += chr((ord(char) - 33 - key)  + 65)
        # elif char == "@":
        #     PTEXT += " "
        # else:
        #     PTEXT += char
    print("Decrypted plaintext: ",PTEXT)
    return PTEXT

plaintext = input("ENter pt: ")
key = int(input("entey key: "))
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
ptext =decrypt(ciphertext, key)

