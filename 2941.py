alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
count = 0
i = 0
while i < len(a):
    if (a[i:i+2] == 'c=') or (a[i:i+2] == 'c-') or (a[i:i+2] == 'd-') or (a[i:i+2]=='lj') or (a[i:i+2] == 'nj') or (a[i:i+2] == 's=') or (a[i:i+2] == 'z='):
        count += 1
        i = i + 2
    elif a[i:i+3] == 'dz=':
        count += 1
        i = i + 3
    else :
        count += 1
        i = i+1
print(count)