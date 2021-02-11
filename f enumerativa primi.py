import time
import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt

N = int(input('Scegli N: ')) #Stampa i primi N numeri primi
start_time=time.time()
y=np.array([])
x=np.array([])
h=0
def isPrime(n):
    if(n==1):
         return False
    if(n%2 == 0 and n!=2):
         return False
    for i in range(3, n//2, 2):
        if(n%i == 0):
             return False
    return True

for i in range(N):
    if(isPrime(i)):
        #print(i)
        h+=1
        y=np.insert(y, len(y), h)
        x=np.insert(x, len(x), i)

def g(x):
    return x/np.log(x)

def Li(x):
    return sc.expi(np.log(x))

y=y-1
t=np.linspace(2, N, 10000)
plt.figure(1)
plt.grid()
plt.title('Funzione enumerativa dei numeri primi')
plt.plot(x, y, color ='black', label=r'$ \pi(x) $')
plt.plot(t, Li(t), color= 'red', label='Li(x)')
plt.plot(t, g(t), color='blue', label=r'$\frac{x}{\lnx} $')
plt.legend(loc='best')
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))

