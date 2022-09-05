dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J',
        'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 
        'U', 'V'], ['W', 'X', 'Y', 'Z']]
result = 0
a = input()
for i in range(len(a)):
    for k in range(len(dial)):
        if a[i] in dial[k]:
            result = result + k + 3
print(result)