t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    a.sort()
    r = float('inf')
    for i in range (n-1):
        r = min(r,a[i]^a[i+1])
    print(int(r))
    t = t-1
