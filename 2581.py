import math
m = int(input())
n = int(input())
check = []

for i in range(m, n+1):
    tmp = True
    if i == 1:
        continue
    for k in range(2, int(math.sqrt(i)+1)):
        if i % k == 0:
            tmp = False
            #print(tmp)
            break
    if tmp == True:
        check.append(i)
if len(check) == 0:
    print(-1)
else :
    print(sum(check))
    print(min(check))
        
        