import random as rm


def mil_rab(p):
    '''Test di rpimalità di miller rabin
    '''
    if p == 1 or p % 2 == 0: return False
    if p == 2: return True
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = rm.randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1: return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1: return False
        if x == p - 1: return True
        k = k - 1
    return False


def is_prime(p, r):
    '''chiamando mil_rab controlla se un numero è primo
       r è il numero di tentativi
    '''
    for i in range(r):
        if mil_rab(p):
            return True
        else:
            return False


def gen_primo(k, r):
    '''genera casualmnete un numero primo di k bit
       r è il numero di tentativi
    '''
    if k < 2:
        return None
    while True:
        number = rm.randrange(pow(2, k - 1) + 1, pow(2, k), 2)
        if is_prime(number, r):
            return number


def MCD(a, b):
    '''Calcolo del massimo comune divisore fra a e b
    '''
    while b != 0:
        a, b = b, a % b
    return a


def CO(phi):
    '''calcola un numero che è coprimo con phi
    '''
    while True:
        H = rm.randrange(2, phi)
        if MCD(H, phi) == 1:
            return H


def EMCD(a, b):
    '''algoritmo esteso di eculide
    '''
    x = 0; X = 1
    y = 1; Y = 0
    r = b; R = a
    while r != 0:
        q = R // r
        R, r = r, R - q*r
        X, x = x, X - q*x
        Y, y = y, Y - q*y
    return R, X, Y


def MI(a, b):
    ''' tramite ECDM calcola l'inverso moltiplicativo
    '''
    g, x, y = EMCD(a, b)
    if x < 0:
        x += b
    return x


def gen_chiavi(dim, r):
    '''genera le chiavi lunghe dim bit
    '''
    p = gen_primo(dim, r)
    q = gen_primo(dim, r)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = CO(phi)
    d = MI(e, phi)
    return N, e, d


def cifra(e, N, msg):
    '''cifra il messaggio
    '''
    cifr = ""
    for l in msg:
        m = ord(l)
        M = pow(m, e, N)
        cifr += str(M) + " "
    return cifr


def decifra(d, N, cifr):
    '''decifra il messaggio
    '''
    msg = ""
    lett = cifr.split()
    for l in lett:
        c = int(l)
        C = pow(c, d, N)
        msg += chr(C)
    return msg


def main():

    print("Il codice codifica e decodifica testi presenti su un txt. \n"
          "Anche le chiavi se, già si possiedono, devono essere in un txt\n"
          "nell'ordine N, e, d, separate da un a capo.")
    print()
    print("Si è in possesso o si vuole generare la chiave?\ndigitare 0 per generarle, 1 altrimenti")
    E = int(input("generare?"))
    if E == 0:
        dim = int(input("dimensione in bit della chiave:"))
        r = int(input("numeri di tentativi per il test di miller rabin, 40 possono andare:"))
        p = input('inseire path dove salvare il file:\n')
        N, e, d = gen_chiavi(dim, r)
        path = r"%s.txt"%p
        file = open(path, "w")
        file.write(str(N))
        file.write('\n')
        file.write(str(e))
        file.write('\n')
        file.write(str(d))
        file.close()
        print("Chiavi generate, veranno lette automaticamente")

    while True:
        A = int(input("\n"
                      "Digitare 1 per leggere file.txt da cifrare \n"
                      "Digitare 2 per leggere file.txt da decifrare \n"
                      "Digitare 3 per terminare l'esecuzione \n"))

        if A == 1:
            if E == 0:
                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                e = int(chiave[1])

            elif E == 1:
                f = input("Path assoluto del file con le chiavi: \n")
                path = r"%s.txt"%f
                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                e = int(chiave[1])


            f = input("Path assoluto del file da leggere: \n")
            pathl = r"%s.txt"%f
            f1 = input("Path assoluto del file su cui scrivere\n"
                       "se non esiste esso viene creato automaticamente: \n")
            paths = r"%s.txt"%f1

            msg = open(pathl, "r").read()
            enc = cifra(e, N, msg)

            file = open(paths, "w")
            file.write(enc)
            file.close()

            print("Mesaggio cifrato e stamapto")

        elif A == 2:
            if E == 0:
                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                d = int(chiave[2])

            elif E == 1:
                f = input("Path assoluto del file con le chiavi: \n")
                path = r"%s.txt"%f
                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                d = int(chiave[2])

            f = input("Path assoluto del file da leggere: \n")
            pathl = r"%s.txt"%f
            f1 = input("Path assoluto del file su cui scrivere\n"
                       "se non esiste esso viene creato automaticamente: \n")
            paths = r"%s.txt"%f1

            enc = open(pathl, "r").read()
            dec = decifra(d, N, enc)

            file = open(paths, "w")
            file.write(dec)
            file.close()

            print("Mesaggio decifrato e stamapto")

        elif A == 3:
            print("garzie e arrivederci")
            break

main()
