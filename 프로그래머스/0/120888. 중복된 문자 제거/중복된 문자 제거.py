def solution(my_string):
    answer = []
    my_string
    for x in range(len(my_string)):
        if my_string[x] in answer:
            pass
        elif my_string[x] not in answer:
            answer.append(my_string[x])
    answer = ''.join(map(str, answer))
    return answer