print("Vigenere Cipher")

plaintext = input("Enter the plaintext : ")
keyword = input("Enter the Keyword : ")

cipherText = []

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        is_upper = plaintext[i].isupper()
        index = (ord(plaintext[i].upper()) - ord('A') + ord(keyword[i % len(keyword)].upper()) - ord('A')) % 26
        substituted_char = chr(index + ord('A'))
        if not is_upper:
            substituted_char = substituted_char.lower()
        cipherText.append(substituted_char)
    else:
        cipherText.append(plaintext[i])     

print("Encrypted Text:", ''.join(cipherText))      