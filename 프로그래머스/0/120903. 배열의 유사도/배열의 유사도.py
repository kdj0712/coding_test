def solution(str1, str2):
    answer = 0
    for x in range(len(str2)):
        if str2[x] in str1: 
            answer = answer + 1
        else:
            answer
    return answer
