t = int(input())
case = []
for i in range(0, t*2):
    
    count = 0
    if i%2 == 0:
        k = int(input())
    else :
        n = int(input())
        answer=[[0 for col in range(n)] for row in range(k+1)]
        for t in range(k+1):
            for j in range(n):
                if t == 0:
                    answer[t][j] = j+1
                else :
                    answer[t][j] = sum(answer[t-1][0:j+1])
        print(answer[k][n-1])
                
    
    
    
    
        