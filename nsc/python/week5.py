def a_public_value(p,g,a):
    x_a = g**a
    return x_a%p

def b_public_value(p,g,b):
    x_b = g**b
    return x_b%p

p=int(input("Enter public number P : "))
g=int(input("Enter primitive root of P : "))
a=int(input("Enter private key of a : "))
b=int(input("Enter private key of b : "))
p_a=b_public_value(p,g,b)
p_b=a_public_value(p,g,a)

sym_a = (p_a**a)%p
sym_b = (p_b**b)%p

print("The secret key for a :",sym_a)
print("The secret key for b :",sym_b)