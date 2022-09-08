n = int(input())
a = 2
answer = []
while True:
    if n == 1:
        break
    if n % a == 0:
        n = n / a
        print(a)
    else :
        a += 1