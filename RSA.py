import numpy as np
import random as rm

def mil_rab(p):
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
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
    for i in range(r):
        if mil_rab(p) == True:
            return True
        else:
            return False


def gen_primo(k, r):
    if k < 2:
        return None
    while True:
        number = rm.randrange(pow(2, k - 1) + 1, pow(2, k), 2)
        if is_prime(number, r):
            return number


def MCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def CO(phi):
    while True:
        H=rm.randrange(2, phi)
        if MCD(H, phi)==1:
            return H


def EMCD(a, b):
    x=0; X=1
    y=1; Y=0
    r=b; R=a
    while r!=0:
        q = R // r
        R, r = r, R - q*r
        X, x = x, X - q*x
        Y, y = y, Y - q*y
    return R, X, Y


def MI(a, b):
    g, x, y =EMCD(a, b)
    if x<0:
        x+=b
    return x


def gen_chiavi(dim, r):
    p=gen_primo(dim, r)
    q=gen_primo(dim, r)
    N=p*q
    phi=(p-1)*(q-1)
    e=CO(phi)
    d=MI(e, phi)
    return N, e, d


def cifra(e, N, msg):
    cifr = ""
    for l in msg:
        m = ord(l)
        M = pow(m, e, N)
        cifr += str(M) + " "
    return cifr


def decifra(d, N, cifr):
    msg = ""
    lett = cifr.split()
    for l in lett:
        c = int(l)
        C = pow(c, d, N)
        msg += chr(C)
    return msg


def main():
    i=0
    print("Il codice codifica e decodifica testi presenti su un txt. \n"
          "Anche le chiavi se, già si possiedono, devono essere in un txt\n"
          "nell'ordine N, e, d, separate da un a capo.")
    print()
    print("Si è in possesso o si vuole generare la chiave?\ndigitare 0 per generarle, 1 altrimenti")
    E=int(input("generare?"))
    if E==0:
        dim=int(input("dimensione in bit della chiave:"))
        r=int(input("numeri di tentativi per il test di meller rabin, 40 possono andare:"))
        N, e, d=gen_chiavi(dim, r)
        path=r"C:\\Users\\franc\\Desktop\\chiavi.txt"
        file= open(path, "w")
        file.write(str(N))
        file.write('\n')
        file.write(str(e))
        file.write('\n')
        file.write(str(d))
        file.close()
        print("Chiavi generate e stampate su un file su desktop, verranno poi lette automaticamente")

    while True:
        if(i!=0):
            print("Ora che vuoi fare?")
        A=int(input("\n"
                    "Digitare 1 per leggere file.txt da cifrare \n"
                    "Digitare 2 per leggere file.txt da decifrare \n"
                    "Digitare 3 per terminare l'esecuzione'\n"))

        if A==1:
            if E==0:
                path=r"C:\\Users\\franc\\Desktop\\chiavi.txt"
                chiave=open(path, "r").read()
                chiave=chiave.split()
                N=int(chiave[0])
                e=int(chiave[1])

            elif E==1:
                f=input("Path assoluto del file con le chiavi (doppio \):")
                path=r"%s.txt"%f
                chiave=open(path, "r").read()
                chiave=chiave.split()
                N=int(chiave[0])
                e=int(chiave[1])

            G=int(input("digita 0 se il txt non è sul desktop, 1 altrimenti:"))

            if G==0:
                f=input("Path assoluto del file da leggere (doppio \):")
                path=r"%s.txt"%f

                f1=input("Path assoluto del file su cui scrivere\n"
                         "se non esiste esso viene creato automaticamente:")
                path1=r"%s.txt"%f1

            elif G==1:
                f=input("Inserisci il nome del file da leggere:")
                path=r"C:\\Users\\franc\\Desktop\\%s.txt"%f

                f1=input("Inserisci il nome del file su cui scrivere\n"
                         "se non esiste esso viene creato automaticamente:")
                path1=r"C:\\Users\\franc\\Desktop\\%s.txt"%f1

            msg=open(path, "r").read()
            enc = cifra(e, N, msg)

            file= open(path1, "w")
            file.write(enc)
            file.close()


        elif A==2:
            if E==0:
                path=r"C:\\Users\\franc\\Desktop\\chiavi.txt"
                chiave=open(path, "r").read()
                chiave=chiave.split()
                N=int(chiave[0])
                d=int(chiave[2])

            elif E==1:
                f=input("Path assoluto del file con le chiavi (doppio \):")
                path=r"%s.txt"%f
                chiave=open(path, "r").read()
                chiave=chiave.split()
                N=int(chiave[0])
                d=int(chiave[2])

            G=int(input("Digita 0 se il txt non è sul desktop 1 altrimenti:"))

            if G==0:
                f=input("Path assoluto del file da leggere (doppio \):")
                path=r"%s.txt"%f

                f1=input("Path assoluto del file su cui scrivere\n"
                         "se non esiste esso viene creato automaticamente:")
                path1=r"%s.txt"%f1

            elif G==1:
                f=input("Inserisci il nome del file da leggere:")
                path=r"C:\\Users\\franc\\Desktop\\%s.txt"%f

                f1=input("Inserisci il nome del file su cui scrivere\n"
                         "se non esiste esso viene creato automaticamente:")
                path1=r"C:\\Users\\franc\\Desktop\\%s.txt"%f1

            enc=open(path, "r").read()
            dec = decifra(d, N, enc)

            file= open(path1, "w")
            file.write(dec)
            file.close()


        elif A==3:
            break
        i=i+1

main()