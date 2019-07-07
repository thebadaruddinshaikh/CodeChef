def splitter(n):
    add = 0
    n.split()
    for k in n:
        add = add + int(k)
    print(add)
att = int(input())
la = []
i = 0
while i < att:
    la.append(input())
    i+=1
for j in la:
    splitter(j)
