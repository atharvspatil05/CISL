print("Hill Cipher")

import numpy as np
import string

A = string.ascii_uppercase
A_map = {ch: i for i, ch in enumerate(A)}

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def prepare(text):
    text = text.upper().replace(" ", "")
    return text + ('X' if len(text) % 2 else '')

def text_to_vec(text):
    return [A_map[c] for c in text]

def vec_to_text(vec):
    return ''.join(A[i % 26] for i in vec)

def encrypt(text, K):
    text = prepare(text)
    nums = text_to_vec(text)
    result = ''
    for i in range(0, len(nums), 2):
        pair = np.dot(K, nums[i:i+2]) % 26
        result += vec_to_text(pair)
    return result

def decrypt(cipher, K):
    det = int(round(np.linalg.det(K))) % 26
    det_inv = modinv(det, 26)
    if det_inv is None:
        return "Key is not invertible modulo 26!"
    K_inv = det_inv * np.round(np.linalg.inv(K) * det).astype(int) % 26
    return encrypt(cipher, K_inv.astype(int))

plain = input("Enter plaintext (letters only): ")
print("Enter 2x2 key matrix values (row-wise):")
k11 = int(input("k11: "))
k12 = int(input("k12: "))
k21 = int(input("k21: "))
k22 = int(input("k22: "))
K = np.array([[k11, k12], [k21, k22]])


cipher = encrypt(plain, K)
decrypted = decrypt(cipher, K)

print("\nEncrypted:", cipher)
print("Decrypted:", decrypted)