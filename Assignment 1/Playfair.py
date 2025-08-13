print("Playfair Cipher")

def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    seen = set()

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]


def format_plaintext(plaintext):
    text = ''.join(filter(str.isalpha, plaintext)).upper().replace('J', 'I')
    result = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + 'X'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'X'
            i += 1
    return result


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def PlayfairEncrypt(plaintext, key):
    matrix = generate_matrix(key)
    plaintext = format_plaintext(plaintext)
    ciphertext = ''

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

print("Playfair Cipher")

plaintext = input("Enter the plaintext message: ")
key = input("Enter the keyword: ")

cipher = PlayfairEncrypt(plaintext, key)
print("Encrypted Text:", cipher)
