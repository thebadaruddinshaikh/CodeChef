x = int(input())
i = 0
la = []
while i < x:
    la.append(int(input()))
    i+=1
for i in la:
    f = 1
    for j in range(1,i+1):
        f = f*j
    print(f)
