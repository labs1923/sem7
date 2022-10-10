def encrypt(pt,key=3):
    et = ""
    for i in range(len(pt)):
        et += chr((ord(pt[i])+key-65)%26+65)
    return et.upper()
def decrypt(ct,key=3):
    dt = ""
    for i in range(len(ct)):
        dt += chr((ord(ct[i])-key-65)%26+65)
    return dt.upper()
pt = input("Enter the Plain text : ").upper()
key = int(input("Enter the Key : "))
print("Plain Text :",pt,"\nKey :",key)
while(True):
    ch = int(input("0.Exit\n1.Encryption\n2.Decryption\nEnter Your Choice :"))
    if(ch==0):
        exit()
    elif(ch==1):
        cipher_text = encrypt(pt,key)
        print("Original Text After Encryption :",cipher_text)
    elif(ch==2):
        orig_text = decrypt(cipher_text,key)
        print("Original Text After Decryption :",orig_text)
    else:
        print("Invalid Inputs!!")