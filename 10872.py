n = int(input())
global answer
answer = 1
def factorial(n):
    global answer
    if n == 1:
        print(answer)
        return 
    elif n == 0:
        print(answer)
        return
    answer = answer * n
    factorial(n-1)

factorial(n)