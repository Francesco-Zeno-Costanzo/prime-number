import time
import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt

N = int(input('Scegli N: ')) #Stampa i primi N numeri primi
start_time=time.time()
b = 0
y=np.array([])
x=np.array([])
h=0
for k in range(2,N):
    #Controlla se e' divisibile per qualche numero...
    for D in range(2, k+1):
        b = 1
        if ((k % D) == 0) and (k != D):
            b = 0 #E' divisibile, non e' un numero primo
            break
    if b:
        print (k)
        h+=1
        y=np.insert(y, len(y), h)
        x=np.insert(x, len(x), k)

def g(x):
    return x/np.log(x)

def Li(x):
    return sc.expi(np.log(x))

y=y-1
t=np.linspace(2, N, 10000000)
plt.figure(1)
plt.grid()
plt.title('Funzione enumerativa dei numeri primi')
plt.plot(x, y, color ='black', label=r'$ \pi(x) $')
plt.plot(t, Li(t), color= 'red', label='Li(x)')
plt.plot(t, g(t), color='blue', label=r'$\frac{x}{\lnx} $')
plt.legend(loc='best')
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))

