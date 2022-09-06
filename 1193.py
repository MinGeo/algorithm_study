x = int(input())
a = 0
b = 0
while x > a:
    b +=1
    a += b
gap = a-x
if b % 2 ==0:
    first = b - gap
    second = gap + 1
else : 
    first = gap + 1
    second = b - gap
print('{x}/{y}'.format(x = first, y = second))
    

    