t  = int(input())
for i in range(t):
    n,k = map(int, input().split())
    A = list(map(int, input().split()))
    p=k%n
    A = A[n-p:]+A[:n-p]
    print(*A) #remove[] and ,
    i=i+1
