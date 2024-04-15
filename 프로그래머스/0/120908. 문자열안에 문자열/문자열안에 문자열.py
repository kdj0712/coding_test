def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2 
    return answer

def solve():
    str1 = "ab6CDE443fgh22iJKlmn1o"
    str2 = "6CD"
    answer = solution(str1, str2)
    print(answer)
    return

solve()