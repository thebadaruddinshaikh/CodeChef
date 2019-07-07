x = int(input())
i = 0
while i < x:
    k = input()
    a,b = map(int,k.split())
    if b == 0:
        i+=1
        continue
    print(a%b)
    i+=1
