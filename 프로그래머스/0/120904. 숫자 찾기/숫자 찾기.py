def solution(num,k):
    s = str(num)
    answer = 0
    for x in range(len(s)):
        if str(k) == s[x]:
            answer = x+1
            break            
        else:
            answer = -1
    return answer