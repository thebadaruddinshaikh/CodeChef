att = int(input())
i = 0
la= []
while i < att:
    la.append(input())
    i+=1
for i in la:
    a,b = map(int,i.split())
    print(a+b)
