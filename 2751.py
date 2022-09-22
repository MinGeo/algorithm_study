import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
data.sort()
print('\n'.join(map(str, data)))
    
