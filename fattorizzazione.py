import numpy as np
'''
I codici nelle prime tre celle fattorizzano un numero in forma
di prodotto fra due numeri primi, purtroppo non va tutto sempre bene
e.g. n = 100 non produce due numeri primi poichè 100 ha una fattorizzazione
con più di due termini.
L'ultimo codice trova l'intera scomposizione in primi di un numero
'''
n =  99881*40387

##algoritmo di Fermat
def Fermat(n):
    a = int(np.sqrt(n)+1)
    while True:
        b2 = a**2 - n
        if np.sqrt(b2) - int(np.sqrt(b2)):
            a += 1
        else:
            b = np.sqrt(b2)
            break
    print(a-b, a+b)

Fermat(n)

#con 100, stampa 2 e 50
Fermat(100)



##fattorizzazione con goldbach debole
def GD(n):
    r = 23 #deve esser primo
    v = r + 2*int(np.sqrt(n))
    x = ((v - r) + np.sqrt(abs((v - r)*(v - r) - 4*n)))/2

    while x != int(x):
        v = v + 2
        x = ((v - r) + np.sqrt(abs((v - r)*(v - r) - 4*n)))/2

    print(x, n/x)

GD(n
)
#con 100 stampa 10 e 10
GD(100)

##fattorizzazione con l'ipotesi di Riemann
def IR(n):
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

IR(n)

#con 100 stampa 5 e 20
IR(100)

##Scomposizione in primi completa

def fattori(n):
    i = 2
    f = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            f.append(i)
    if n > 1:
        f.append(n)
    return f

R = range(10)

a = {n: fattori(n) for n in R}
print(a)

