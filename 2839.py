n = int(input())
count = []
if n % 5 == 0:
    print(int(n/5))
else :
    for i in range(0, n//5+1):
        tmp = n
        tmp = tmp -5*i
        if tmp % 3 == 0:
            count.append(int(tmp/3)+i)
    if len(count) == 0:
        print(-1)
    else :
        print(min(count))
        