x = int(input())
i = 0
la = []
while i < x:
    la.append(input())
    i+=1
for i in la:
    u = i.__len__() -1
    add = int(i[0]) + int(i[u])
    print(add)
