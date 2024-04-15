def solution(my_string):
    answer = []
    for x in range(len(my_string)):
        try:
            num = int(my_string[x])
            answer.append(num)
        except:
            pass
    answer.sort(reverse=False)
    return answer