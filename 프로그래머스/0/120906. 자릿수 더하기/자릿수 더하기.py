def solution(n):
    n = str(n)
    lists = []
    for x in range(len(n)):
        lists.append(n[x])
    answer = 0
    for y in range(len(lists)):
        add = int(lists[y])
        answer = answer + add
    answer
    return answer

def solve():
    n = 930211
    answer = solution(n)
    print(answer)
    return

solve()