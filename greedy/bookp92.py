"""

입력

첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며,
각 자연수는 공백으로 구분한다.
둘쨰 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력

첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

입력 ex)
5 8 3
2 4 5 4 6

출력 ex)
46
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

result += first * k * (m//k)
result += second * (m % k)
print(result)
    


