def flipper(l,u):
    for i in range(l,u+1):
        if la[i] == 1:
            la[i] = 0
        elif la[i] == 0:
            la[i] = 1
def headsup(l,u):
    q = 0
    for i in range(l,u+1):
        if la[i] == 0:
            q+=1
    print(q)
# coin array initiation
x = input()
n, o= map(int,x.split())
la= []
i = 0
while i < n:
    la.append(1)
    i+=1
i = 0
while i < o:
    com = input()
    oper,lower,upper = map(int,com.split())
    if oper == 0:
        flipper(lower,upper)
    elif oper == 1:
        headsup(lower,upper)
    i+=1
