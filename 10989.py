import sys
n = int(sys.stdin.readline())
count = [0 for i in range(10001)]

for i in range(n):
    count[int(sys.stdin.readline())] += 1
for i in range(1,10001):
    if count[i] != 0:
        for k in range(count[i]):
            print(i)