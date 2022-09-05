alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
        'U', 'V', 'W', 'X', 'Y', 'Z']
check = [0 for i in range(len(alph))]
tmp = 0
index = 0
a = input()
a = a.upper()
for i in range(len(a)):
    for k in range(len(alph)):
        if alph[k] == a[i]:
            check[k] += 1
            break
for i in range(len(check)):
    if max(check) == check[i]:
        tmp += 1
        index = i
if tmp == 1:
    print(alph[index])
else :
    print('?')