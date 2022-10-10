import numpy as np
import math
def hillcipher(pt,key):
    keyMatrix(key,len(pt))
    for i in range(1):
        for j in range(len(pt)):
            pm[i][j] = ord(pt[j]) % 65
    encrypted_text = encrypt()
    print("Plain text :",pt)
    print("Encrypted text :",encrypted_text)
    decrypted_text = decrypt(km)
    print("Decrypted text :",decrypted_text)
def encrypt():
    k=0
    for i in range(len(km)):
        for j in range(len(km)):
            et[0][k]=et[0][k]+(km[i][j]*pm[0][j])
        k=k+1
    encrypted_text=""
    for i in range(len(et[0])):
        encrypted_text += chr(et[0][i]%26+65)
    return encrypted_text
def decrypt(km):
    km = np.array(km)
    det = np.linalg.det(km)
    km=np.linalg.inv(km)
    k=0
    for i in range(len(km)):
        for j in range(len(km)):
            dt[0][k]=dt[0][k]+(km[i][j]*et[0][j])
        k+=1
    decrypted_text=""
    for i in range(len(dt[0])):
        decrypted_text += chr(round(dt[0][i])+65)
    return decrypted_text
def keyMatrix(key,n):
    k=0
    for i in range(n):
        for j in range(n):
            km[i][j] = ord(key[k]) % 65
            k=k+1
pt=input("Enter plain text :")
key=input("Enter key :")
km = [[0]*len(pt) for i in range(len(pt))]
pm = [[0]*len(pt) for i in range(1)]
et = [[0]*len(pt) for i in range(1)]
dt = [[0]*len(pt) for i in range(1)]
hillcipher(pt,key)
