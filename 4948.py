import math
limit = 123456
check = [1]*(limit*2+1)
check[0] = 0
check[1] = 0

for i in range(2, len(check)):
    if check[i]:
        for k in range(2, int(math.sqrt(i)+1)):
            if i % k == 0:
                check[i] = 0
                break 

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(check[n+1:2*n+1]))
    