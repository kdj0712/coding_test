def solution(my_string):
    answer = [0]
    answer = answer * len(my_string)
    for i in range(len(my_string)):
        s = 0
        s = len(my_string)-(i+1)
        answer[i] = my_string[s]
        pass
    answer = ''.join(map(str, answer))
    return answer

def solve():
    my_string = "jaron"
    answer = solution(my_string)
    print(answer)
    return

solve()