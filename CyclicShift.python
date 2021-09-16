t = int(input())
while t!=0:
    n,k = map(int, input().split())
    a = input()
    max = ""
    f = -1
    for i in range(n):
        if max < a:
            max = a
            rt = i
        elif max == a:
            f = i - rt
            break
        a = a[1:] + a[:1]
    if f == -1:
        print(rt + (k-1)*n)
    else:
        print(rt + (k-1)*f)
    print ("")
    t = t-1
