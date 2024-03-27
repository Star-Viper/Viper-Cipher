import math

def create_matrix_from_cipher(ciphertext):
    # Calculate the number of rows needed for the matrix
    rows = math.ceil(len(ciphertext) / 3)

    # Create an empty matrix
    matrix = [['' for _ in range(3)] for _ in range(rows)]

    # Start filling the matrix from the last of the first row
    index = 0
    for j in range(2, -1, -1):
        if j % 2 == 0:
            for i in range(rows):
                if index < len(ciphertext):
                    matrix[i][j] = ciphertext[index]
                    index += 1
        else:
            for i in range(rows - 1, -1, -1):
                if index < len(ciphertext):
                    matrix[i][j] = ciphertext[index]
                    index += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def print_elements(matrix):
    concatenated_string = ""
    for row in matrix:
        concatenated_string += ''.join(row)
    print("Concatenated string:", concatenated_string)
    reversed_string = concatenated_string[::-1]
    print("Reversed string:", reversed_string)

def main():
    ciphertext = input("Enter the ciphertext: ")
    matrix = create_matrix_from_cipher(ciphertext)
    print("Matrix:")
    print_matrix(matrix)
    print("Elements:")
    print_elements(matrix)

if __name__ == "__main__":
    main()


# 5.1 76)3&"-*