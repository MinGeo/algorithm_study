import math
limit = 10000
check = [1]*(limit*2+1)
check[0] = 0
check[1] = 0
for i in range(2,len(check)):
        if check[i]:
            for k in range(2, int(math.sqrt(i)+1)):
                if i % k == 0:
                    check[i] = 0
                    break
t = int(input())
for j in range(t):
    n = int(input())
    tmp1 = 0
    tmp2 = 0
    diff = 0
    count = 0
    for i in range(2, n+1):
        if check[i] == 1:
            if check[n - i] == 1:
                if count == 0:
                    tmp1, tmp2 = i, n-i
                    count += 1
                    diff = abs(i-(n-i))
                else :
                    if abs(i-(n-i)) < diff:
                        tmp1, tmp2 = i, n-i
                        diff = abs(i-(n-i))
                        count += 1
    print(tmp1, tmp2)
                        
            