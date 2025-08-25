from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key_des = b'12345678'
cipher_des = DES.new(key_des, DES.MODE_ECB)
plaintext_des = b'HelloDES' 
ciphertext_des = cipher_des.encrypt(plaintext_des)

print("DES Encrypted:", ciphertext_des)

decipher_des = DES.new(key_des, DES.MODE_ECB)
decrypted_des = decipher_des.decrypt(ciphertext_des)

print("DES Decrypted:", decrypted_des)
