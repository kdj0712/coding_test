def solution(n):
    for x in range(n-1):
        if n == (x**2):
            answer = 1
            break
        else:
            answer = 2 
    return answer
