def solution(my_string):
    answer = my_string.lower()
    answer = sorted(answer,reverse=False)
    answer = ''.join(map(str, answer))
    return answer