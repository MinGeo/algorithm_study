from re import I


n = int(input())
tmp = 1
i = 1
if n == 1:
    print(1)
else :
    while True:
        if n <= tmp:
            print(i)
            break
        tmp += 6*i 
        i += 1
