
t = int(input())
z=0
while z < t:
    n = int(input())
    m =[]
    count=0
    for j in range(n):
            f = list(map(int,input().split()))
            m.append(f)
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q:
                        if m[i][j]>m[p][q]:
                            count+=1
    print(count)
    z+=1   
