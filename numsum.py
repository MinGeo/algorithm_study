n = input()
a = input()
sum = 0
a = list(map(int, a))
for i in range(0, int(n)):
    sum += a[i]
    
print(sum)