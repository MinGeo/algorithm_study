n = int(input())
a = []
check = []
count = n
answer = 0
for i in range(n):
    a.append(list(map(str,input())))
for i in range(n):
    for k in range(len(a[i])-1):
        if a[i][k] != a[i][k+1]:
            if a[i][k] in a[i][k+1:len(a[i])]:
                count -= 1
                break
print(count)
                

        
            
        
