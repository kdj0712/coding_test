def solution(cipher,code):
    answers = []
    for x in range(len(cipher)):
        if (x+1) % code == 0:
            answers.append(cipher[x])
        else:
            pass
    answer = ''.join(map(str, answers))
    return answer

def solve():
    cipher = "pfqallllabwaoclk"
    code = 2
    answer = solution(cipher,code)
    print("{}".format(answer))
    return

solve()