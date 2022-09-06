t = int(input())

for i in range(t):
    floor = 0
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
        num = n//h 
    else :
        floor = n % h
        num = n//h + 1

    if num < 10:
        print('{a}0{b}'.format(a = floor, b = num))
    else :
        print('{a}{b}'.format(a = floor, b = num))
