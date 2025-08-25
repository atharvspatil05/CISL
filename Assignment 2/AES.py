from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key_aes = get_random_bytes(16)
cipher_aes = AES.new(key_aes, AES.MODE_EAX)
plaintext_aes = b'HelloAES'

ciphertext_aes, tag = cipher_aes.encrypt_and_digest(plaintext_aes)
print("AES Encrypted (ciphertext):", ciphertext_aes)
print("Nonce:", cipher_aes.nonce)
print("Tag:", tag)

cipher_aes_dec = AES.new(key_aes, AES.MODE_EAX, nonce=cipher_aes.nonce)
decrypted_aes = cipher_aes_dec.decrypt_and_verify(ciphertext_aes, tag)
print("AES Decrypted:", decrypted_aes)
