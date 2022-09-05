ra = []
rb = []
n = int(input())
for i in range(n):
    a, b = input().split()
    ra.append(int(a))
    rb.append(b)
for i in range(n):
    rb[i] = list(map(lambda x: x*ra[i], list(rb[i])))
for i in range(n):
    print(''.join(rb[i]))