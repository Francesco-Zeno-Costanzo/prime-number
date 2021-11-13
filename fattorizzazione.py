import numpy as np

n = 99881*40387

##algoritmo di Fermat

a = int(np.sqrt(n)+1)
while True:
    b2 = a**2 - n
    if np.sqrt(b2) - int(np.sqrt(b2)):
        a += 1
    else:
        b = np.sqrt(b2)
        break

m = (a-b)*(a+b)

print(n)
print(a-b, a+b)

##fattorizzazione con goldbach debole

r = 23 #deve esser primo
v = r + 2*int(np.sqrt(n))
x = ((v - r) + np.sqrt(abs((v - r)*(v - r) - 4*n)))/2

while x != int(x):
    v = v + 2
    x = ((v - r) + np.sqrt(abs((v - r)*(v - r) - 4*n)))/2

print(x, n/x)

##fattorizzazione con l'ipotesi di Riemann

M = np.sqrt(n)/np.log(np.sqrt(n))
pm = M*(np.log(M) + np.log(np.log(M))-1)
k = int(pm)

if k/2 == int(k/2):
    k = k+1

while n/k != int(n/k):
    k = k+2

p = k
q = n/k

print(p,q)