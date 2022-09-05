a, b, c = input().split()
a, b, c = int(a),int(b),int(c)
if c > b:
    print(a//(c-b)+1)
else:
    print(-1)