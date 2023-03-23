"""
입력
첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N, M <= 100)

둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.

출력

첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

입력 예시 1
3 3
3 1 2
4 1 4
2 2 2

출력 예시 1
2
"""
n, m = map(int, input().split())
data = []
temp = []
for i in range(0, n):   
    data.append(list(map(int, input().split())))

for k in range(0, n):
    temp.append(min(data[k]))
print(max(temp))