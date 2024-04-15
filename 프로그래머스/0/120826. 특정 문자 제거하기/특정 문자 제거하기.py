def solution(my_string, letter):
    i = len(my_string)
    answer = []
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer.append(my_string[i])
        elif my_string[i] == letter:
            pass
    answer =''.join(map(str, answer))
    return answer

def solve():
    my_string = "BCBdbe"
    letter = "B"
    answer = solution(my_string, letter)
    print(answer)
    return

solve()