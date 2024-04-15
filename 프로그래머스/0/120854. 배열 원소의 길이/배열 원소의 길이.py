def solution(strlist):
    answer = [0] * len(strlist)
    for i in range(len(strlist)):
        s = len(strlist[i])
        answer[i] = s
    pass
    return answer

def solve():
    strlist = ["I", "Love", "Programmers."]
    answer = solution(strlist)
    print("{}".format(answer))
    return

solve()