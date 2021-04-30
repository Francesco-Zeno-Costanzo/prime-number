# prime-number
The first code calculates the first prime numbers smaller than a given N and returns the graph of the enumerative function and its two main approximations;
the second is a small implementation of the Goldbach conjecture.

The RSA method is an asymmetric public key cryptographic algorithm.
The user must independently generate two keys: one public and accessible to all that can be used by another user to encrypt the message to be sent, a private one known only by the user which is used to decrypt the message received.


Math behind RSA: We are searching for a number d such that 
<a href="https://www.codecogs.com/eqnedit.php?latex=e^d&space;~&space;mod(n)&space;=&space;m^{ed}&space;~&space;mod(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e^d&space;~&space;mod(n)&space;=&space;m^{ed}&space;~&space;mod(n)" title="e^d ~ mod(n) = m^{ed} ~ mod(n)" /></a>
and ed = 1 mod((p-1)(q-1)).
From the last equation we obtain
<a href="https://www.codecogs.com/eqnedit.php?latex=ed&space;=&space;mod(p-1)&space;\text{&space;and&space;}&space;ed&space;=&space;mod(q-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ed&space;=&space;mod(p-1)&space;\text{&space;and&space;}&space;ed&space;=&space;mod(q-1)" title="ed = mod(p-1) \text{ and } ed = mod(q-1)" /></a>
Using, then, Fermat's little theorem we get
<a href="https://www.codecogs.com/eqnedit.php?latex=m^{ed}&space;=&space;m&space;~&space;mod(p)&space;\text{&space;and&space;}&space;m^{ed}&space;=&space;m&space;~&space;mod(q)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m^{ed}&space;=&space;m&space;~&space;mod(p)&space;\text{&space;and&space;}&space;m^{ed}&space;=&space;m&space;~&space;mod(q)" title="m^{ed} = m ~ mod(p) \text{ and } m^{ed} = m ~ mod(q)" /></a>
We observe now that p and q are different prime numbers so we can use Chinese remainder theorem obtaining that
<a href="https://www.codecogs.com/eqnedit.php?latex=m^{ed}&space;=&space;m&space;~&space;mod(pq)&space;\Rightarrow&space;e^d&space;=&space;m&space;~&space;mod(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m^{ed}&space;=&space;m&space;~&space;mod(pq)&space;\Rightarrow&space;e^d&space;=&space;m&space;~&space;mod(n)" title="m^{ed} = m ~ mod(pq) \Rightarrow e^d = m ~ mod(n)" /></a>
To find d such that ed = 1 mod((p-1)(q-1)) we use the Extended Euclidean algorithm which, in this case, states that 
<a href="https://www.codecogs.com/eqnedit.php?latex=ed&space;&plus;&space;my&space;=&space;gcd(a,&space;b)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ed&space;&plus;&space;my&space;=&space;gcd(a,&space;b)" title="ed + my = gcd(a, b)" /></a>
