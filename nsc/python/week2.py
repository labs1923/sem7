import numpy as np
def generate_Key_Matrix(key):
    key_mat = np.array([[0,0,0],[0,0,0],[0,0,0]])
    k = 0
    for i in range(3):
        for j in range(3):
            key_mat[i][j] += ord(key[k])-65
            k += 1
    return key_mat
def generate_Plain_text_Matrix(pt): 
    pt_mat = np.array([[0],[0],[0]])   
    for i in range(3):
        pt_mat[i][0] += ord(pt[i])-65
    return pt_mat
def HillCipher(key_mat,pt_mat):
    ct_mat = np.array([[0,0,0],[0,0,0],[0,0,0]])
    for i in range(3):
        for j in range(1):
            ct_mat[i][j] = 0
            for x in range(3):
                ct_mat[i][j] += (key_mat[i][x]*pt_mat[x][j])
            ct_mat[i][j] = ct_mat[i][j]%26
    return ct_mat
def MatrixInverse(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv
pt = input("Enter the Plain Text :").upper()
key = input("Enter the Key :").upper()
pt1 = generate_Plain_text_Matrix(pt)
key1 = generate_Key_Matrix(key)
K_inverse = MatrixInverse(key1)
ctm = HillCipher(key1,pt1)
p1 = HillCipher(K_inverse,ctm)
ct = []
for i in range(3):
    ct.append(chr(ctm[i][0]+65))
print("Original Plain Text : ",pt)
print("Entered Key : ",key)
print("Encrypted Cipher Text : ","".join(ct))
dt = []
for i in range(3):
    dt.append(chr(p1[i][0]+65))
print("Decrypted Original Plain text : ","".join(dt))