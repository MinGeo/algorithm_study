n = int(input())
a = list(map(int, input().split()))
answer = 0
for i in a:
    count = 0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
    if count == 2:
        answer +=1
print(answer)