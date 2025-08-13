print(" Caesor Cipher")

pt= input(" Enter the plain Text : ")
key= int(input("Enter the Key : "))

def encrypt(pt,key):
    ct=""
    for ch in pt:
        if ch.isupper():
            ch=chr((ord(ch)-ord('A')+key)% 26 + ord('A'))
            ct+=ch
        elif ch.islower():
            ch=chr((ord(ch)-ord('a')+key)% 26 + ord('a'))
            ct+=ch
        else :
            ct+=ch
    return ct
     
        
def decrypt(pt,key):
    ct=""
    for ch in pt:
        if ch.isupper():
            ch=chr((ord(ch)-ord('A')-key)% 26 + ord('A'))
            ct+=ch
        elif ch.islower():
            ct+=ch
            ch=chr((ord(ch)-ord('a')-key)% 26 + ord('a'))
            ct+=ch
    return ct    

print("Encrypted Text is :"+ encrypt(pt,key))    
print("Decrypted Text is :"+ decrypt(encrypt(pt,key),key))   