n = int(input('Scegli numero maggiore di 2: '))


def primo(x):   #ritorna True se x è primo
    for y in range(2,x):
        if(x%y == 0):
            return False
    return True

n1=2
n2=n-2
while(n1 <= n2):
    if(primo(n1) and primo(n2)):
        print(n1,n2)
    n1+=1
    n2-=1