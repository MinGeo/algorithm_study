import math
m, n = map(int, input().split())
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
        print(i)

        
        