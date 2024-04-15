def solution(rsp):
    s = "2"
    r = "0"
    p = "5"
    answers = []
    for x in range(len(rsp)):
        if rsp[x] == s:
            answers.append(r)
        elif rsp[x] == r:
            answers.append(p)
        elif rsp[x] == p:
            answers.append(s)
    answer = ''.join(map(str, answers))
    return answer

def solve():
    rsp = "205"
    answer = solution(rsp)
    print("{}".format(answer))
    return

solve()