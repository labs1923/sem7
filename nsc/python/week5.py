def primitive(n):
    l=[]
    for i in range(1,n):
        for j in range(0,n-1):
            k = int(pow(i,j,n))
            if k not in l:
                l.append(k)
        if len(l)==n-1:
            return i
        l.clear()

p = int(input("enter p "))
g = primitive(p)
print(g)
a = int(input("enter a "))
b = int(input("enter b "))

x = int(pow(g,a,p))
y = int(pow(g,b,p))

print(' keys of a is x=',x)
print(' keys of b is y=',y)

k1 = int(pow(y,a,p))
k2= int(pow(x,b,p))

print('Secret key for the a is',k1)
print('Secret key for the is',k2)
