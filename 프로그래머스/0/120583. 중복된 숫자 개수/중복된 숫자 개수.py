def solution(array, n):
    answers = []
    answers = array
    answer = 0
    for x in answers:
        if x == n:
            answer = answer + 1
        else:
            answer = answer + 0
    return answer

def solve():
    array = [0, 2, 3, 4, 5]
    n = 1
    answer = solution(array, n)
    print(answer)
    return

solve()