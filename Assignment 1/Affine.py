print(" Affine Cipher")

pt=input("Enter the Plain Text : ")
a=int(input("Enter the key (a) :"))
b=int(input("Enter the key (b) :"))

def aff_encrypt(pt,a,b):
    ct=""
    for ch in pt:
        if ch.isupper():
            ch=chr(((a*(ord(ch)-ord('A'))+b)%26)+ord('A'))
        elif ch.islower():
            ch=chr(((a*(ord(ch)-ord('a'))+b)%26)+ord('a'))
        ct+=ch
    return ct
ct=aff_encrypt(pt,a,b)
print("Cipher Text :",ct)