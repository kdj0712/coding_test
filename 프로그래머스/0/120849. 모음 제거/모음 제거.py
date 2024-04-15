def solution(my_string):
    y = "aeiou"
    answer = []
    for x in my_string:
        if x not in y:
            answer.append(x)
        else:
            pass
    answer = "".join(answer)
    return answer

def solve():
    my_string = "nice to meet you"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()