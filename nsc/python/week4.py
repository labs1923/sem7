def gcd(a,b):
    if (b==0):
        return a
    return gcd(b,a%b)

m=int(input("Enter input message number : "))
p=int(input("Enter a prime number p : "))
q=int(input("Enter a prime number q : "))
n=p*q
fi_n=(p-1)*(q-1)

e=1
for i in range(2,fi_n):
    if(gcd(i,fi_n)==1):
        e=i
        break

d=1
for i in range(2,fi_n):
    if((i*e)%fi_n==1 and i!=e):
        d=i
        break

enc=(m**e)%n
print("encrypted text : ",enc)

dec=(enc**d)%n
print("decrypted text : ",dec)