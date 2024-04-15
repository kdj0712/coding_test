def solution(n,numlist):
    answer = []
    for x in range(len(numlist)):
        if numlist[x]%n == 0:
            answer.append(numlist[x])
        else:
            pass
    return answer

def solve():
    n = 3
    numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    answer = solution(n, numlist)
    print(answer)
    return

solve()