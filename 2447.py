def append_star(LEN):
    if LEN == 1:
        return ['*']
    Stars = append_star(LEN//3)
    L = []  
    for S in Stars:
        L.append(S*3)
    for S in Stars: #맨 처음 star에 별 하나가 들어간 상태로 for문 3개가 실행됨 
        L.append(S+' '*(LEN//3)+S)#다음으로 N = 9, 27이런식으로 순서대로 들어가서 더해짐
    for S in Stars:
        L.append(S*3)#.join 되면서 계속해서 합쳐짐
    return L

n = int(input())
print('\n'.join(append_star(n)))