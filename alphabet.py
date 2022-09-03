a = list(input())
alen = len(a)
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
check = [-2 for i in range(len(alph))]
for i in range(len(alph)):
    tmp = 0
    for k in range(alen):
        if alph[i] == a[k]:
            if check[i] != -2:
                continue
            check[i] = k
        else:
            tmp += 1
        if tmp == alen:
            check[i] = -1
check = list(map(str, check))
print(' '.join(check))