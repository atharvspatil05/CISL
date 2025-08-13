print(" Keyword Cipher")

pt=input("Enter Plain Text : ")
key=input("Enter Keyword : ").upper()

alphabet=''.join(dict.fromkeys(key+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

c=''
for ch in pt:
    if ch.isalpha():
        i=ord(ch.upper())-65
        sub = alphabet[i]
        c+=sub if ch.upper() else sub.lower()
    else:
        c+=ch

print("Encrypted Message :",  c)

